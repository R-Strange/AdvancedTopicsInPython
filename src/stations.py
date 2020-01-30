from typing import List


class Station:
    def __init__(self, station_name):
        self.station_name: str = station_name
        self.baseline_score = 30
        self.section_cap: int = 6
        self.staff_list: List = list()
        self.staff_bonuses: List = list()
        self.current_score: int = 30

    def calculate_sum_score(self) -> None:
        self.current_score = self.baseline_score + sum(self.staff_bonuses)

    def __repr__(self):
        self.calculate_sum_score()
        return "{} (Score: {}) {} of {} positions filled.".format(
            self.station_name,
            self.current_score,
            len(self.staff_list),
            self.section_cap,
        )

    def __str__(self):
        "{} station".format(self.station_name)


class Engineering(Station):
    def __init__(self):
        super().__init__(station_name="Engineering")

    def retrieve_bonuses(self) -> None:
        bonuses_list = list()
        for crewman in self.staff_list:
            bonuses_list.append(crewman.engineering_bonus)

        self.staff_bonuses = bonuses_list


class Medical(Station):
    def __init__(self):
        super().__init__(station_name="Medical")

    def retrieve_bonuses(self) -> None:
        bonuses_list = list()
        for crewman in self.staff_list:
            bonuses_list.append(crewman.medical_bonus)

        self.staff_bonuses = bonuses_list


class WeaponsSystems(Station):
    def __init__(self):
        super().__init__(station_name="Weapons Systems")

    def retrieve_bonuses(self) -> None:
        bonuses_list = list()
        for crewman in self.staff_list:
            bonuses_list.append(crewman.weapons_systems_bonus)

        self.staff_bonuses = bonuses_list


class Science(Station):
    def __init__(self):
        super().__init__(station_name="Science")

    def retrieve_bonuses(self) -> None:
        bonuses_list = list()
        for crewman in self.staff_list:
            bonuses_list.append(crewman.science_bonus)

        self.staff_bonuses = bonuses_list


class Command(Station):
    def __init__(self):
        super().__init__(station_name="Command")

    def retrieve_bonuses(self) -> None:
        bonuses_list = list()
        for crewman in self.staff_list:
            bonuses_list.append(crewman.command_bonus)

        self.staff_bonuses = bonuses_list
