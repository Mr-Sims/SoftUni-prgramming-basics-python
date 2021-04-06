import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    fuel = 10
    horse_power = 100

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    #opional test 1
    def test_vehicle_init__expect_fuel_consumption_to_be_equal_to_default_fuel_consumption(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    #optional test 2
    def test_vehicle_init__expect_capacity_to_be_equal_to_fuel(self):
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)

    def test_vehicle_drive__when_fuel_capacity_is_enough(self):
        self.vehicle.drive(8)
        self.assertEqual(0, self.vehicle.fuel)

    def test_vehicle_drive__when_fuel_capacity_is_not_enough__expect_exception(self):
        vehicle = Vehicle(self.fuel, self.horse_power)
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(10)
        expected = "Not enough fuel"
        self.assertEqual(expected, str(context.exception))

    def test_vehicle_refuel__when_fuel_too_much__expect_exception(self):
        self.vehicle.fuel = 10
        self.vehicle.capacity = 20
        fuel = 20
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(fuel)
        expected = "Too much fuel"
        self.assertEqual(expected, str(context.exception))

    def test_vehicle_refuel__when_fuel_value_is_correct(self):
        self.vehicle.fuel = 10
        self.vehicle.capacity = 20
        fuel = 9
        self.vehicle.refuel(fuel)
        expected = 19
        actual = self.vehicle.fuel
        self.assertEqual(expected, actual)

    def test_vehicle_str_method(self):
        result = self.vehicle.__str__()
        expected = f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()



