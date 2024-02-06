Doubly Linked List-Based Stack Implementation in Python

This Python implementation provides a stack data structure based on a doubly linked list. A doubly linked list allows for efficient addition and removal of elements at the top of the stack, following the Last In, First Out (LIFO) principle.

Node Class
Constructor (__init__):
Parameters:
item: The value to be stored in the node.
Attributes:
item: The value stored in the node.
next: Reference to the next node in the list.
prev: Reference to the previous node in the list.
Stack Class
Constructor (__init__):
Attributes:
size: Current size of the stack.
top: Reference to the top of the stack.
push Method:
Parameters:
item: The value to be added to the stack.
Description:
Adds a new item to the top of the stack.
peek Method:
Returns:
The item on the top of the stack without removing it, or None if the stack is empty.
pop Method:
Returns:
The item removed from the top of the stack, or None if the stack is empty.
showStack Method:
Description:
Displays the elements of the stack in a visual representation.
clear Method:
Description:
Clears the stack, removing all elements.
Implementation Details
The stack implementation utilizes a doubly linked list structure, where each node in the list maintains references to both the next and previous nodes. This structure allows for efficient manipulation of the stack, enabling fast addition, removal, and peeking operations.

Usage
Import the classes:

python

from stack import Node, Stack
Create an instance of the Stack class:

python

my_stack = Stack()
Use the various methods:

python
Copy code
my_stack.push(42)
top_item = my_stack.peek()
popped_item = my_stack.pop()
my_stack.showStack()
my_stack.clear()
Feel free to incorporate this doubly linked list-based stack implementation into your projects and modify it based on your specific requirements. If you encounter any issues or have suggestions for improvements, please feel free to contribute.
