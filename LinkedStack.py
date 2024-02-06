class Node:
    def __init__(self, item):
        """
        Constructor for the Node class.

        Args:
            item: The value to be stored in the node.
        """
        self.item = item
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        """
        Constructor for the Stack class.
        Initializes an empty stack.
        """
        self.size = 0
        self.top = None

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def push(self, item):
        """
        Add a new item to the top of the stack.

        Args:
            item: The value to be added to the stack.
        """
        newTop = Node(item)
        if self.isEmpty():
            self.top = newTop
        else:
            newTop.prev = self.top
            self.top.next = newTop
            self.top = newTop
        self.size += 1

    def peek(self):
        """
        Peek at the item on the top of the stack without removing it.

        Returns:
            The item on the top of the stack, or None if the stack is empty.
        """
        if not self.isEmpty():
            return self.top.item
        else:
            return None

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        Returns:
            The item removed from the top of the stack, or None if the stack is empty.
        """
        if not self.isEmpty():
            popped_item = self.top.item
            self.top = self.top.prev
            self.size -= 1
            return popped_item
        else:
            return None

    def showStack(self):
        """
        Display the elements of the stack.

        Prints a visual representation of the stack elements.
        """
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack Elements:")
            currentNode = self.top
            while currentNode:
                print("|", currentNode.item, "|")
                print("  ---")
                currentNode = currentNode.prev

    def clear(self):
        """
        Clear the stack, removing all elements.
        """
        self.top = None
        self.size = 0
