#
class Zoo:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print(f"{animal} is not in the zoo.")

    def get_animals(self):
        return self.animals

    def describe(self):
        print(f"Welcome to {self.name} located in {self.location}!")
        print("Our zoo has the following animals:")
        all_animals = {}
        for animal in self.animals:
            print("- " + animal)
            if animal in all_animals.keys():
                all_animals[animal] = all_animals[animal] + 1
            else:
                all_animals[animal]



# Creating instances and using the class methods
my_zoo = Zoo("Kölner Zoo", "Köln")
my_zoo.describe()

my_zoo.add_animal("Lion")
my_zoo.add_animal("Tiger")
my_zoo.add_animal("Elephant")
my_zoo.add_animal("Giraffe")

print("Animals in the zoo:", my_zoo.get_animals())

my_zoo.remove_animal("Tiger")
my_zoo.remove_animal("Bear")  # Not in the zoo

print("Updated list of animals:", my_zoo.get_animals())
