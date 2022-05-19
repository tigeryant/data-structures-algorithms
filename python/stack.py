from contextlib import nullcontext


class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def is_empty(self):
        if self.top == -1:
            print('The stack is empty.')
            return True
        else:
            print('The stack is not empty.')
            return False

    def size(self):
        size = self.top + 1
        print(f'The size of the stack is {size} elements.')

    def top_element(self):
        if self.is_empty():
            print('There is no top element in the stack.')
        else:
            top_element = self.stack[self.top]
            print(f'The top element is: {top_element}.')
    
    def push(self, element):
        self.top = self.top + 1
        self.stack.insert(self.top, element)
        print(f'{element} was added to the stack.')

    def pop(self):
        if self.is_empty():
            print('Nothing to pop - the stack is empty.')
        else:
            element = self.stack[self.top]
            self.top = self.top - 1
            print(f'{element} was removed from the stack.')

myStack = Stack()

myStack.size()
myStack.top_element()

myStack.push(10)
myStack.push(20)
myStack.push(30)

myStack.size()
myStack.top_element()

myStack.pop()
myStack.size()
myStack.top_element()
    
