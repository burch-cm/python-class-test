from python_class_test import *

Duck = Animal(animaltype = "duck")
Duck.set_legs(2)
Duck.set_arms(2)
Duck.set_eyes(2)
Duck.describe()

Maurice = Animal("Maurice", animaltype = "wombat")
Maurice.set_legs(4)
Maurice.set_eyes(2)
Maurice.describe()

Daniel = Animal("Daniel", "anteater")
Daniel.set_legs(4)
Daniel.set_eyes(2)
Daniel.describe()

Polyphemus = Animal("Polyphemus", "cyclops")
Polyphemus.set_legs(2)
Polyphemus.set_arms(2)
Polyphemus.set_eyes(1)
Polyphemus.describe()

Jeff = Person("Jeff")
Jeff.greet()
Jeff.describe()

Anon = Person(legs = 1, arms = 4, eyes = 17)
Anon.greet("Blarg! Warble!")
Anon.describe()