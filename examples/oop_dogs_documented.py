
class CommentedDog:

    def __init__(self, name, breed="Unknown"):  # take the name from user and set unknown breed
        self.number_of_legs = 4  # a dog has 4 legs
        self.chases_sticks = True  # set the dog to like chasing sticks
        self.breed = breed  # set the breed
        self.name = name  # set the user-supplied name
        self.has_fur = True  # set the dog to have fur
        self.size = "Unknown"  # set the size to be unknown

    def barks(self):
        print("{} says 'WOOF!'".format(self.name))


class CommentedYorkshireTerrier(CommentedDog):

    def __init__(self, name):
        super().__init__(name=name, breed="Yorkshire Terrier")  # need to provide a name to dog superclass
        self.chases_rats = True
        self.has_fur = False  # overwrites superclass attribute
        self.size = "Small"  # overwrites superclass attribute


class CommentedGreyhound(CommentedDog):
    """
    Base class for dogs, with the ability
    """

    def __init__(self, name):
        super().__init__(name=name, breed="Greyhound")
        self.chases_rabbits = True
        self.size = "Medium"


class DocumentedDog:
    """
    the DocumentedDog object holds various breeds of dog.

    Args:
        name (str): The name of the dog
        breed (str): The breed of the dog. Default to "Unknown".

    Attributes:
        number_of_legs (int): The number of legs a dog has.
        chases_sticks (bool): If a dog likes to chase after sticks.
        breed (str): The name of the breed of dog.
        name (str): The name of the breed of dog.
        has_fur (bool): If a dog has fur or not.
        size (str): The qualitative size of the dog.
    """
    def __init__(self, name: str, breed: str = "Unknown"):
        self.number_of_legs: int = 4
        self.chases_sticks: bool = True
        self.breed: str = breed
        self.name: str = name
        self.has_fur: bool = True
        self.size: str = "Unknown"

    def barks(self) -> None:
        """
        We are told that a dog is barking
        Returns:
            None
        """
        print("{} says 'WOOF!'".format(self.name))


class DocumentedYorkshireTerrier(DocumentedDog):
    """
    The Yorkshire terrier breed is a subclass of dog.

    Will auto-set the Dog breed argument with "Yorkshire Terrier"

    Args:
        name (str): the name of the dog

    Attributes:
        chases_rats (bool): If the yorkshire terrier likes to chase rats
        has_fur (bool): If the dog has fur - overwrites parent class as Yorkies have hair
        size (str): Size of the dog - overwrites parent class
    """
    def __init__(self, name):
        super().__init__(name=name, breed="Yorkshire Terrier")
        self.chases_rats = True
        self.has_fur = False
        self.size = "Small"


class DocumentedGreyhound(DocumentedDog):
    """
    The Greyhound breed is a subclass of dog.

    Will auto-set the Dog breed argument with "Greyhound"

    Args:
        name (str): the name of the dog

    Attributes:
        chases_rabbits (bool): If the greyhound likes to chase rabbits
        size (str): Size of the dog - overwrites parent class
    """

    def __init__(self, name):
        super().__init__(name=name, breed="Greyhound")
        self.chases_rabbits = True
        self.size = "Medium"

