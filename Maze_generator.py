import random

class Cell:
    """Maze will consist of a grid system and a cell will represent one 1x1 square"""

    wall_values = {'N':0b1000, 'E': 0b0100, 'S':0b0010, 'W':0b0001}
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self,x,y):
        """ initialize a cell at (x,y) """
        self.x = x
        self.y = y
        # initialized to have all walls (represented in binary for quick ops)
        self.walls = 0b1111;


    def has_all_walls(self):
        """ returns whether or not a block has all its walls """
        return self.walls == 0b1111

    def remove_wall(self,neighbor, direction):
        """ removes a wall between self and its neighbor given a direction N, S, E, W """
        self.walls = self.walls & (~Cell.wall_values[direction])
        neighbor.walls = neighbor.walls & (~Cell.wall_values[Cell.wall_pairs[direction]])

    def missing_wall(self, direction):
        return self.walls & Cell.wall_values[direction] == 0


class Maze:
    """Maze represented by a grid consisting of cells"""

    wall_values = {'N': 0b1000, 'E': 0b0100, 'S': 0b0010, 'W': 0b0001}

    def __init__(self, width, height, ix=0, iy=0):
        """ Initialize maze grid of size width x height """

        self.width, self.height = width, height
        self.ix,self.iy = ix, iy
        self.maze_grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def cell_at(self,x,y):
        """return cell at (x,y)"""
        return self.maze_grid[x][y]

    def __str__(self):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * self.width * 2]
        for y in range(self.height):
            maze_row = ['|']
            for x in range(self.width):
                if self.maze_grid[x][y].walls & Maze.wall_values['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.width):
                if self.maze_grid[x][y].walls & Maze.wall_values['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def find_valid_neighbours(self, cell):
        """Return a list of unvisited neighbours to cell."""

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.width) and (0 <= y2 < self.height):
                neighbour = self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def make_maze(self):
        # Total number of cells.
        n = self.width * self.height
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.find_valid_neighbours(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.remove_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1

# Maze dimensions (ncols, nrows)
nx, ny = 5,5
# Maze entry position
ix, iy = 0, 0

maze = Maze(nx, ny, ix, iy)
maze.make_maze()

print(maze)
