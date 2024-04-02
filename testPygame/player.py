from Settings import *


class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.playerLife = 10
        self.playerMaxLife = 10
        self.playerAttack = 5
        self.playerVelocity = 5
        self.image = py.image.load('Images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = HEIGHT / 2
        self.rect.y = WIDTH / 2

    def MoveRight(self):
        self.rect.x += self.playerVelocity

    def MoveLeft(self):
        self.rect.x -= self.playerVelocity

    def Jump(self):
        self.rect.y += self.playerVelocity