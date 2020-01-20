import numpy as np
from typing import Mapping, List, Union


def skill_to_bonus(skill_value) -> int:

    bonus = (skill_value // 2) - 5

    return bonus


def skill_init() -> int:
    rolls: Union = np.random.randint(1, 7, 5)
    rolls.sort()
    skill_score = rolls[2:].sum()
    return int(skill_score)
