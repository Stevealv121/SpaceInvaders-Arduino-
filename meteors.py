import pygame as py
from random import*


class Meteoroids(py.sprite.Sprite):
    def __init__(self, speed, main_screen):
        py.sprite.Sprite.__init__(self)
        self.speed = speed
        self.meteor = py.image.load("imagenes/meteor1.png")
        self.meteor = py.transform.scale(self.meteor, (40, 40))
        self.rect = self.meteor.get_rect(topleft=(randrange(30, 770), -100))
        self.main_screen = main_screen
        self.timer = py.time.get_ticks()

    def update(self, *args):
        self.main_screen.blit(self.meteor, self.rect)
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.kill()
