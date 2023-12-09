import sqlite3
import queue

#from myproject.boards.models import Book


from .models import Book


# Define a function to sort a list of books using a priority queue
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


# Connect to the database
conn = sqlite3.connect('db.FinalProjectBooksDB')

# Create a cursor object
cur = conn.cursor()

# Execute the SQL query
cur.execute('SELECT title FROM boards_book')

# Fetch the results as a list of tuples
books = cur.fetchall()

# Test the function with the books from the database
books = Book.objects.all()
sorted_books = sort_books(books)  # Sort the books using the function
for book in sorted_books:  # Print the sorted books
    print(book)
