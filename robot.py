from random import randint


class Robot:
    def __init__(self, grid):
        self.row = 0
        self.column = 1
        self.grid = grid

    def display_grid(self):
        for row in range(10):
            print(self.grid[row])
            
    
    def move_random(self):
        choice = randint(3)
        if choice == 0: self.move_north()
        if choice == 1: self.move_east()
        if choice == 2: self.move_south()
        if choice == 3: self.move_west()

    def pickup_can(self):
        pass

    def move_north(self):
        if self.column == 0:
            input('bump')
            return
            
        self.grid[self.row - 1][self.column] = self.grid[self.row][self.column]
        self.column -= 1

    def move_east(self):
        pass

    def move_south(self):
        pass

    def move_west(self):
        pass
