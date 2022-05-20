class Queue():
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.queue = []

    def is_empty(self):
        if (self.front == self.rear):
            return True
        return False

    def enqueue(self, element):
        self.rear = self.rear + 1
        self.queue.insert(self.rear, element)

    def dequeue(self):
        if (self.is_empty()):
            return None
        else:
            self.front = self.front + 1
            return self.queue[self.front]
