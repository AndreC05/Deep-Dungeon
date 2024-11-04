import unittest
from monsters import *
from create_items import *
from player_character import *

all_items()
item_list = [all_items.sword1, all_items.sword2, all_items.sword3, all_items.sword4, all_items.sword5,
             all_items.sword6, all_items.sword7, all_items.sword8, all_items.shield1, all_items.shield2,
             all_items.shield3, all_items.shield4, all_items.shield5, all_items.helmet1, all_items.helmet2,
             all_items.helmet3, all_items.helmet4, all_items.armour1, all_items.armour2, all_items.armour3,
             all_items.armour4, all_items.legarmour1, all_items.legarmour2, all_items.legarmour3,
             all_items.legarmour4]


class TestMonsters(unittest.TestCase):
    def setUp(self):
        weapon1 = item_list[2]
        armour1 = item_list[20]
        self.monster1 = Spider("monster1", "m", 1)
        self.monster2 = Goblin("monster2", "f", 3, None, None, weapon1, armour1, None)
        self.character1 = PlayerCharacter("name1", 34, "m", "elf", 196, 67, "grey")


class TestInit(TestMonsters):
    def test_name(self):
        self.assertEqual(self.monster1.name, "monster1")
        self.assertEqual(self.monster2.name, "monster2")

    def test_gender(self):
        self.assertEqual(self.monster1.gender, "m")
        self.assertEqual(self.monster2.gender, "f")

    def test_level(self):
        self.assertEqual(self.monster1.level, 1)
        self.assertLess(self.monster1.level, self.monster2.level)

    def test_species(self):
        self.assertEqual(self.monster1.species, "Spider")
        self.assertEqual(self.monster2.species, "Goblin")

    def test_stats(self):
        self.assertLess(self.monster1.max_hp, self.monster2.max_hp)
        self.assertLess(self.monster1.strength, self.monster2.strength)
        self.assertLess(self.monster1.defence, self.monster2.defence)
        self.assertLess(self.monster1.points_worth, self.monster2.points_worth)
        self.assertLess(self.monster1.exp_worth, self.monster2.exp_worth)
        self.assertLess(self.monster1.gold_worth, self.monster2.gold_worth)


class TestMonsterActions(TestMonsters):
    def test_monster_death(self):
        self.assertTrue(self.monster1.alive)
        self.monster1.monster_death()
        self.assertFalse(self.monster1.alive)

    def test_drop_equipment(self):
        weapon1 = item_list[2]
        armour1 = item_list[20]
        self.assertListEqual(self.monster2.drop_equipment(), [None, None, weapon1, armour1, None])

    def test_monster_attack(self):
        self.monster1.monster_attack(self.character1)
        self.assertLess(self.character1.current_hp, self.character1.max_hp)

    def test_monster_display(self):
        self.monster1.monster_display()
        self.monster2.monster_display()


if __name__ == '__main__':
    unittest.main()
