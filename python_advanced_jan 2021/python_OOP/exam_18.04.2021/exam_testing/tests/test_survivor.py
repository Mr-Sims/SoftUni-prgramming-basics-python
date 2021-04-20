from unittest import TestCase, main

from project.survivor import Survivor

class TestSurvivor(TestCase):
    name = "Test"
    age = 10

    def setUp(self) -> None:
        self.survivor = Survivor(self.name, self.age)

    def test_init__if_all_valid__expect_to_be_set(self):
        self.assertEqual("Test", self.survivor.name)
        self.assertEqual(10, self.survivor.age)
        self.assertEqual(100, self.survivor.health)
        self.assertEqual(100, self.survivor.needs)

    def test_name_property_if_validator_works(self):
        name = ""
        with self.assertRaises(ValueError) as context:
            survivor = Survivor(name, 10)
        self.assertEqual("Name not valid!", str(context.exception))

    def test_age_property_if_validator_works(self):
        age = -1
        with self.assertRaises(ValueError) as context:
            survivor = Survivor("Test", age)
        self.assertEqual("Age not valid!", str(context.exception))

    def test_health_if_validator_works(self):
        with self.assertRaises(ValueError) as context:
            self.survivor.health = -1
        self.assertEqual("Health not valid!", str(context.exception))

    def test_needs__if_validator_works(self):
        with self.assertRaises(ValueError) as context:
            self.survivor.needs = -1
        self.assertEqual("Needs not valid!", str(context.exception))

    def test__needs_sustenance_return_false(self):
        expected = False
        actual = self.survivor.needs_sustenance
        self.assertEqual(expected, actual)

    def test__needs_sustenance_return_true(self):
        self.survivor.needs = 50
        expected = True
        actual = self.survivor.needs_sustenance
        self.assertEqual(expected, actual)

    def test__needs_healing_return_false(self):
        expected = False
        actual = self.survivor.needs_healing
        self.assertEqual(expected, actual)

    def test__needs_healing_return_true(self):
        self.survivor.health = 50
        expected = True
        actual = self.survivor.needs_healing
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()