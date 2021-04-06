import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    name = "Harambe"
    type = "gorilla"
    sound = "roar"

    def setUp(self) -> None:
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_mammal_private_attribute_kingdom(self):
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        expected = f"{self.name} makes {self.sound}"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_mammal_get_kigdom(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_mammal_info(self):
        expected = f"{self.name} is of type {self.type}"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
