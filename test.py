
import unittest
from unittest.mock import patch
from exceptions import GameOver
from unittest import mock
import exceptions
from game import name_input
from models import Player
from models import Enemy


class TestGame(unittest.TestCase):
    def test_name_input(self):
        with patch('builtins.input', return_value='stan'):
            self.assertEqual(name_input(), 'Stan')


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.new_enemy = Enemy(5)

    def test_select_attack(self):
        change = self.new_enemy.select_attack()
        bool_result = change in (1, 2, 3)
        self.assertTrue(bool_result)

    def test_get_info(self):
        self.assertEqual(self.new_enemy.get_info(), 5)

    def test_decrease_lives(self):
        self.new_enemy.decrease_lives()
        self.assertEqual(self.new_enemy.get_info(), 4)


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player('stan')
        self.enemy_obj = Enemy(5)

    def test_fight(self):
        self.assertEqual(self.player.fight(1, 3), -1)

    def test_input_validation(self):
        for var in range(1, 4):
            user_input = str(var)
            with patch('builtins.input', return_value=user_input):
                self.assertEqual(self.player.input_validation('hi'), var)

    def test_decrease_lives(self):
        self.player.decrease_lives()
        self.assertEqual(self.player.lives, 4)

    def test_decrease_lives_error(self):
        self.player.lives = 1
        self.assertRaises(GameOver, self.player.decrease_lives)

    def test_attack(self):
        ...

    def test_defence(self):
        ...


class TestException(unittest.TestCase):
    ...


if __name__ == '__main__':
    unittest.main()
