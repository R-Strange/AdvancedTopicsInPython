import unittest

from src.stations import Station


class TestStation(unittest.TestCase):
    def setUp(self) -> None:
        self.station_instance = Station("Example Station")

    def test_baseline_score(self):
        self.assertEqual(30, self.station_instance.baseline_score)


if __name__ == '__main__':
    unittest.main()
