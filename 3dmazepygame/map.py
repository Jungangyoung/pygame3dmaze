"""
import pygame as pg


_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, 1, 1, 1, _, 1],
    [1, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 20, pos[1] * 20, 20, 20), 2)
         for pos in self.world_map]
"""


import pygame as pg
import random


class Map:
    def __init__(self, game):
        self.game = game

        # Maze dimensions
        # Use odd numbers!
        self.width = 21
        self.height = 21

        self.world_map = {}

        # Player spawn position
        self.spawn = (1.5, 1.5)

        self.generate_maze()

    # ==================================================
    # MAZE GENERATION
    # ==================================================

    def generate_maze(self):

        # Start with everything being a wall
        grid = [
            [1 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        # Start position
        start_x = 1
        start_y = 1

        # Make starting cell floor
        grid[start_y][start_x] = 0

        # Stack for recursive backtracking
        stack = [(start_x, start_y)]

        while stack:

            x, y = stack[-1]

            # Find unvisited cells two tiles away
            neighbors = []

            directions = [
                (2, 0),
                (-2, 0),
                (0, 2),
                (0, -2)
            ]

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if (
                    1 <= nx < self.width - 1
                    and 1 <= ny < self.height - 1
                    and grid[ny][nx] == 1
                ):
                    neighbors.append((nx, ny, dx, dy))

            # No unvisited neighbors
            if not neighbors:
                stack.pop()
                continue

            # Choose random neighbor
            nx, ny, dx, dy = random.choice(neighbors)

            # Remove wall between cells
            grid[y + dy // 2][x + dx // 2] = 0

            # Make new cell floor
            grid[ny][nx] = 0

            # Continue from new cell
            stack.append((nx, ny))

        # Convert grid into world_map
        self.world_map.clear()

        for y in range(self.height):
            for x in range(self.width):

                if grid[y][x] == 1:
                    self.world_map[(x, y)] = 1

    # ==================================================
    # DRAW MINIMAP
    # ==================================================

    def draw(self):

        for x, y in self.world_map:

            pg.draw.rect(
                self.game.screen,
                'darkgray',
                (
                    x * 20,
                    y * 20,
                    20,
                    20
                ),
                2
            )

"""

import pygame as pg
import random


class Map:
    def __init__(self, game):
        self.game = game

        self.width = 15
        self.height = 15

        self.world_map = {}

        self.spawn = (1.5, 1.5)
        self.exit = (1.5, 1.5)

        self.generate_dungeon()

    # ==================================================
    # GENERATE DUNGEON
    # ==================================================

    def generate_dungeon(self):

        # Start completely filled with walls
        grid = [
            [1 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        rooms = []

        # --------------------------------------------------
        # CREATE ROOMS
        # --------------------------------------------------

        for _ in range(30):

            room_width = random.randrange(3, 8, 2)
            room_height = random.randrange(3, 8, 2)

            x = random.randrange(
                1,
                self.width - room_width,
                2
            )

            y = random.randrange(
                1,
                self.height - room_height,
                2
            )

            new_room = (
                x,
                y,
                room_width,
                room_height
            )

            # Don't overlap existing rooms
            if any(self.rooms_overlap(new_room, room)
                   for room in rooms):
                continue

            self.carve_room(grid, new_room)

            rooms.append(new_room)

        # --------------------------------------------------
        # CONNECT ROOMS
        # --------------------------------------------------

        for i in range(1, len(rooms)):

            previous = rooms[i - 1]
            current = rooms[i]

            x1 = previous[0] + previous[2] // 2
            y1 = previous[1] + previous[3] // 2

            x2 = current[0] + current[2] // 2
            y2 = current[1] + current[3] // 2

            # Randomly choose corridor direction
            if random.choice([True, False]):

                self.carve_horizontal(
                    grid,
                    x1,
                    x2,
                    y1
                )

                self.carve_vertical(
                    grid,
                    y1,
                    y2,
                    x2
                )

            else:

                self.carve_vertical(
                    grid,
                    y1,
                    y2,
                    x1
                )

                self.carve_horizontal(
                    grid,
                    x1,
                    x2,
                    y2
                )

        # --------------------------------------------------
        # ADD EXTRA CONNECTIONS
        # --------------------------------------------------

        # These make the dungeon less like a tree
        # and create loops.
        for _ in range(8):

            if len(rooms) < 2:
                break

            room_a = random.choice(rooms)
            room_b = random.choice(rooms)

            if room_a == room_b:
                continue

            x1 = room_a[0] + room_a[2] // 2
            y1 = room_a[1] + room_a[3] // 2

            x2 = room_b[0] + room_b[2] // 2
            y2 = room_b[1] + room_b[3] // 2

            if random.choice([True, False]):

                self.carve_horizontal(
                    grid,
                    x1,
                    x2,
                    y1
                )

                self.carve_vertical(
                    grid,
                    y1,
                    y2,
                    x2
                )

            else:

                self.carve_vertical(
                    grid,
                    y1,
                    y2,
                    x1
                )

                self.carve_horizontal(
                    grid,
                    x1,
                    x2,
                    y2
                )

        # --------------------------------------------------
        # CONVERT TO WORLD MAP
        # --------------------------------------------------

        self.world_map.clear()

        for y in range(self.height):
            for x in range(self.width):

                if grid[y][x] == 1:
                    self.world_map[(x, y)] = 1

        # --------------------------------------------------
        # PLAYER SPAWN
        # --------------------------------------------------

        self.spawn = self.find_spawn(grid, rooms)

        # --------------------------------------------------
        # EXIT
        # --------------------------------------------------

        self.exit = self.find_exit(grid, self.spawn)

    # ==================================================
    # ROOM FUNCTIONS
    # ==================================================

    def rooms_overlap(self, a, b):

        ax, ay, aw, ah = a
        bx, by, bw, bh = b

        return not (
            ax + aw + 1 < bx
            or bx + bw + 1 < ax
            or ay + ah + 1 < by
            or by + bh + 1 < ay
        )

    def carve_room(self, grid, room):

        x, y, width, height = room

        for yy in range(y, y + height):

            for xx in range(x, x + width):

                if (
                    0 < xx < self.width - 1
                    and 0 < yy < self.height - 1
                ):
                    grid[yy][xx] = 0

    # ==================================================
    # CORRIDORS
    # ==================================================

    def carve_horizontal(self, grid, x1, x2, y):

        start = min(x1, x2)
        end = max(x1, x2)

        for x in range(start, end + 1):

            if 0 < x < self.width - 1:
                grid[y][x] = 0

    def carve_vertical(self, grid, y1, y2, x):

        start = min(y1, y2)
        end = max(y1, y2)

        for y in range(start, end + 1):

            if 0 < y < self.height - 1:
                grid[y][x] = 0

    # ==================================================
    # FIND PLAYER SPAWN
    # ==================================================

    def find_spawn(self, grid, rooms):

        if rooms:

            room = random.choice(rooms)

            x = room[0] + room[2] // 2
            y = room[1] + room[3] // 2

            return x + 0.5, y + 0.5

        # Fallback
        for y in range(1, self.height - 1):

            for x in range(1, self.width - 1):

                if grid[y][x] == 0:
                    return x + 0.5, y + 0.5

        return 1.5, 1.5

    # ==================================================
    # FIND EXIT
    # ==================================================

    def find_exit(self, grid, spawn):

        sx = int(spawn[0])
        sy = int(spawn[1])

        # Find the floor tile furthest from spawn
        visited = {(sx, sy)}
        queue = [(sx, sy)]

        furthest = (sx, sy)

        while queue:

            x, y = queue.pop(0)

            furthest = (x, y)

            neighbors = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]

            for nx, ny in neighbors:

                if (
                    0 < nx < self.width - 1
                    and 0 < ny < self.height - 1
                    and grid[ny][nx] == 0
                    and (nx, ny) not in visited
                ):

                    visited.add((nx, ny))
                    queue.append((nx, ny))

        x, y = furthest

        return x + 0.5, y + 0.5

    # ==================================================
    # DRAW
    # ==================================================

    def draw(self):

        for x, y in self.world_map:

            pg.draw.rect(
                self.game.screen,
                'darkgray',
                (
                    x * 20,
                    y * 20,
                    20,
                    20
                ),
                2
            )

"""