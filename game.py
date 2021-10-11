"""
==========================================================
GAME WIZARD, WARRIOR, ROBBER
----------------------------------------------------------
the wizard defeats the warrior
the warrior defeats the robber
the robber defeats the wizard

the player's life and level in the settings.py
for each round won, the player receives 5 points

the results are written to scores.txt
=========================================================
"""

import settings
from models import Player
from models import Enemy
from exceptions import EnemyDown
from exceptions import GameOver


def name_input():
    """base  validation for name input"""
    while True:
        name = input('please enter your name').capitalize()
        if name == '':
            print('You entered an empty line')
        elif len(name) < 4:
            print('You entered the name must be at least three characters long')
        else:
            break
    return name


def play(name):
    """WWR game loop"""
    print(
        '\nthe wizard(select 1) defeats the warrior'
        '\nthe warrior(select 2) defeats the robber'
        '\nthe robber (select 3) defeats the wizard'
        '\n'
        '\nfor a successful attack, the enemy loses one life',
        '\nfor defeating the enemy, you get 5 points'
        '\nbut remember, you are death too ...'
        '\n'
    )
    player = Player(name)
    level = 1
    enemy = Enemy(level)
    while True:
        try:
            print(player.attack(enemy))
            print(player.defence(enemy))
        except EnemyDown:
            print("\nEnemy defeated, next enemy!\n")
            level += 1
            enemy = Enemy(level)
            player.score += 5
            print(name, ' Lives - ', player.lives)
            print('Enemy level - ', enemy.get_info(), '\n')
            continue


def process_game(user_name):
    """ main program body"""
    try:
        play(user_name)
    except GameOver:
        print('Game Over')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')


if __name__ == '__main__':
    try:
        user_name = name_input()
        print('Hi, ', user_name, ' thanks for start the program')
        while True:
            print("\nPlease enter the command:"
                  "\nif you don't know how to enter help")
            user_input = input('\nEnter command please')
            if user_input == 'start':
                process_game(user_name)
            elif user_input == 'show scores':
                GameOver.show_scores()
            elif user_input == 'help':
                for i in settings.help_list:
                    print(i)
            elif user_input == 'exit':
                raise ZeroDivisionError
            else:
                print('\nIncorrect enter command, try again')
    except ZeroDivisionError:
        print('\nClose the program')
        print('Thank you, come again please')
