import unittest

from src.stations import *


class TestStation(unittest.TestCase):
    def setUp(self) -> None:
        self.station_instance = Station("Example Station")

    def test_baseline_score(self):
        self.assertEqual(30, self.station_instance.baseline_score)

    def test_init_staff_cap(self):
        self.assertEqual(6, self.station_instance.section_cap)

    def test_init_staff_list(self):
        self.assertSequenceEqual(self.station_instance.staff_list, list())

    def test_init_staff_bonuses(self):
        self.assertSequenceEqual(self.station_instance.staff_bonuses, list())

    def test_init_current_bonus(self):
        self.assertEqual(self.station_instance.current_score, 30)

    def test_sum_bonuses(self):
        self.station_instance.staff_bonuses = [0, 0, 1, 3, 6, 6]
        self.station_instance.calculate_sum_score()
        self.assertEqual(46, self.station_instance.current_score)


class TestEngineering(unittest.TestCase):
    def setUp(self) -> None:
        self.engineering_instance = Engineering()

    def test_baseline_exists(self):
        self.assertEqual(30, self.engineering_instance.baseline_score)


class TestMedical(unittest.TestCase):
    def setUp(self) -> None:
        self.medical_instance = Medical()

    def test_baseline_exists(self):
        self.assertEqual(30, self.medical_instance.baseline_score)


class TestWeaponsSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.weapons_systems_instance = WeaponsSystems()

    def test_baseline_exists(self):
        self.assertEqual(30, self.weapons_systems_instance.baseline_score)


class TestScience(unittest.TestCase):
    def setUp(self) -> None:
        self.science_instance = Science()

    def test_baseline_exists(self):
        self.assertEqual(30, self.science_instance.baseline_score)


class TestCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.command_instance = Command()

    def test_baseline_exists(self):
        self.assertEqual(30, self.command_instance.baseline_score)


if __name__ == '__main__':
    unittest.main()
