import unittest
from items import *


class TestItems(unittest.TestCase):
    def setUp(self):
        self.helmet = Helmet("Leather helmet", 3200, 8)
        self.weapon = Weapon("Short sword", 1050, 12)


class TestInit(TestItems):
    def test_name(self):
        self.assertEqual(self.helmet.name, "Leather helmet")
        self.assertEqual(self.weapon.name, "Short sword")
        self.assertNotEqual(self.helmet.name, self.weapon.name)

    def test_worth(self):
        self.assertEqual(self.helmet.worth, 3200)
        self.assertEqual(self.weapon.worth, 1050)
        self.assertGreater(self.helmet.worth, self.weapon.worth)

    def test_item_type(self):
        self.assertEqual(self.helmet.item_type, "Helmet")
        self.assertEqual(self.weapon.item_type, "Weapon")

    def test_item_value(self):
        self.assertEqual(self.helmet.item_value, 8)
        self.assertEqual(self.weapon.item_value, 12)
        self.assertLess(self.helmet.item_value, self.weapon.item_value)


class TestRepr(TestItems):
    def test_output(self):
        self.assertEqual(self.helmet.name, repr(self.helmet))
        self.assertEqual(self.weapon.name, repr(self.weapon))


class TestDisplay(TestItems):
    def test_display(self):
        self.helmet.display()


if __name__ == '__main__':
    unittest.main()
