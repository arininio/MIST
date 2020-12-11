import Maze_generator

class Robot:
    """This class will contain all the available functions our robot is capable of"""

    wall_values = {'N': 0b1000, 'E': 0b0100, 'S': 0b0010, 'W': 0b0001}
    LR_values   = {'N': ('W', 'E'), 'E': ('N', 'S'), 'S': ('E', 'W'), 'W': ('S', 'N')}

    def __init__(self, init_x, init_y, maze):
        """initialize robot with a, beginning position (x,y) in maze and make it start pointing south"""
        self.x = init_x
        self.y = init_y
        self.maze = maze
        self.forward = 'S'
        self.changed_dir = False

    def can_go_left(self):
        """returns true if robot can go left, returns false if there's a wall"""
        x, y = self.x, self.y
        left_dir = Robot.LR_values[self.forward][0]
        return self.maze.cell_at(x,y).missing_wall(left_dir)

    def can_go_right(self):
        """returns true if robot can go right, returns false if there's a wall"""
        x, y = self.x, self.y
        right_dir = Robot.LR_values[self.forward][1]
        return self.maze.cell_at(x, y).missing_wall(right_dir)

    def can_go_forward(self):
        """returns true if robot can go forward, returns false if there is a wall"""
        x, y = self.x, self.y
        return self.maze.cell_at(x, y).missing_wall(self.forward)

    def move_forward(self):
        """moves robot forward one pace, taking into account which direction it's facing"""
        if self.can_go_forward():
            if self.forward == 'N':
                self.y = self.y - 1
            elif self.forward == 'S':
                self.y = self.y + 1
            elif self.forward == 'E':
                self.x = self.x + 1
            else:
                self.x = self.x - 1
            self.changed_dir = False
    def turn_left(self):
        """rotates front of robot 90 degrees to the left"""
        current_facing = self.forward
        self.forward = Robot.LR_values[current_facing][0]
        self.changed_dir = True

    def turn_right(self):
        """rotates front of robot 90 degrees to the right"""
        current_facing = self.forward
        self.forward = Robot.LR_values[current_facing][1]
        self.changed_dir = True