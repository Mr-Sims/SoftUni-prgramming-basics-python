from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    name = "TestTrain"
    capacity = 10

    def setUp(self) -> None:
        self.train = Train(self.name, self.capacity)

    def test__init__when_all_valid__expect_be_set(self):
        self.assertEqual(self.name, self.train.name)
        self.assertEqual(self.capacity, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_train_add__when_passenger_added__expect_to_set(self):
        passenger = "Pesho"
        self.train.add(passenger)
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual("Added passenger Pesho",  self.train.PASSENGER_ADD.format(passenger))

    def test_train_add__when_passenger_added_if_not_enough_capacity__expect_ValueError(self):
        train = Train("Test", 1)
        passenger = "Pesho"
        passenger2 = "Peter"
        with self.assertRaises(ValueError) as context:
            train.add(passenger)
            train.add(passenger2)

        self.assertEqual("Train is full", str(context.exception))

    def test_train_add__when_passenger_already_added__expect_ValueError(self):
        train = Train("Test", 10)
        passenger = "Pesho"

        with self.assertRaises(ValueError) as context:
            train.add(passenger)
            train.add(passenger)
        self.assertEqual("Passenger Pesho Exists", str(context.exception))

    def test_remove__when_passenger_not_on_train__expect_ValueError(self):
        train = Train("Test", 10)
        passenger = "Pesho"
        with self.assertRaises(ValueError) as context:
            train.remove(passenger)
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_remove__when_passenger_on_train_expect_to_be_removed(self):
        train = Train("Test", 10)
        passenger = "Pesho"
        train.add(passenger)
        self.assertEqual("Removed Pesho", train.remove(passenger))
        # train.remove(passenger)

if __name__ == "__main__":
    main()