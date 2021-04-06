class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value



    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

import unittest


class TestCar(unittest.TestCase):
    make = "make"
    model = "model"
    fuel_consumption = 10
    fuel_capacity = 100

    def setUp(self) -> None:
        self.car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_car_make__when_value_is_not_None_expect_to_change_make(self):
        self.make = "test"
        self.assertEqual(self.make, "test")

    def test_car_make_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = None
        expected = "Make cannot be null or empty!"
        self.assertEqual(expected, str(context.exception))

    def test_car_model__when_value_is_not_None_expect_to_change_model(self):
        self.model = "test"
        self.assertEqual("test", self.model)

    def test_car_model_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model = None
        expected = "Model cannot be null or empty!"
        self.assertEqual(expected, str(context.exception))

    def test_car_fuel_consumption__when_value_is_not_None_expect_to_change_model(self):
        self.fuel_consumption = 10
        self.assertEqual(10, self.fuel_consumption)

    def test_car_fuel_consumption_setter__when_zero_or_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = 0
        expected = "Fuel consumption cannot be zero or negative!"
        self.assertEqual(expected, str(context.exception))

    def test_car_fuel_capacity__when_value_is_not_None_expect_to_change_model(self):
        self.fuel_capacity = 100
        self.assertEqual(100, self.fuel_capacity)

    def test_car_fuel_capacity_setter__when_zero_or_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = 0
        expected = "Fuel capacity cannot be zero or negative!"
        self.assertEqual(expected, str(context.exception))

    def test_car_fuel_amount__when_value_is_not_None_expect_to_change_model(self):
        self.car.fuel_amount = 0
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_fuel_amount_setter__when_negative__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        expected = "Fuel amount cannot be negative!"
        self.assertEqual(expected, str(context.exception))

    def test_car_refuel__when_provided_fuel_is_zero__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.refuel(0)
        expected = "Fuel amount cannot be zero or negative!"
        self.assertEqual(expected, str(context.exception))

    def test_car_refuel__when_provided_fuel_is_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.refuel(-1)
        expected = "Fuel amount cannot be zero or negative!"
        self.assertEqual(expected, str(context.exception))

    def test_car_refuel__when_provided_fuel_is_correct__expect_to_increase_fuel_amount_by_given_value(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.refuel(fuel)
        self.assertEqual(fuel, car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_more_than_capacity__expect_to_increase_amount_to_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.fuel_capacity = 60
        car.fuel_amount = 40
        car.refuel(fuel)
        self.assertEqual(car.fuel_capacity, car.fuel_amount)

        # car.refuel(self.fuel_capacity*2)
        # self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_car_drive__when_fuel_amount_is_enough_to_cover_distance(self):
        self.car.fuel_amount = 10
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_drive__when_fuel_amount_is_not_enough_to_cover_distance(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.car.fuel_amount = 1
        with self.assertRaises(Exception) as context:
            car.drive(200)
        expected = "You don't have enough fuel to drive!"
        self.assertEqual(expected, str(context.exception))

if __name__ == '__main__':
    unittest.main()