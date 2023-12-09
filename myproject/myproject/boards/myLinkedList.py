# Define a class for the node of the linked list
class Node:
    # Initialize the node with the book data and the next pointer
    def __init__(self, id, title, author, price, status, next=None):
        self.id = id # The book ID
        self.title = title # The book title
        self.author = author # The book author
        self.price = price # The book price
        self.status = status # The book status
        self.next = next # The pointer to the next node



    def __str__(self):
        # return a string with the book data in a readable format
        return f"Book ID: {self.id}, Title: {self.title}, Author: {self.author}, Price: {self.price}, Status: {self.status}"

    def __repr__(self):
        # return a string with the Node class name and the book data as arguments
        return f"Node({self.id}, {self.title}, {self.author}, {self.price}, {self.status})"

    def __eq__(self, other):
        # return True if the book data of both nodes are equal, False otherwise
        return (
                    self.id == other.id and self.title == other.title and self.author == other.author and self.price == other.price and self.status == other.status)


# Define a class for the linked list
class LinkedList:
    # Initialize the linked list with the head and the tail pointers
    def __init__(self):
        self.head = None # The pointer to the first node
        self.tail = None # The pointer to the last node

    def __iter__(self):
        # start from the head node
        current = self.head
        # loop until the end of the list
        while current is not None:
            # yield the current node's value
            yield current.data
            # move to the next node
            current = current.next

    # Define a method to insert a new node at the end of the list
    def insert(self, id, title, author, price, status):
        # Create a new node with the book data
        new_node = Node(id, title, author, price, status)
        # If the list is empty, set the head and the tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Else, append the new node to the tail and update the tail pointer
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Define a method to delete a node by its book ID
    def delete(self, id):
        # If the list is empty, return None
        if self.head is None:
            return None
        # If the head node has the matching ID, remove it and update the head pointer
        if self.head.id == id:
            removed_node = self.head
            self.head = self.head.next
            return removed_node
        # Else, traverse the list until the node with the matching ID is found or the end is reached
        else:
            current_node = self.head
            while current_node.next is not None:
                # If the next node has the matching ID, remove it and update the pointers
                if current_node.next.id == id:
                    removed_node = current_node.next
                    current_node.next = current_node.next.next
                    # If the removed node is the tail, update the tail pointer
                    if removed_node == self.tail:
                        self.tail = current_node
                    return removed_node
                # Else, move to the next node
                else:
                    current_node = current_node.next
            # If the node with the matching ID is not found, return None
            return None

    # Define a method to traverse the list and print the book data
    def traverse(self):
        # If the list is empty, print a message
        if self.head is None:
            print("The list is empty")
        # Else, iterate over the nodes and print their data
        else:
            current_node = self.head
            while current_node is not None:
                print(f"ID: {current_node.id}, Title: {current_node.title}, Author: {current_node.author}, price: {current_node.price}, Status: {current_node.status}")
                current_node = current_node.next




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
            # If the node with the matching title is not found, return None
            return None


