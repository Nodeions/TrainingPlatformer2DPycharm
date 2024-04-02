from Settings import *
from player import Player



class Game:
    def __init__(self):
        self.running = True
        self.player = Player()


    def update(self):
        pass

    def draw(self):
        SCREEN.fill(0)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(player.image, player.rect)
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
        quit()