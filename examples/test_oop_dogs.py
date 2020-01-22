import unittest
import contextlib
import io
from examples.oop_dogs import YorkshireTerrier


class TestYorkshireTerrier(unittest.TestCase):

    def setUp(self):
        self.yorkie_instance = YorkshireTerrier("test_yorkie")

    def test_has_fur(self):
        self.assertFalse(self.yorkie_instance.has_fur)

    def test_barks(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.yorkie_instance.barks()

        bark_output = f.getvalue()

        self.assertEqual(bark_output, "test_yorkie says 'WOOF!'\n")


if __name__ == '__main__':
    unittest.main()
