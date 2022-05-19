## Algorithms

### Insertion sort
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. This algorithm runs in quadratic time, and can be used when n is low (where n is the number of items to be sorted). Analogous to sorting a card deck with both hands.

</br>

## Data structures

### Stack
* Stack data structure implemented in PHP - functions include: `isEmpty()`, `size()`, `topElement()`, `push()` and `pop()`.
* Stack data structure implemented in Python - functions include: `is_empty()`, `size()`, `top_element()`, `push()` and `pop()`.

### Queue
* Queue data structure implemented in PHP - functions include: `isEmpty()`, `size()`, `frontElement()`, `rearElement()`, `enQueue()` and `deQueue()`.
* Queue data structure implemented in Python - functions include: `is_empty()`, `size()`, `front_element()`, `rear_element`, `enqueue()` and `dequeue()`.

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
