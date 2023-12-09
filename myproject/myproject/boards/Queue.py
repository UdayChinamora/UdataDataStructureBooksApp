# Define a class to represent a queue
class Queue:

    # Initialize an empty list to store the elements and a max size
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Check if the queue is full
    def is_full(self):
        return len(self.items) == self.max_size

    # Add an element to the rear of the queue if not full
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        else:
            self.items.append(item)

    # Remove and return the element from the front of the queue if not empty
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    # Print the elements of the queue from front to rear
    def print_queue(self):
        for item in self.items:
            print(item, end=" ")
        print()
