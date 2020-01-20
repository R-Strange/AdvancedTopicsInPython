import unittest

from src.enterprise import Enterprise as src_Enterprise


class TestEnterprise(unittest.TestCase):

    def setUp(self) -> None:
        self.enterprise_instance = src_Enterprise()

    def test_init_power(self):
        expected_power_level = 5000
        actual_power_level = self.enterprise_instance.power_level
        self.assertEqual(expected_power_level, actual_power_level)

    def test_init_population_cap(self):
        expected_population_cap = 30
        actual_population_cap = self.enterprise_instance.population_cap
        self.assertEqual(expected_population_cap, actual_population_cap)

    def test_init_crew(self):
        expected_crew = 0
        actual_crew = self.enterprise_instance.crew_number
        self.assertEqual(expected_crew, actual_crew)

    def test_init_health_cap(self):
        expected_health_cap = 100
        actual_health_cap = self.enterprise_instance.health_cap
        self.assertEqual(expected_health_cap, actual_health_cap)

    def test_init_health(self):
        expected_health = 100
        actual_health = self.enterprise_instance.health
        self.assertEqual(expected_health, actual_health)

    def test_repr(self):
        expected_repr = """Starship Enterprise. 0 crew, Power at 5000, at 100 health"""
        actual_repr = repr(self.enterprise_instance)
        self.assertEqual(expected_repr, actual_repr)

    def test_str(self):
        expected_string = """Space, the final frontier. These are the voyages of the Starship Enterprise. Its continuing mission: To explore strange new worlds, to seek out new life and new civilizations, to boldly go where no one has gone before."""
        actual_string = str(self.enterprise_instance)
        self.assertEqual(expected_string, actual_string)

if __name__ == '__main__':
    unittest.main()
