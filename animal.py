# Here we are creating a class called Animal. Note classes should start with a capital letter.
class Animal:

    def __init__(self, eat, sleep):
        self.eat = eat
        self.sleep = sleep

    # Here we are creating methods
    def hunger(self):
        self.eat = "I am hungry"
        print("I am hungry")

    def tired(self):
        self.sleep = True

animal = Animal(True, "ZZZZZZZ")

