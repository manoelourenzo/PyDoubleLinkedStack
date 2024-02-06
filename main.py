from LinkedStack import *

stack = Stack()
while True:
    stack.showStack()
    print("\nOptions:")
    print("1. Push an element onto the stack")
    print("2. Pop an element from the stack")
    print("3. Display the stack")
    print("4. Clear stack")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        value = int(input("Enter the value to push onto the stack: "))
        stack.push(value)
        print(f"{value} pushed onto the stack.")
    elif choice == "2":
        popped_item = stack.pop()
        if popped_item is not None:
            print(f"Popped item: {popped_item}")
        else:
            print("Cannot pop from an empty stack.")
    elif choice == "3":
        stack.showStack()

    elif choice == "4":
        print("Cleaning Stack...")
        stack.clear()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")