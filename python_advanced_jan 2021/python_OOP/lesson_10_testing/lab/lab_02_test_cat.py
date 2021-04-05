class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class TestCat(unittest.TestCase):
    name = "PussyCat"

    def setUp(self) -> None:
        self.cat = Cat(self.name)

    def test_cat_eat_expect_cat_size_increase_by_1(self):
        """Cat's size is increased after eating"""
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_fed_set_to_true_after_eat(self):
        """Cat is fed after eating"""
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_sleep__when_fed_expect_not_to_be_sleepy(self):
        """Cat is not sleepy after sleeping"""
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_cat_eat_when_fed_expect_exception(self):
        """Cat cannot eat if already fed, raises an error"""
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep_when_not_fed_expect_exception(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        self.cat.fed = False
        with self.assertRaises(Exception):
            self.cat.sleep()


if __name__ == '__main__':
    unittest.main()


