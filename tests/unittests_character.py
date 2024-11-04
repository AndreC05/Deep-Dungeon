import unittest
from player_character import *
from map import *

all_items()
item_list = [all_items.sword1, all_items.sword2, all_items.sword3, all_items.sword4, all_items.sword5,
             all_items.sword6, all_items.sword7, all_items.sword8, all_items.shield1, all_items.shield2,
             all_items.shield3, all_items.shield4, all_items.shield5, all_items.helmet1, all_items.helmet2,
             all_items.helmet3, all_items.helmet4, all_items.armour1, all_items.armour2, all_items.armour3,
             all_items.armour4, all_items.legarmour1, all_items.legarmour2, all_items.legarmour3,
             all_items.legarmour4]


class TestPlayerCharacter(unittest.TestCase):
    def setUp(self):
        self.character1 = PlayerCharacter("name1", 34, "m", "elf", 196, 67, "grey")
        self.character2 = PlayerCharacter("name2", 44, "f", "human", 155, 57, "black")


class TestInit(TestPlayerCharacter):
    def test_name(self):
        self.assertEqual(self.character1.name, "name1")
        self.assertEqual(self.character2.name, "name2")
        self.assertNotEqual(self.character1.name, self.character2.name)

    def test_age(self):
        self.assertEqual(self.character1.age, 34)
        self.assertEqual(self.character2.age, 44)
        self.assertLess(self.character1.age, self.character2.age)

    def test_gender(self):
        self.assertEqual(self.character1.gender, "m")
        self.assertEqual(self.character2.gender, "f")
        self.assertNotEqual(self.character1.gender, self.character2.gender)

    def test_species(self):
        self.assertEqual(self.character1.species, "elf")
        self.assertEqual(self.character2.species, "human")
        self.assertNotEqual(self.character1.species, self.character2.species)

    def test_height(self):
        self.assertEqual(self.character1.height, 196)
        self.assertEqual(self.character2.height, 155)
        self.assertGreater(self.character1.height, self.character2.height)

    def test_weight(self):
        self.assertEqual(self.character1.weight, 67)
        self.assertEqual(self.character2.weight, 57)
        self.assertGreater(self.character1.weight, self.character2.weight)

    def test_hair_colour(self):
        self.assertEqual(self.character1.hair_colour, "grey")
        self.assertEqual(self.character2.hair_colour, "black")
        self.assertNotEqual(self.character1.hair_colour, self.character2.hair_colour)

    def test_level(self):
        self.assertEqual(self.character1.level, 1)
        self.assertEqual(self.character2.level, 1)
        self.assertEqual(self.character1.level, self.character2.level)

    def test_initial_exp_gold_points(self):
        self.assertEqual(self.character1.current_exp, 0)
        self.assertEqual(self.character1.current_exp, self.character2.current_exp)
        self.assertEqual(self.character1.current_exp, self.character1.gold, self.character1.points)
        self.assertEqual(self.character2.current_exp, self.character2.gold, self.character2.points)

    def test_initial_location(self):
        self.assertEqual(self.character1.location, "town")
        self.assertEqual(self.character1.location, self.character2.location)

        self.assertEqual(self.character1.x, 0)
        self.assertEqual(self.character1.y, 0)
        self.assertEqual(self.character1.x, self.character2.x)
        self.assertEqual(self.character1.y, self.character2.y)

    def test_inventory(self):
        self.assertListEqual(self.character1.inventory, [])
        self.assertListEqual(self.character2.inventory, [])


class TestChangeEquipment(TestPlayerCharacter):
    def test_pickup_equipment(self):
        weapon = item_list[1]
        self.character1.pickup_item(weapon)

        self.assertListEqual(self.character1.inventory, [weapon])

    def test_change_equipment(self):
        weapon = item_list[1]
        helmet = item_list[14]
        self.character1.pickup_item(weapon)
        self.character1.change_equipment(weapon, "right hand")
        self.assertEqual(self.character1.R_hand.name, weapon.name)

        self.character1.pickup_item(helmet)
        self.character1.change_equipment(helmet, "right hand")
        self.assertNotEqual(self.character1.R_hand.name, helmet.name)


class TestLevelUp(TestPlayerCharacter):
    def test_level_up(self):
        self.character1.level_up(1000)
        self.assertEqual(self.character1.level, 2)
        self.assertEqual(self.character1.current_exp, 0)
        self.assertEqual(self.character1.max_exp, 1500)
        self.assertEqual(self.character1.max_hp, 75)
        self.assertEqual(self.character1.current_hp, 75)
        self.assertEqual(self.character1.strength, 14)
        self.assertEqual(self.character1.defence, 14)


class TestDungeon(TestPlayerCharacter):
    def test_enter_dungeon(self):
        self.character1.enter_dungeon()
        self.assertEqual(self.character1.location, "dungeon")

    def test_player_attack(self):
        monster = Spider("monster1", "m", 1)
        self.character1.player_attack(monster)
        self.assertLess(monster.current_hp, monster.max_hp)
        self.character1.player_attack(monster)
        self.character1.player_attack(monster)
        self.character1.player_attack(monster)
        self.character1.player_attack(monster)
        self.assertFalse(monster.alive)

    def test_battle(self):
        monster2 = Spider("monster2", "m", 1)
        self.character1.battle(monster2)
        self.assertLess(monster2.current_hp, monster2.max_hp)
        self.assertLess(self.character1.current_hp, self.character1.max_hp)
        self.assertTrue(monster2.alive)

    def test_movement(self):
        f_map = Map()
        self.character1.move_up(f_map)
        self.assertEqual(self.character1.y, 1)
        self.character1.move_down(f_map)
        self.assertEqual(self.character1.y, 0)
        self.character1.move_left(f_map)
        self.assertEqual(self.character1.x, 1)
        self.character1.move_right(f_map)
        self.assertEqual(self.character1.x, 0)

        self.character1.next_floor()

        self.assertEqual(self.character1.floor, 2)



if __name__ == '__main__':
    unittest.main()
