import queue

import form
from django import forms
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.template import loader

from .EnQueue import enqueue, printQueue, LinkedList
from .forms import BookForm, BooksForm
from .models import Book, Review, Author, BookStore


# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


"""def book_list(request):
    query = request.GET.get('search')
    if query:
        books = Book.objects.filter(Q(title__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
"""


def my_books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def linked_list_books(request):
    template = loader.get_template('linkedlist_books.html')
    return HttpResponse(template.render())


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    genre = book.genre.all()
    reviews = Review.objects.filter(book=book)

    context = {
        'book': book,
        'genre': genre,
        'reviews': reviews,
    }

    return render(request, 'book_detail.html', context)





# Define the sort_books function
def sort_books(books):
    # Create an empty priority queue
    pq = queue.PriorityQueue()

    # Enqueue each book into the priority queue
    for book in books:
        pq.put(book)

    # Create an empty list to store the sorted books
    sorted_books = []

    # Dequeue each book from the priority queue and append it to the sorted list
    while not pq.empty():
        sorted_books.append(pq.get())

    # Return the sorted list of books
    return sorted_books


# Define the sorted_book_list view
def sorted_book_list(request):
    # Get all the books from the database
    books = Book.objects.all()

    # Sort the books using the function
    sorted_books = sort_books(books)

    # Render the template with the sorted books
    return render(request, 'books_sorted_template.html', {'sorted_books': sorted_books})


def enqueue_view(request):
    # Get all the books from the database
    books = Book.objects.all()
    titles = list(books.values_list('title', flat=True))
    # Add some items to the queue
    try:
        enqueue(titles[1])
        enqueue(titles[3])
        enqueue(titles[0])
        # Call the printQueue() function and get the output string
        output = printQueue()
    # If the queue is full, display a message
    except queue.Full:
        output = "Queue is full"
    # Render the template with the output string
    return render(request, 'enqueue_template.html', {'output': output})


# Create a hashmap to store book_title as the key and book object as the value
book_map = {}
# Loop through all the books in the database and add them to the hashmap
books = Book.objects.all()
for book in books:
    book_map[book.title] = book


# Define a function to delete a book from the database and the hashmap
def delete_book(request):
    # Get the book_title from the request
    book_title = request.POST.get('book_title')
    # Check if the book_title is valid and exists in the hashmap
    if book_title and book_title in book_map:
        # Get the book object from the hashmap
        book = book_map[book_title]
        # Delete the book from the database
        try:
            book.delete()
        except Exception as e:
            return HttpResponse(f'Error deleting book: {str(e)}')
        # Delete the book from the hashmap
        del book_map[book_title]
        # Return a success message
        return HttpResponse(f'Book {book_title} deleted successfully.')
    else:
        # Return an error message
        return HttpResponse('Invalid book_title.')


# Define a function to display the remaining books in the database and the hashmap
def map_book_list(request):
    # Get the remaining books from the database
    books = Book.objects.all()
    # Render the book_list.html template with the books and the hashmap as context
    return render(request, 'Map_book_list.html', {'books': books, 'book_map': book_map})


# Define a function to edit a book in the database and the linked list
def edit_book(request):
    # Get the book_id and new book details from the request
    book_id = request.POST.get('book_id')
    new_title = request.POST.get('new_title')
    new_author = request.POST.get('new_author')
    new_published_date = request.POST.get('new_published_date')
    new_price = request.POST.get('new_price')

    new_image_url = request.POST.get('new_image_url')
    # Check if the book_id is a valid integer
    try:
        book_id = int(book_id)
    except ValueError:
        # Return an error message
        return HttpResponse('Invalid book_id. It must be an integer.')
    # Check if the new book details are valid
    if new_title and new_author and new_published_date and new_price and new_image_url:
        # Create a new book object with the new book details
        new_book = Book(title=new_title, author=new_author, published_date=new_published_date, price=new_price,
                        image_url=new_image_url)
        # Update the book in the database
        book_queryset = Book.objects.filter(id=book_id)
        # Update the book in the linked list
        book_queryset.update(title=new_title, author=new_author, published_date=new_published_date, price=new_price,
                             image_url=new_image_url)
        # Return a success message
        return HttpResponse(f'Book {book_id} edited successfully.')
    else:
        # Return an error message
        return HttpResponse('Invalid new book details.')


def edited_book_list(request):
    # Get the books from the database
    books = Book.objects.all()
    # Render the book_list.html template with the books and the linked list as context
    return render(request, 'edit_using_LinkedList.html', {'books': books, 'book_list': book_list})


# Create a queue object
book_queue = queue.Queue()


def queue_book_view(request):
    # If the request is a POST method, get the book title from the form and enqueue it
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_title = form.cleaned_data['book_title']
            if not book_title.isnumeric() and Book.objects.filter(title=book_title).exists():
                book_queue.put(book_title)
            else:
                error_message = "Oops! The book title doesn't exist or you entered an integer. Please try again."
                return HttpResponse(error_message)

    # If the request is a GET method, check if there is a 'remove' parameter and dequeue the book
    elif request.method == 'GET':
        if 'remove' in request.GET:
            book_queue.get()

    # Render the template with the book queue as context
    return render(request, 'queue_books.html', {'book_queue': book_queue})


def search_books(request):
    search_query = request.GET.get('search_query', '')

    if search_query:
        # Search for books with matching title
        searched_books = Book.objects.filter(title__icontains=search_query)

        if not searched_books:
            error_message = "Sorry, no books found with that title."
            context = {
                "searched_books": searched_books,
                "search_query": search_query,
                "error_message": error_message
            }
        else:
            context = {
                "searched_books": searched_books,
                "search_query": search_query
            }
    else:
        context = {}
    return render(request, "searched_book_list.html", context)


# Create a global linked list object
book_list = LinkedList()


