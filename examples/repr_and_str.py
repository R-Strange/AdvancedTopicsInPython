class MyCar:
    def __init__(self, mileage, colour):
        self.mileage = mileage
        self.colour = colour

    def __str__(self):
        return "a {} car".format(self.colour)

    def __repr__(self):
        return "car: Mileage {}, Colour {}".format(self.mileage, self.colour)
