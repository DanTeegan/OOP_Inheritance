# Here we are importing the parent files/methods from filename animal and class Animal
from animal import Animal

# Here we are creating a new class called Human and linking the parent class Animals to it.
class Human(Animal):

    def __init__(self, eat, sleep, brush_teeth, comb_hair):
        super().__init__(eat, sleep)
        self.brush_teeth = brush_teeth
        self.comb_hair = comb_hair

    def tooth_ache(self):
        self.brush_teeth = True

    def messy_hair(self):
        self.comb_hair = True

human = Human("I am hungry", "I am Tired", "Brush your teeth!", "Brush your hair!")

print(human.hunger())
print(human.messy_hair())
print(human.tired())