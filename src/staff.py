from src.utils import skill_init, skill_to_bonus


class Staff:
    def __init__(self, name: str):
        self.name: str = name

        self.engineering_skill: int = skill_init()
        self.medical_skill: int = skill_init()
        self.weapons_systems_skill: int = skill_init()
        self.science_skill: int = skill_init()
        self.command_skill: int = skill_init()

        self.engineering_bonus: int = skill_to_bonus(self.engineering_skill)
        self.medical_bonus: int = skill_to_bonus(self.medical_skill)
        self.weapons_systems_bonus: int = skill_to_bonus(self.weapons_systems_skill)
        self.science_bonus: int = skill_to_bonus(self.science_skill)
        self.command_bonus: int = skill_to_bonus(self.command_skill)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{}. Bonuses: Eng {}, Med {}, Wep {}, Sci {}, Com {}".format(
            self.name,
            self.engineering_bonus,
            self.medical_bonus,
            self.weapons_systems_bonus,
            self.science_bonus,
            self.command_bonus,
        )
