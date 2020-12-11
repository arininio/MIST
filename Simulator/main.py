import Maze_generator
import robot
import maze_frontend

INITIAL_X = 0
INITIAL_Y = 0
INIT_MAZE_W = 10
INIT_MAZE_H = 10

'''change this value to change speed of simulation (in ms)'''
SPEED = 500

def initialize_maze(width, height):
    return Maze_generator.Maze(width, height)


def initialize_robot(initial_x, initial_y, maze):
    return robot.Robot(initial_x, initial_y, maze)


def SLPA(robot, end_x, end_y):
    """straight line path algorithm, robot follows the left hand wall until it reaches the end"""
    if robot.x == end_x and robot.y == end_y:
        pass
    elif robot.changed_dir and robot.can_go_forward():
        robot.move_forward()

    elif robot.can_go_left():
        robot.turn_left()

    elif robot.can_go_forward():
        robot.move_forward()

    else:
        robot.turn_right()


def main():
    maze = initialize_maze(INIT_MAZE_W, INIT_MAZE_H)
    robot = initialize_robot(INITIAL_X, INITIAL_Y, maze)
    game = maze_frontend.Frontend(maze, robot, SLPA)
    game.run_game(SPEED)

if __name__ == "__main__":
    main()