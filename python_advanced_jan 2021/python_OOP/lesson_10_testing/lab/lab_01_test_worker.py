class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')

import unittest


class WorkerTests(unittest.TestCase):
    name = "Test Worker"
    salary = 1000
    energy = 3

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    # Test if the worker is initialized with correct name, salary and energy
    def test_worker_init_when_correct_args__expect_to_be_initialized(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    # Test if the worker`s energy is incremented after the rest method is called
    def test_worker__rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    # Test if an error is raised if the worker tries to work with negative energy or equal to 0
    def test_worker_work__when_energy_is_zero_expect_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    # Test if the worker's money is increased by his salary correctly after the work method is called
    def test_worker_work__when_energy_is_above_zero_expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.salary *2, self.worker.money)

    # Test if the worker's money is increased by his salary correctly after the work method is called
    def test_worker_work__when_energy_is_above_0_expect_energy_to_be_decremented(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    # Test if the get_info method returns the proper string with correct values
    def test_worker__get_info_expect_correct_values(self):
        actual_msg = self.worker.get_info()
        expected_msg = f'{self.name} has saved 0 money.'
        self.assertEqual(actual_msg, expected_msg)

if __name__ == '__main__':
    unittest.main()
