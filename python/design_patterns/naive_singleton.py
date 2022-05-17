class SingletonMeta(type):
    """Private dictionary variable to store the singleton class instance"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Instantiates a class, or returns the single class instance"""

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def instance_logic(self):
        """Instance logic statments"""

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contian different instances.")
        
        