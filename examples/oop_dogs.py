class Dog:

    def __init__(self, name, breed="Unknown"):
        self.number_of_legs = 4
        self.chases_sticks = True
        self.breed = breed
        self.name = name
        self.has_fur = True
        self.size = "Unknown"

    def barks(self):
        print("{} says 'WOOF!".format(self.name))


class YorkshireTerrier(Dog):

    def __init__(self, name):
        super().__init__(name=name, breed="Yorkshire Terrier")
        self.chases_rats = True
        self.has_fur = False
        self.size = "Small"


class Greyhound(Dog):

    def __init__(self, name):
        super().__init__(name=name, breed="Greyhound")
        self.chases_rabbits = True
        self.size = "Medium"