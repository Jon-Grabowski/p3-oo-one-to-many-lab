import ipdb

class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
        # Owner.add_pet(self)

    def get_pet_type(self):
        return self._pet_type
    
    def set_pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception('Not a valid pet type.')

    pet_type = property(get_pet_type, set_pet_type)

class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, new_pet):
        new_pet.owner = self

    def get_sorted_pets(self):
        pets = self.pets()
        return sorted(pets, key=lambda pet: pet.name)

# owner1 = Owner("Jon")
# pet1 = Pet("Potato", "cat", owner1)
# pet2 = Pet("Basil", "cat", owner1)
# pet3 = Pet("Olive", "dog")

# ipdb.set_trace()