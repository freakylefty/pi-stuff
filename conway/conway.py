import random


class GameOfLife:
    def __init__(self, width, height, initial_state=None):
        self._width = width
        self._height = height
        if initial_state:
            self._grid = [row[:] for row in initial_state]
        else:
            self._grid = [[0 for _ in range(width)] for _ in range(height)]

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def grid(self):
        return self._grid

    def random_cell(self):
        # For cells that are out of range (e.g. left neighbour of left-most column) get a random dead/alive value, skewed towards dead
        # This guarantees the simulation will keep on going, though activity will be biased towards the edges
        # Other strategies involve adding noise to dead spots or occasionally artificially throwing guns, gliders, etc into the mix
        return random.choice([0, 0, 1])

    def get_cell(self, x, y):
        if 0 <= x < self._width and 0 <= y < self._height:
            return self._grid[y][x]
        else:
            return self.random_cell()

    def count_alive_neighbors(self, x, y):
        directions = [(-1, -1), (0, -1), (1, -1),
                      (-1, 0), (1, 0),
                      (-1, 1), (0, 1), (1, 1)]
        return sum(self.get_cell(x + dx, y + dy) for dx, dy in directions)

    def tick(self):
        new_grid = [[0 for _ in range(self._width)] for _ in range(self._height)]
        for y in range(self._height):
            for x in range(self._width):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self._grid[y][x] == 1:
                    new_grid[y][x] = 1 if alive_neighbors in [2, 3] else 0
                else:
                    new_grid[y][x] = 1 if alive_neighbors == 3 else 0
        self._grid = new_grid
