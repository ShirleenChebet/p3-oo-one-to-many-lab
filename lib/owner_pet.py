class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Initialize an empty list to store the owner's pets

    def pets(self):
        """Returns the list of pets owned by this owner."""
        return self._pets

    def add_pet(self, pet):
        """Associates a Pet instance with this owner."""
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance.")
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a list of this owner's pets sorted by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)
    
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Stores all Pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types are: {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Owner will be set when added to an owner

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            owner.add_pet(self)

        Pet.all.append(self)