import robot
import pygame
import Maze_generator
WHITE = (200,200,200)
BLACK = (0, 0, 0)
DISPLAY_SIZE = (600, 600)
LINE_WIDTH = 2


class Frontend:

    def __init__(self, maze, robot, algorithm):
        """intitializes the frontend with a maze, robot, and the algorithm for the robot"""
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.maze = maze
        self.robot = robot
        self.algorithm = algorithm

    def draw_board(self):
        """draws the maze by printing a grid and deleting all the walls necessary"""
        total_cells = self.maze.width * self.maze.height
        cell_width  = DISPLAY_SIZE[0] / self.maze.width
        cell_height = DISPLAY_SIZE[1] / self.maze.height
        self.maze.make_maze()

        #Print grid
        for x in range(self.maze.width):
            pygame.draw.line(self.screen, WHITE, (cell_width*(x+1), 0), (cell_width*(x+1), DISPLAY_SIZE[1]), LINE_WIDTH)
        for y in range(self.maze.height):
            pygame.draw.line(self.screen, WHITE, (0, cell_height*(y+1)), (DISPLAY_SIZE[0], cell_height*(y+1)), LINE_WIDTH)

        #erase walls
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                cell = self.maze.cell_at(x,y)
                if cell.walls & 0b0001 == 0b0000:  #missing West wall
                    start_point = (cell_width*x, cell_height*y)
                    end_point   = (cell_width*x, cell_height*(y+1))
                    pygame.draw.line(self.screen, BLACK, start_point, end_point, LINE_WIDTH)
                if cell.walls & 0b0010 == 0b0000:  #missing South wall
                    start_point = (cell_width*x, cell_height*(y+1))
                    end_point   = (cell_width*(x+1), cell_height*(y+1))
                    pygame.draw.line(self.screen, BLACK, start_point, end_point, LINE_WIDTH)
                if cell.walls & 0b0100 == 0b0000:  #missing East wall
                    start_point = (cell_width*(x+1), cell_height*y)
                    end_point   = (cell_width*(x+1), cell_height*(y+1))
                    pygame.draw.line(self.screen, BLACK, start_point, end_point, LINE_WIDTH)
                if cell.walls & 0b1000 == 0b0000:  #missing North wall
                    start_point = (cell_width*x, cell_height*y)
                    end_point   = (cell_width*(x+1), cell_height*y)
                    pygame.draw.line(self.screen, BLACK, start_point, end_point, LINE_WIDTH)

    def draw_robot_helper(self, x, y, width, height, dir):
        """helps draw the dot that indicates the front of the robot"""
        if dir == 'N':
            x_result = x * width  + (width / 2)
            y_result = y * height + (height * 0.3)
        elif dir == 'E':
            x_result = x * width  + (width * 0.7)
            y_result = y * height + (height / 2)
        elif dir == 'S':
            x_result = x * width  + (width / 2)
            y_result = y * height + (height * 0.7)
        else:
            x_result =  x * width  + (width * 0.3)
            y_result =  y * height + (height / 2)
        return x_result, y_result

    def draw_robot(self, robot):
        """draws the robot in whatever location it is in"""
        cell_width = DISPLAY_SIZE[0] / robot.maze.width
        cell_height = DISPLAY_SIZE[1] / robot.maze.height

        rect_x, rect_y = robot.x*cell_width + (.25 * cell_width), robot.y*cell_height + (.25 * cell_height)
        circle_x, circle_y = self.draw_robot_helper(robot.x, robot.y, cell_width, cell_height, robot.forward)

        rect = pygame.Rect((rect_x, rect_y),(cell_width/2, cell_height/2))
        pygame.draw.rect(self.screen, WHITE, rect)
        pygame.draw.circle(self.screen, BLACK, (circle_x, circle_y), 3)

    def erase_robot(self, robot):
        """hides robot to help simulate movement"""
        cell_width = DISPLAY_SIZE[0] / robot.maze.width
        cell_height = DISPLAY_SIZE[1] / robot.maze.height
        x,y = robot.x*cell_width + (.25 * cell_width), robot.y*cell_height + (.25 * cell_height)
        rect = pygame.Rect((x,y),(cell_width/2, cell_height/2))
        pygame.draw.rect(self.screen, BLACK, rect)

    def run_game(self, speed):
        """main loop that runs the simulation"""
        pygame.display.set_caption('Maze')
        self.screen.fill(BLACK)
        self.draw_board()
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


            self.draw_robot(self.robot)
            pygame.display.flip()
            pygame.time.wait(speed)
            self.erase_robot(self.robot)
            self.algorithm(self.robot,self.maze.width-1,self.maze.height-1)












