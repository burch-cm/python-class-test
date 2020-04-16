class Animal:
	def __init__(self, name = "none", animaltype = "undefined", legs = 0, arms = 0, eyes = 0):
		self.name = name
		self.animaltype = animaltype
		self.legs = legs
		self.arms = arms
		self.eyes = eyes

	def greet(self, greeting = ""):
		pass

	def describe(self):
		name = self.name
		if self.name == "none":
			name = "This"
		if self.animaltype.startswith(("a", "e", "i", "o", "u")):
			article = "an"
		else:
			article = "a"
		print("{name} is {article} {animaltype}, with {legs} legs, {arms} arms, and {eyes} eyes.\n".format(
				name = name, 
				article = article,
				animaltype = self.animaltype, 
				legs = self.legs, 
				arms = self.arms, 
				eyes = self.eyes)
			)

class Person(Animal):
	def __init__(self, name = "none", legs = 2, arms = 2, eyes = 2):
	    super().__init__(name, animaltype = "human",
	    	             legs = legs, arms = arms, eyes = eyes)

	def greet(self, greeting = "Hello"):
		if self.name != "none":
			nameref = "My name is {}".format(self.name)
		else:
			nameref = "I don't have a name."
		print("{}! {}".format(greeting, nameref))

class Dog(Animal):
	def __init__(self, name = "none", legs = 4, eyes = 2):
		super().__init__(name, animaltype = "dog", legs = legs, eyes = eyes)

	def greet(self):
		print("Woof!")

class Snake(Animal):
	def __init__(self, name = "none", eyes = 2):
	    super().__init__(name, animaltype = "snake", eyes = eyes)

	def greet(self):
		print("Hiiisssss!")
