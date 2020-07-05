# Here we are creating a class called Animal. Note classes should start with a capital letter.
class Animal:

    def __init__(self, eat, sleep):
        self.eat = eat
        self.sleep = sleep

    # Here we are creating methods
    def hunger(self):
        self.eat ="I am hungry!! YUM"
        print("I am hungry!!")
        self.eat = False

    def tired(self):
        if self.sleep == True:
            print("Yawnnn get some sleep!")
        elif self.sleep == False:
            print("Im not tired yet")


animal = Animal("Hungry!!", "Sleepy!!")

animal.tired()