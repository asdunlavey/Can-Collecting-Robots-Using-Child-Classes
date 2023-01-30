from dunbot import Dunbot
from robot import Robot


def generate_grid():
    return [
        [None] * 10,
        [None] * 10,
        [None] * 10,
        [None] * 10,
        [None] * 10,
        [None] * 10,
        [None] * 10,
        [None] * 10,
        [None] * 10,
        [None] * 10,
    ]


def display_grid(grid):
    for row in range(10):
        print(grid[row])


def main():
    grid = generate_grid()
    grid[1][0] = 'R'

    robot = Robot(grid)
    #robot.display_memory()
    robot.display_grid()
    robot.move_north()
    robot.display_grid()
    robot.move_north()


if __name__ == "__main__":
    main()
