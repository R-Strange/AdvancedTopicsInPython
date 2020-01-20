from src.enterprise import Enterprise


class Station(Enterprise):

    def __init__(self, name):
        self.name: str = name
        self.baseline_score = 30
        super().__init__()