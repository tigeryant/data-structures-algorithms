## Algorithms

### Insertion sort
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. This algorithm runs in quadratic time, and can be used when n is low (where n is the number of items to be sorted). Insertion sort is analogous to sorting a card deck with both hands.

### Bubble sort
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order. It has a time complexity of O(n^2).

### Linear search
Linear search is a simple search algorithm that sequentially checks each element of the list until a match is found or the whole list has been searched. It has a time complexity of O(n).

### Binary search
Binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. It repeatedly halves the divides the search interval in half. It has a time complexity of O(log n).

### Breadth first search
Breadth-first search is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. The Time complexity of BFS is O(V + E) when an adjacency list is used and O(V^2) when an adjacency matrix is used.

</br>

## Data structures

### Stack
A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.
* Stack data structure implemented in PHP - functions include: `isEmpty()`, `size()`, `topElement()`, `push()` and `pop()`.
* Stack data structure implemented in Python - functions include: `is_empty()`, `size()`, `top_element()`, `push()` and `pop()`.

### Queue
Queue is a similar data structure to a stack, but it is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue). Queue follows First In First Out methodology, i.e., the data item stored first will be accessed first.
* Queue data structure implemented in PHP - functions include: `isEmpty()`, `size()`, `frontElement()`, `rearElement()`, `enQueue()` and `deQueue()`.
* Queue data structure implemented in Python - functions include: `is_empty()`, `size()`, `front_element()`, `rear_element`, `enqueue()` and `dequeue()`.

### Min heap
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.

</br>

## Design patterns

### Singleton
The singleton ensures a class has only one instance, and provides a global point of access to it. The example is a naive implementation of a singleton in Python that makes use of metaclasses. It is naive because it does not behave correctly in a multi-threaded environment - that is, multiple threads can call the creation method simultaneously and get several instances of Singleton class.

### Factory method
The factory method defines an interface for creating an object, but lets subclasses decide which class to instantiate. It lets a class defer instantiation to subclasses. The example shows a basic implementation of the factory method in Python. The user is prompted at runtime to decide which object they want to instantiate. The responsibility of instantiating a concrete class (`Student` or `Teacher`) is delegated to the `PersonFactory` class. `Teacher` and `Student` both implement the `IPerson` interface, which ensures that each of them implement the `person_method()`.

### Observer
The observer defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. The example is an implementation of the observer pattern using `Subject` and `Object` interfaces and concrete subclasses for each of these interfaces. Observers can be added, removed and notified, and they update themselves when they are notified of a state change in the subject they are observing.

### Adapter
The adapter design pattern converts the interface of a class into another interface clients expect. It let's classes work together that couldn't otherwise because of incompatible interfaces. In the example, a `TurkeyAdapter` adapts a `Turkey` interface into a `Duck` interface.

### Facade
The facade pattern provides a uniﬁed interface to a set of interfaces in a subsytem. Facade deﬁnes a higher-level interface that makes the subsystem easier to use. The example implements a 'home theater' subsystem, and a `HomeTheaterFacade` as the interface to this subsystem. The client interacts with the facade, which is simpler than interacting with the objects in the subsystem individually.
