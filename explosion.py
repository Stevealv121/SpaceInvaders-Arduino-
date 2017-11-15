import pygame as py


class Explosion(py.sprite.Sprite):
    
    def __init__(self, xpos, ypos, row, ship, main_screen):
        py.sprite.Sprite.__init__(self)
        self.main_screen = main_screen
        self.row = row
        self.isShip = ship
        self.image = py.image.load("imagenes/explosion.png")
        self.image = py.transform.scale(self.image, (40, 35))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.main_screen.blit(self.image, self.rect)
        self.timer = py.time.get_ticks()
        
    def update(self, current_time):
        if self.isShip:    
            if 300 < current_time - self.timer <= 600:
                self.main_screen.blit(self.image, self.rect)
            if current_time - self.timer > 900:
                self.kill()
        else:  # Crea el efecto de explosion (hace la imagen mas grande por unos segundos)
            if current_time - self.timer <= 100:
                self.main_screen.blit(self.image, self.rect)
            if 100 < current_time - self.timer <= 200:
                self.image = py.transform.scale(self.image, (50, 45))
                self.main_screen.blit(self.image, (self.rect.x-6, self.rect.y-6))
            if current_time - self.timer > 400:
                self.kill()
