from unittest import TestCase, main
from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTests(TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware("SSD", "Heavy", 500, 500)

    def test_init_attrs_are_set(self):
        self.assertEqual("SSD", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(500, self.hardware.capacity)
        self.assertEqual(500, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware__no_memory_when_software_is_installed__expect_exception(self):
        software = Software("Win10", "Light", 501, 501)
        with self.assertRaises(Exception) as context:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_equal_capacity_and_memory_when_software_is_installed(self):
        software = Software("Win10", "Light", 500, 500)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_hardware_uninstall__expect_software_to_be_removed_from_software_components(self):
        software = Software("Win10", "Light", 500, 500)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)


if __name__ == "__main__":
    main()
