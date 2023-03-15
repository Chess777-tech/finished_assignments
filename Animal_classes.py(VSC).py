class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_noise(self):
        print(f"{self.name} is making noise.")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "dog")

    def make_noise(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "cat")

    def make_noise(self):
        print(f"{self.name} meows.")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "bird")

    def make_noise(self):
        print(f"{self.name} chirps.")


# Create some animals
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 5)
bird = Bird("Tweety", 1)

# Make the animals eat, sleep, and make noise
dog.eat()        # Output: Buddy is eating.
cat.sleep()      # Output: Whiskers is sleeping.
bird.make_noise()  # Output: Tweety chirps.

# Make the animals make their respective noises
dog.make_noise()  # Output: Buddy barks.
cat.make_noise()  # Output: Whiskers meows.
bird.make_noise()  # Output: Tweety chirps.
