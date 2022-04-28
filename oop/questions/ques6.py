class Dog:
    # class attribute
    attr1 = "mammal"

    # instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# accessing class methods
Rodger.speak()
Tommy.speak()
