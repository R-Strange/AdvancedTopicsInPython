import unittest

from src.staff import Staff as src_Staff


class TestStaff(unittest.TestCase):

    def setUp(self) -> None:
        self.staff_member = src_Staff("Anon. Y. Mous")

    def test_init_engineering_skill_not_zero(self):
        engineering_skill = self.staff_member.engineering_skill
        self.assertGreater(engineering_skill, 0)
        self.assertLessEqual(engineering_skill, 18)

    def test_init_engineering_skill_is_integer(self):
        engineering_skill = self.staff_member.engineering_skill
        self.assertIsInstance(engineering_skill, int)

    def test_init_medical_skill_not_zero(self):
        medical_skill = self.staff_member.medical_skill
        self.assertGreater(medical_skill, 0)
        self.assertLessEqual(medical_skill, 18)

    def test_init_medical_skill_is_integer(self):
        medical_skill = self.staff_member.medical_skill
        self.assertIsInstance(medical_skill, int)
        
    def test_init_weapons_systems_skill_not_zero(self):
        weapons_systems_skill = self.staff_member.weapons_systems_skill
        self.assertGreater(weapons_systems_skill, 0)
        self.assertLessEqual(weapons_systems_skill, 18)

    def test_init_weapons_systems_skill_is_integer(self):
        weapons_systems_skill = self.staff_member.weapons_systems_skill
        self.assertIsInstance(weapons_systems_skill, int)
        
    def test_init_science_skill_not_zero(self):
        science_skill = self.staff_member.science_skill
        self.assertGreater(science_skill, 0)
        self.assertLessEqual(science_skill, 18)

    def test_init_science_skill_is_integer(self):
        science_skill = self.staff_member.science_skill
        self.assertIsInstance(science_skill, int)
        
    def test_init_command_skill_not_zero(self):
        command_skill = self.staff_member.command_skill
        self.assertGreater(command_skill, 0)
        self.assertLessEqual(command_skill, 18)

    def test_init_command_skill_is_integer(self):
        command_skill = self.staff_member.command_skill
        self.assertIsInstance(command_skill, int)


if __name__ == '__main__':
    unittest.main()
