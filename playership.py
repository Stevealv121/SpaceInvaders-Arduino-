import pygame as py


class PlayerShip(py.sprite.Sprite):

    def __init__(self, main_screen):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load("imagenes/ship1.png")
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.main_screen = main_screen
        self.speed = 5

    def update(self, *args):
        keys = py.key.get_pressed()
        if keys[py.K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
            self.image = py.image.load("imagenes/ship1-x.png")
        if keys[py.K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
            self.image = py.image.load("imagenes/ship1+x.png")
        if keys[py.K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
            self.image = py.image.load("imagenes/ship1.png")
        if keys[py.K_DOWN] and self.rect.y < 540:
            self.rect.y += self.speed
            self.image = py.image.load("imagenes/ship1.png")
        self.main_screen.blit(self.image, self.rect)
