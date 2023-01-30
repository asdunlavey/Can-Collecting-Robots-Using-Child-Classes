from robot import Robot


class Manualbot(Robot):
    def __init__(self, score):
        super().__init__(score)
    
    def move_manually(self):
        while True:
            choice = input()
            if choice == 'w': self.move_north()
            elif choice == 'd': self.move_east()
            elif choice == 's': self.move_south()
            elif choice == 'a': self.move_west() 
            elif choice == 'exit': break
            self.display_grid()
        print(self.score)
