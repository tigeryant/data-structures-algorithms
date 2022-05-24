import sys

class MinHeap:
    def __init__(self, maxsize):
       self.maxsize = maxsize
       self.size = 0
       self.Heap = [0] * (self.maxsize + 1)
       self.Heap[0] = -1 * sys.maxsize
       self.FRONT = 1

    # return the position of the parent of the node at pos
    def parent(self, pos):
        return pos // 2

    # return the position of the left child of the node at pos
    def left_child(self, pos):
        return 2 * pos

    # return the position of the right child of the node at pos
    def right_child(self, pos):
        return (2 * pos) + 1

    # return true if passed node is leaf node
    def is_leaf(self, pos):
        return pos * 2 > self.size

    # swap two nodes on the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # heapify the node at pos
    def min_heapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its children
        if not self.is_leaf(pos):
            if (self.Heap[pos] > self.Heap[self.left_child(pos)] or 
               self.Heap[pos] > self.Heap[self.right_child(pos)]):
  
                # swap with the left child and heapify
                # the left child
                if self.Heap[self.left_child(pos)] < self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
  
                # swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    # insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
  
        current = self.size
  
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
  
    # print the contents of the heap
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))
  
    # build the min heap using
    # the min_heapify function
    def min_heap(self):
  
        for pos in range(self.size//2, 0, -1):
            self.min_heapify(pos)
  
    # remove and return the minimum
    # element from the heap
    def remove(self):
  
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.min_heapify(self.FRONT)
        return popped
    
    # Driver Code
if __name__ == "__main__":
      
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(8)
    minHeap.insert(9)
    minHeap.insert(12)
    minHeap.insert(19)
    minHeap.insert(15)
    minHeap.insert(21)
    minHeap.insert(2)
    minHeap.insert(32)
    minHeap.insert(4)
    minHeap.min_heap()
  
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))