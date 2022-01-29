from calendar import c
import numpy as np
import pygame as pg

from util import rotation_matrix

vec = pg.math.Vector2

class Cube:
    all_sprites = []
    vertecies = np.array([
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1],
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1]
    ])
    projection_matrix = np.array([
        [1, 0, 0],
        [0, 1, 0]
    ])
    projected_points = np.array([
        [n, n] for n in range(len(vertecies))
    ])
    def __init__(self, game):
        self.all_sprites.append(self)
        self.game = game
        self.center = vec(self.game.width // 2, self.game.height // 2)
        self.radius = 5
        self.scale = 100
        self.angle = 0

    def update(self):
        self.angle += 0.001

    def draw(self):
        for i, point in enumerate(self.vertecies):
            rotated_x = rotation_matrix("x", self.angle) @ point.T
            rotated_y = rotation_matrix("y", self.angle) @ rotated_x.T
            rotated_z = rotation_matrix("z", self.angle) @ rotated_y.T
            projected = self.projection_matrix @ rotated_z.T
            x = projected[0] * self.scale + self.game.width // 2
            y = projected[1] * self.scale + self.game.height // 2
            self.projected_points[i] = [x, y]
            # pg.draw.circle(self.game.screen, self.game.colordict["black"], vec(x, y), self.radius)

        for i in range(4):
            # self.draw_connection(i, (i + 1) % 4, self.projected_points)
            # self.draw_connection(i + 4, ((i + 1) % 4) + 4, self.projected_points)
            self.draw_connection(i, (i + 4), self.projected_points)

        pg.draw.polygon(self.game.screen, self.game.colordict["magenta"], self.projected_points[:4])
        pg.draw.polygon(self.game.screen, self.game.colordict["magenta"], self.projected_points[4:8])
        # pg.draw.polygon(self.game.screen, self.game.colordict["red"], list(self.projected_points[2:5]) + list(self.projected_points[6:8]))


    def draw_connection(self, i, j, points):
        pg.draw.line(self.game.screen, self.game.colordict["magenta"], vec(points[i][0], points[i][1]), vec(points[j][0], points[j][1]))