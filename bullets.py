import pygame as py


class Bullets(py.sprite.Sprite):

    def __init__(self, xpos, ypos, direction, speed, filename, side, main_screen):
        py.sprite.Sprite.__init__(self)
        self.filename = filename
        self.laser = py.image.load(("imagenes/{}.png").format(self.filename))
        self.rect = self.laser.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.direction = direction
        self.side = side
        self.main_screen = main_screen
        self.timer = py.time.get_ticks()

    def update(self, *args):
        self.main_screen.blit(self.laser, self.rect)
        self.rect.y += self.speed * self.direction
        if self.rect.y < 15 or self.rect.y > 600:
            self.kill()  # Remueve al elemento de la pantalla, en este caso a la bala
