import pygame as pg
import sprites

pg.init()

class Game:
    colordict = {"white": (255, 255, 255), "red": (255, 0, 0), "black": (0, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "gray": (255/2, 255/2, 255/2), "magenta": (255, 0, 255)}
    def __init__(self):
        self.width, self.height = 600, 600
        self.screen = pg.display.set_mode((self.width, self.height), 0, 32)
        self.clock = pg.time.Clock()
        self.FPS = 60

    def new(self):
        self.c1 = sprites.Cube(self)

    def run(self):
        while True:
            self.dt = self.clock.tick(self.FPS) / 1e3
            self.event_handling()
            self.update()
            self.draw()

    def update(self):
        self.c1.update()

    def draw(self):
        self.screen.fill(self.colordict["black"])

        self.c1.draw()

        pg.display.flip()

    def quit(self):
        pg.quit()
        exit()

    def event_handling(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

g1 = Game()
while True:
    g1.new()
    g1.run()
