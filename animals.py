from python_class_test import *

print("From the Animal class:")
Duck = Animal(animaltype = "duck")
Duck.legs = 2
Duck.arms = 2
Duck.eyes = 2
Duck.describe()

print("From the Person class:")
Jeff = Person("Jeff")
Jeff.greet()
Jeff.describe()

Anon = Person(legs = 1, arms = 4, eyes = 17)
Anon.greet("Blarg! Warble!")
Anon.describe()

print("From the Dog class:")
Fido = Dog("Fido")
Fido.greet()
Fido.describe()

print("From the Snake class:")
ASnake = Snake()
ASnake.greet()
ASnake.describe()

Snake2 = Snake("Sir Hiss", eyes = 3)
Snake2.greet()
Snake2.describe()
