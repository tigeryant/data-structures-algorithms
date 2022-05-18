from abc import ABC, abstractmethod

# The Duck interface ensures that subclasses implement its methods
class Duck(ABC):
    @abstractmethod
    def quack():
        pass

    @abstractmethod
    def fly():
        pass

# The ConcreteDuck class implements the methods defined in the Duck interface
class ConcreteDuck(Duck):
    def quack():
        print("Quack")

    def fly():
        print("I'm flying")

# The Turkey interface enforces different methods on its subclasses than the Duck class
class Turkey(ABC):
    @abstractmethod
    def gobble():
        pass

    @abstractmethod
    def fly():
        pass

# The ConcreteTurkey class implements the methods defined in the Turkey interface
class ConcreteTurkey(Turkey):
    def gobble():
        print("Gobble gobble")

    def fly():
        print("I'm flying a short distance")

# ADAPTER

# Here we want to use a Turkey in place of a duck by having the client interface with the TurkeyAdapter.
# This allows the client to treat the TurkeyAdapter as if it were a duck.

# First, we implement the interface of the type we're adapting to. This is the interface the client expects
# to see. Here, the TurkeyAdapter implements the Duck interface.

# We are adapting (FROM) a turkey to a Duck

class TurkeyAdapter(Duck):

    # ERROR IS HERE, IN THE NEXT FEW LINES
    # Should this be instantiated here? What should be passed to the constructor? See the errors
    
    turkey = Turkey()

    # Next, we need a reference to the object that we're adapting - we do that through the constructor
    def __init__(self, turkey):
        self.turkey = turkey

    # Next, we implement the methods in the interface we're adapting to.
    def quack(self):
        self.turkey.gobble()
    
    # Turkeys implement the fly() method differently to ducks, so we call the turkey's fly() method five times to 
    # demonstrate this
    def fly(self):
        for x in range(6):
           self.turkey.fly() 

# This method is passed a duck object and calls its methods
def test_duck(duck):
    duck.quack()
    duck.fly()

# Here we can test the adapter
# We create instances of both the turkey and the duck
mallard_duck = ConcreteDuck()
wild_turkey = ConcreteTurkey()

# Now we wrap the turkey in a TurkeyAdapter, which makes it appear like a duck from the outside
turkey_adapter = TurkeyAdapter(wild_turkey)

# Test the turkey by calling its gobble and fly methods
print("Wild turkey says: ")
turkey_adapter.gobble()
turkey_adapter.fly()

# Test the duck by passing the duck object to the testDuck() method above
print("The duck says: ")
test_duck(mallard_duck)

# Test the turkey adapter (which should behave like a duck) by passing the turkey_adapter instance to the test_duck()
# method (which expects a duck object)
print("The turkey adapter says: ")
test_duck(turkey_adapter)


