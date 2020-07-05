# Here we are importing the parent files/methods from filename animal and class Animal
from animal import Animal

# Here we are creating a new class called Human and linking the parent class Animals to it.
class Human(Animal):

    def __init__(self, eat, sleep, brush_teeth, comb_hair):
        super().__init__(eat, sleep)
        self.brush_teeth = brush_teeth
        self.comb_hair = comb_hair

    def tooth_ache(self):
        self.brush_teeth = "I need to brush my teeth"
        print("I need to brush my teeth")

    def messy_hair(self):
        self.comb_hair = True

daniel = Human("I am hungry", "I am sleepy!", "I need to brush my teeth!", "I need to comb my hair!")

print(daniel.sleep())
# print(daniel.brush_teeth)
# print(daniel.comb_hair)
# print(daniel.eat)
# print(daniel.sleep)
#print(daniel.tired())