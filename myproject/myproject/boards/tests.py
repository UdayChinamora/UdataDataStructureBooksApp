# Import the unittest module and the queue class
import unittest

from myproject.myproject.boards.Queue import Queue
from myproject.myproject.boards.myLinkedList import LinkedList


# Define a test class that inherits from unittest.TestCase
class TestQueue(unittest.TestCase):

    # Define a setUp method that runs before each test
    def setUp(self):
        # Create a queue object with max size 5
        self.queue = Queue(5)

    # Define a test method for is_empty
    def test_is_empty(self):
        # Check that the queue is initially empty
        self.assertTrue(self.queue.is_empty())
        # Add an element to the queue
        self.queue.enqueue(1)
        # Check that the queue is not empty
        self.assertFalse(self.queue.is_empty())

    # Define a test method for is_full
    def test_is_full(self):
        # Check that the queue is initially not full
        self.assertFalse(self.queue.is_full())
        # Add 5 elements to the queue
        for i in range(5):
            self.queue.enqueue(i)
        # Check that the queue is full
        self.assertTrue(self.queue.is_full())

    # Define a test method for enqueue
    def test_enqueue(self):
        # Check that the queue is initially empty
        self.assertEqual(len(self.queue.items), 0)
        # Add an element to the queue
        self.queue.enqueue(1)
        # Check that the queue has one element
        self.assertEqual(len(self.queue.items), 1)
        # Check that the element is at the rear of the queue
        self.assertEqual(self.queue.items[-1], 1)
        # Add another element to the queue
        self.queue.enqueue(2)
        # Check that the queue has two elements
        self.assertEqual(len(self.queue.items), 2)
        # Check that the element is at the rear of the queue
        self.assertEqual(self.queue.items[-1], 2)
        # Try to add an element to a full queue
        for i in range(3, 6):
            self.queue.enqueue(i)
        self.queue.enqueue(6)
        # Check that the queue is still full
        self.assertEqual(len(self.queue.items), 5)
        # Check that the element is not added to the queue
        self.assertNotIn(6, self.queue.items)

    # Define a test method for dequeue
    def test_dequeue(self):
        # Check that the queue is initially empty
        self.assertEqual(len(self.queue.items), 0)
        # Try to dequeue from an empty queue
        self.assertIsNone(self.queue.dequeue())
        # Add some elements to the queue
        for i in range(1, 4):
            self.queue.enqueue(i)
        # Check that the queue has three elements
        self.assertEqual(len(self.queue.items), 3)
        # Dequeue an element from the queue
        item = self.queue.dequeue()
        # Check that the item is the first element added
        self.assertEqual(item, 1)
        # Check that the queue has two elements
        self.assertEqual(len(self.queue.items), 2)
        # Dequeue another element from the queue
        item = self.queue.dequeue()
        # Check that the item is the second element added
        self.assertEqual(item, 2)
        # Check that the queue has one element
        self.assertEqual(len(self.queue.items), 1)

    # Define a test method for print_queue
    def test_print_queue(self):
        # Check that the queue is initially empty
        self.assertEqual(len(self.queue.items), 0)
        # Capture the output of print_queue
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        self.queue.print_queue()
        # Check that the output is an empty line
        self.assertEqual(output.getvalue(), "\n")
        # Add some elements to the queue
        for i in range(1, 4):
            self.queue.enqueue(i)
        # Capture the output of print_queue
        output = StringIO()
        sys.stdout = output
        self.queue.print_queue()
        # Check that the output is the elements from front to rear
        self.assertEqual(output.getvalue(), "1 2 3 \n")

    # Test if a new node is inserted correctly at the end of a non-empty list:
    def test_insert_non_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert(1, "Book1", "Author1", 10.99, "Available")
        linked_list.insert(2, "Book2", "Author2", 15.99, "Unavailable")
        assert linked_list.head.id == 1
        assert linked_list.head.title == "Book1"
        assert linked_list.head.author == "Author1"
        assert linked_list.head.price == 10.99
        assert linked_list.head.status == "Available"
        assert linked_list.tail.id == 2
        assert linked_list.tail.title == "Book2"
        assert linked_list.tail.author == "Author2"
        assert linked_list.tail.price == 15.99
        assert linked_list.tail.status == "Unavailable"
        assert linked_list.head.next == linked_list.tail

    # Test if a new node is inserted correctly at the end of an empty list:

    def test_insert_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert(1, "Book1", "Author1", 10.99, "Available")
        assert linked_list.head.id == 1
        assert linked_list.head.title == "Book1"
        assert linked_list.head.author == "Author1"
        assert linked_list.head.price == 10.99
        assert linked_list.head.status == "Available"
        assert linked_list.head == linked_list.tail

    # Test if multiple nodes are inserted correctly at the end of the list:
    def test_insert_multiple_nodes(self):
        linked_list = LinkedList()
        linked_list.insert(1, "Book1", "Author1", 10.99, "Available")
        linked_list.insert(2, "Book2", "Author2", 15.99, "Unavailable")
        linked_list.insert(3, "Book3", "Author3", 12.99, "Available")
        assert linked_list.head.id == 1
        assert linked_list.head.title == "Book1"
        assert linked_list.head.author == "Author1"
        assert linked_list.head.price == 10.99
        assert linked_list.head


# Run the tests
if __name__ == "__main__":
    unittest.main()
