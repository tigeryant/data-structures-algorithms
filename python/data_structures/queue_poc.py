class Queue():
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.queue = []

    def is_empty(self):
        if (self.front == self.rear):
            return True
        return False

    def size(self):
        size = self.rear - self.front
        print(f"The size of the queue is {size} element(s).")
    
    def front_element(self):
        if (self.is_empty()):
            print("There is no front element - the queue is empty")
        else:
            front_element = self.queue[self.front + 1]
            print(f"The front element is {front_element}.")
        
    def rear_element(self):
        if (self.is_empty()):
            print("There is no rear element - the queue is empty.")
        else:
            rear_element = self.queue[self.rear]
            print(f"The rear element is {rear_element}")
    
    def enqueue(self, element):
        self.rear = self.rear + 1
        self.queue.insert(self.rear, element)
        print(f"{element} was added to the queue.")
    
    def dequeue(self):
        if (self.is_empty()):
            print("Cannot dequeue - the queue is empty.")
        else:
            self.front = self.front + 1
            element = self.queue[self.front]
            print(f"{element} was deleted from the queue.")
        
myQueue = Queue()

if (myQueue.is_empty()):
    print("The queue is empty.")
else:
    print("The queue is not empty.")

myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)
myQueue.front_element()
myQueue.rear_element()
myQueue.size()

myQueue.dequeue()
myQueue.front_element()
myQueue.rear_element()
myQueue.size()

myQueue.dequeue()
myQueue.dequeue()
myQueue.front_element()
myQueue.rear_element()
myQueue.size()

if (myQueue.is_empty()):
    print("The queue is empty.")
else:
    print("The queue is not empty.")

myQueue.dequeue()
myQueue.front_element()
myQueue.rear_element()
myQueue.size()

if (myQueue.is_empty()):
    print("The queue is empty.")
else:
    print("The queue is not empty.")
