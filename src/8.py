import random
class Pet:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

pets = []
# Add pet objects to the list
pets.append(Pet("Fido"))
pets.append(Pet("Mittens"))
pets.append(Pet("Buddy"))

# Print out the name of each pet in the list
for pet in pets:
    print(pet.get_name())