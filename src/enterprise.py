class Enterprise:
    def __init__(self):
        self.power_level = 5000
        self.population_cap = 30
        self.health_cap = 100
        self.health = 100
        self.crew_number = 0

    def __repr__(self):
        repr_string = "Starship Enterprise. {} crew, Power at {}, at {} health".format(
            self.crew_number, self.power_level, self.health
        )
        return repr_string

    def __str__(self):
        print_string = """Space, the final frontier. These are the voyages of the Starship Enterprise. Its continuing mission: To explore strange new worlds, to seek out new life and new civilizations, to boldly go where no one has gone before."""
        return print_string
