class Robot:
    def __init__(self, grid):
        self.score = 0
        self.row = 0
        self.column = 0
        self.grid = grid #grid[row][column]

    def move_to_tile(self, r, c):
        self.grid[self.row + r][self.column + c] = self.grid[self.row][self.column]
        self.grid[self.row][self.column] = None
        self.row += r
        self.column += c
    
    def display_grid(self):
        for row in range(10):
            print(self.grid[row])
        print()

    def pickup_can(self):
        pass
    
    def move_north(self):
        if self.row == 0:
            self.bump_into_wall()
            return 
        self.move_to_tile(-1, 0)

    def move_east(self):
        if self.column == 9:
            self.bump_into_wall()
            return
        self.move_to_tile(0, 1)

    def move_south(self):
        if self.row == 9:
            self.bump_into_wall()
            return
        self.move_to_tile(1, 0)

    def move_west(self):
        if self.column == 0:
            self.bump_into_wall()
            return
        self.move_to_tile(0, -1)

    def bump_into_wall(self):
        #print('Robot bumped into a wall.')
        self.score -= 10
