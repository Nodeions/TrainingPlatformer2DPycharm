import pygame.transform
from game import Game
from player import Player

from Settings import *

class Game:
    def __init__(self):
        self.running = True
        self.player = Player()
        self.pressed = {py.K_RIGHT: False, py.K_LEFT: False}

    def update(self):
        if self.pressed[py.K_RIGHT]:
            self.player.MoveRight()
        elif self.pressed[py.K_LEFT]:
            self.player.MoveLeft()

    def draw(self):
        SCREEN.fill(0)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(self.player.image, self.player.rect)
        py.display.flip()

    def run(self):
        clock = py.time.Clock()
        while self.running:

            clock.tick(FPS)  # à mettre dans l'update ?
            self.update()
            self.draw()
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                elif event.type == py.KEYDOWN:
                    self.pressed[event.key] = True
                elif event.type == py.KEYUP:
                    self.pressed[event.key] = False
                elif event.type == py.K_SPACE:
                    self.player.Jump()
        quit()

background = py.image.load("Images/1.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
py.mouse.set_visible(0)

g = Game()
g.run()
