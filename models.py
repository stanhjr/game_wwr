"""
Models
=================================================
This module contains class Enemy and class Player

imported here random, settings and exceptions
=================================================
"""

import random
import settings
from exceptions import EnemyDown
from exceptions import GameOver


class Enemy:
    """ The state of the enemy and the technology of returning a random value for the enemy's move"""
    def __init__(self, level):
        self.lives = level

    @staticmethod
    def select_attack() -> int:
        return random.randrange(1, 4)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown

    def get_info(self):
        return self.lives


class Player:
    """player points and lives and round calculation mechanism"""
    def __init__(self, name):
        self.name = name
    score = 0
    lives = settings.lives
    allowed_attack = [1, 2, 3]

    @staticmethod
    def fight(attack, defense) -> int:
        """return the result of the round"""
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or (attack == 3 and defense == 1):
            return 1
        elif (attack == 1 and defense == 3) or (attack == 2 and defense == 1) or (attack == 3 and defense == 2):
            return -1
        else:
            return 0

    @staticmethod
    def input_validation(text_var: str) -> int:
        """validation input for attack"""
        while True:
            num = input(text_var)
            if num == '1':
                return 1
            elif num == '2':
                return 2
            elif num == '3':
                return 3
            else:
                print("input is incorrect")

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.score, self.name)

    def attack(self, enemy_obj):
        attack_player = Player.input_validation('Select attack')
        res = self.fight(attack_player, enemy_obj.select_attack())
        if res == 0:
            return 'Its a draw!'
        elif res == -1:
            return 'You missed!'
        else:
            enemy_obj.decrease_lives()
            return 'You attacked successfully!'

    def defence(self, enemy_obj):
        defence_player = Player.input_validation('Select defence')
        res = self.fight(enemy_obj.select_attack(), defence_player)
        if res == 0:
            return 'Its a draw!'
        elif res == -1:
            return 'He missed!'
        else:
            self.decrease_lives()
            return 'His attack successfully!'


