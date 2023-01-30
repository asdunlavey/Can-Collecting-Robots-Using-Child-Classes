from ranbot import Ranbot
from manualbot import Manualbot


def generate_grid():
    arr = [
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
    arr[0][0] = "R"
    return arr


def display_grid(grid):
    for row in range(10):
        print(grid[row])


def main():
    grid = generate_grid()
    robots = [
        ranbot := Ranbot(grid),
        manualbot := Manualbot(grid)
    ]
    # robots[0].move_random()
    # robots[1].move_manually()


if __name__ == "__main__":
    main()
