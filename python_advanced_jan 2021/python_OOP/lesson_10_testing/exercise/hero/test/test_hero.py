import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("TestName", 3, 100, 3)
        self.enemy = Hero("Enemy", 3, 100, 3)

    def test_check_attrs_are_set(self):
        self.assertEqual("TestName", self.hero.username)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(3, self.hero.damage)

# before_battle_tests
    def test_hero_enemy_name__when_enemy_name_is_same_as_hero_name_expect_exception(self):
        enemy = Hero("TestName", 99, 100, 999)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy)
        expected = "You cannot fight yourself"
        self.assertEqual(expected, str(context.exception))

    def test_hero_health_in_battle__if_zero__expect_ValueError(self):
        enemy = Hero("Enemy", 99, 100, 999)
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy)
        expected = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected, str(context.exception))

    def test_hero_health_in_battle__if_below__expect_ValueError(self):
        enemy = Hero("Enemy", 99, 100, 999)
        self.hero.health = -1
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy)
        expected = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected, str(context.exception))

    def test_hero_enemy_health_in_battle__if_zero__expect_ValueError(self):
        enemy = Hero("Enemy", 99, 0, 999)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy)
        expected = f"You cannot fight Enemy. He needs to rest"
        self.assertEqual(expected, str(context.exception))

    def test_hero_enemy_health_in_battle__if_below__expect_ValueError(self):
        enemy = Hero("Enemy", 99, -1, 999)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy)
        expected = f"You cannot fight Enemy. He needs to rest"
        self.assertEqual(expected, str(context.exception))



### damage_calculation_tests

    # def test_hero_inflicting_damage_upon_enemy(self):
    #     enemy = Hero("Enemy", 99, 100, 999)
    #     self.hero.battle(enemy)
    #     expected_damage = 9
    #     actual = self.hero.damage * self.hero.level
    #     self.assertEqual(expected_damage, actual)
    #
    # def test_hero_enemy_inflicting_damage_upon_hero(self):
    #     enemy = Hero("Enemy", 3, 100, 3)
    #     self.hero.battle(enemy)
    #     expected_damage = 32
    #     actual = enemy.damage * enemy.level
    #     self.assertEqual(expected_damage, actual)

## damage_inflict_tests

    def test_hero_own_health_under_enemy_damage(self):
        enemy = Hero("Enemy", 3, 100, 3)
        self.hero.battle(enemy)
        expected_health = 91
        self.assertEqual(expected_health, self.hero.health)

    def test_hero_enemy_health_under_hero_damage(self):
        enemy = Hero("Enemy", 2, 100, 2)
        self.hero.battle(enemy)
        expected = 96
        actual = enemy.health
        self.assertEqual(expected, actual)


## draw_tests
    def test_hero_health__when_hero_health_goes_below_zero_after_battle__return_msg(self):
        enemy = Hero("Enemy", 2, 2, 2)
        self.hero.health = 2
        expected_msg = "Draw"
        actual_msg = f"{self.hero.battle(enemy)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_hero_health__when_hero_health_goes_to_zero_after_battle__return_msg(self):
        enemy = Hero("Enemy", 2, 9, 2)
        self.hero.health = 4
        expected_msg = "Draw"
        actual_msg = f"{self.hero.battle(enemy)}"
        self.assertEqual(expected_msg, actual_msg)


##main_hero_win_tests
    def test_hero_battle__when_enemy_health_drop_below_zero_after_battle__return_msg(self):
        enemy = Hero("Enemy", 2, 2, 2)
        expected_msg = "You win"
        actual_msg = f"{self.hero.battle(enemy)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_hero_battle__when_enemy_health_drop_to_zero_after_battle__return_msg(self):
        enemy = Hero("Enemy", 2, 9, 2)
        expected_msg = "You win"
        actual_msg = f"{self.hero.battle(enemy)}"
        self.assertEqual(expected_msg, actual_msg)

###enemy_hero_win_tests
    def test_hero_battle__when_hero_health_drop_below_zero_after_battle__return_msg(self):
        enemy = Hero("Enemy", 2, 100, 2)
        self.hero.health = 1
        expected_msg = "You lose"
        actual_msg = f"{self.hero.battle(enemy)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_hero_battle__when_hero_health_drop_to_zero_after_battle__return_msg(self):
        enemy = Hero("Enemy", 2, 100, 2)
        self.hero.health = 4
        expected_msg = "You lose"
        actual_msg = f"{self.hero.battle(enemy)}"
        self.assertEqual(expected_msg, actual_msg)

# test_repr
    def test_hero_str_representation(self):
        expected_msg = f"Hero TestName: 3 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 3\n"
        actual_msg = f"{self.hero.__str__()}"
        self.assertEqual(expected_msg, actual_msg)


if __name__ == "__main__":
    unittest.main()












