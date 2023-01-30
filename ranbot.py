from robot import Robot
from time import sleep
from random import randint


class Ranbot(Robot):
    def __init__(self, score):
        super().__init__(score)

    def move_random(self, number_of_actions = 10, move_cooldown = 0.5):
        for remaining_moves in range(number_of_actions, 0, -1):
            choice = randint(0, 3)
            if choice == 0: self.move_north()
            elif choice == 1: self.move_east()
            elif choice == 2: self.move_south()
            elif choice == 3: self.move_west()
            print(f'{remaining_moves} actions remaining.')
            self.display_grid()
            sleep(move_cooldown)
        print(self.score)
