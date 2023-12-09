import queue

from .models import Book

# Initialize the queue with a fixed size
queue = queue.Queue(maxsize=6)


def enqueue(item):
    # Try to put the item in the queue
    try:
        queue.put(item)
    # If the queue is full, raise an exception
    except queue.Full:
        raise queue.Full("Queue is full")


def dequeue():
    # Try to get the item from the queue
    try:
        item = queue.get()
        return item
    # If the queue is empty, raise an exception
    except queue.Empty:
        raise queue.Empty("Queue is empty")


def printQueue():
    # Initialize an empty list to store the queue items
    items = []
    # Iterate over the queue items
    for item in queue.queue:
        # Append the item to the list
        items.append(item)
    # Join the list with commas and return the string
    return ", ".join(items)


# Create a node class to store book details
class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


# Create a linked list class to store and manipulate book nodes
class LinkedList:
    def __init__(self):
        self.head = None  # pointer to the first node
        self.size = 0  # number of nodes in the list

    # Add a node to the end of the list
    def append(self, book):
        new_node = Node(book)
        if self.head is None:  # if the list is empty
            self.head = new_node
        else:  # if the list is not empty
            current = self.head
            while current.next:  # loop until the last node
                current = current.next
            current.next = new_node
        self.size += 1  # increment the size of the list

    # Delete a node from the list by book_id
    def delete(self, book_id):
        if self.head is None:  # if the list is empty
            return False
        else:  # if the list is not empty
            current = self.head
            previous = None
            while current:  # loop until the end of the list
                if current.book.book_id == book_id:
                    if previous is None:  # if the current node is the head
                        self.head = current.next
                    else:  # if the current node is not the head
                        previous.next = current.next
                    self.size -= 1  # decrement the size of the list
                    return True
                else:  # if the current node does not have the matching book_id
                    previous = current
                    current = current.next
            return False  # no matching book_id found

    # Update a node in the list by book_id and new book details
    def update(self, book_id, new_book):
        if self.head is None:
            return False
        else:  # if the list is not empty
            current = self.head
            while current:  # loop until the end of the list
                if current.book.book_id == book_id:  # if the current node has the matching book_id
                    current.book = new_book  # replace the book object with the new book object
                    return True
                else:
                    current = current.next
            return False  # no matching book_id found

    # Display the list as a string
    def __str__(self):
        result = ""  # initialize an empty string
        current = self.head
        while current:  # loop until the end of the list
            result += f"{current.book.book_id}: {current.book.title}\n"
            current = current.next
        return result  # return the result

# Define a method to search the list by a given title

    def search(self, title):
        # If the list is empty, return None
        if self.head is None:
            return None
        # Else, traverse the list until the node with the matching title is found or the end is reached
        else:
            current_node = self.head
            while current_node is not None:
                # If the node has the matching title, return the node
                if current_node.title == title:
                    return current_node
                # Else, move to the next node
                else:
                    current_node = current_node.next

            return None


# Create a linked list object
book_list = LinkedList()
# Loop through all the books in the database and add them to the linked list
books = Book.objects.all()
for book in books:
    book_list.append(book)
