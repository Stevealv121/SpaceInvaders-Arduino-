# SpaceInvaders v.1.0
import pygame as py
import json
from random import*
from playership import PlayerShip
from invaders import Invader
from bullets import Bullets
from explosion import Explosion
from meteors import Meteoroids
from vars import Vars


class SpaceInvaders(Vars):

        # Constructor
        def __init__(self):
            super().__init__()
            py.init()

        def welcome_screen(self):  # Pantalla de bienvenida
            self.screen.fill(self.BLACK)

            for event in py.event.get():
                if event.type == py.KEYUP:
                    self.startGame = True
                    self.mainScreen = False
                if event.type == py.QUIT:
                    self.quitgame()
            self.screen.blit(self.titleText, (164, 155))
            # Texto parpadeando
            if self.change_text % 2 == 0:
                self.screen.blit(self.titleText2b, (201, 225))
                self.change_text += 1
            else:
                self.screen.blit(self.titleText2w, (201, 225))
                self.change_text += 1
            self.screen.blit(self.highscoreText, (350, 321))
            self.screen.blit(self.highscore1, (372, 361))
            self.screen.blit(self.highscore2, (370, 381))
            self.screen.blit(self.highscore3, (370, 401))
            self.screen.blit(self.highscore4, (370, 421))
            self.screen.blit(self.highscore5, (370, 441))
            py.display.update()
            self.fps.tick(3)

        def initial_position(self, score, lives):  # Crea la mayoria de instancias q necesita el juego para iniciar
            self.player = PlayerShip(self.screen)
            self.playerG = py.sprite.Group(self.player)
            self.explosionsG = py.sprite.Group()
            self.bullets = py.sprite.Group()
            self.invadersBullets = py.sprite.Group()
            self.meteoriteG = py.sprite.Group()
            self.enemyPosition = self.enemyPositionStart
            self.make_enemies()
            self.timer = py.time.get_ticks()
            self.shipTimer = py.time.get_ticks()
            self.score = score
            self.lives = lives
            self.audio()
            self.killed_row = -1
            self.killed_column = -1
            self.makeNewShip = False
            self.shipAlive = True

        def audio(self):
            for sound_name in ["shoot", "invaderkilled", "shipexplosion", "blaster-firing", "blaster-firing2"]:
                self.sounds[sound_name] = py.mixer.Sound("sonidos/{}.wav".format(sound_name))
                self.sounds[sound_name].set_volume(0.2)

        def controls_input(self):
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quitgame()
                if event.type == py.KEYDOWN:  # Loop, detecta cada vez q la barra espaciadora es presionada (disparar)
                    if event.key == py.K_SPACE:
                        if len(self.bullets) == 0 and self.shipAlive:
                            if self.score < 310:
                                bullet = Bullets(self.player.rect.x + 19, self.player.rect.y + 5, -1, 15, "laser",
                                                 "center", self.screen)
                                self.bullets.add(bullet)
                                self.allSprites.add(self.bullets)
                                self.sounds["blaster-firing"].play()
                            else:
                                left_bullet = Bullets(self.player.rect.x + 7, self.player.rect.y + 5, -1, 15, "laser",
                                                      "left", self.screen)
                                right_bullet = Bullets(self.player.rect.x + 32, self.player.rect.y + 5, -1, 15, "laser",
                                                       "right", self.screen)
                                self.bullets.add(left_bullet)
                                self.bullets.add(right_bullet)
                                self.allSprites.add(self.bullets)
                                self.sounds["blaster-firing2"].play()

        def make_enemies(self):  # Crea la cantidad de naves invasoras especificadas
            invaders = py.sprite.Group()
            for row in range(3):
                for column in range(10):
                    invader = Invader(row, column, self.screen, 600)
                    invader.rect.x = 100 + (column * 65)
                    invader.rect.y = self.enemyPosition + (row * 60)
                    invaders.add(invader)

            self.invaders = invaders
            self.allSprites = py.sprite.Group(self.player, self.invaders)

        def make_enemies_shoot(self):  # Instancia a los enemigos a disparar cada cierto tiempo
            column_list = []
            for enemy in self.invaders:
                column_list.append(enemy.column)

            column_set = set(column_list)
            column_list = list(column_set)
            shuffle(column_list)
            column = column_list[0]
            row_list = []

            for enemy in self.invaders:
                if enemy.column == column:
                    row_list.append(enemy.row)
            row = max(row_list)
            for enemy in self.invaders:
                if enemy.column == column and enemy.row == row:
                    if abs(py.time.get_ticks() - self.timer) > 700:
                        self.invadersBullets.add(
                            Bullets(enemy.rect.x + 14, enemy.rect.y + 20, 1, 5, "enemylaser", "center", self.screen))
                        self.allSprites.add(self.invadersBullets)
                        self.timer = py.time.get_ticks()
                        self.sounds["shoot"].play()

        def meteor_shower(self):  # Crea la caida de meteoritos
            meteoroid = Meteoroids(randrange(1, 10), self.screen)
            if py.time.get_ticks() - self.timer > 700:
                self.meteoriteG.add(meteoroid)
                self.allSprites.add(self.meteoriteG)
                self.timer = py.time.get_ticks()

        def update_enemy_speed(self):  # acelera la velocidad de los meteoritos segun el puntuaje
            if self.score > 1000:
                meteoroid = Meteoroids(randrange(5, 10), self.screen)
                if py.time.get_ticks() - self.timer > 700:
                    self.meteoriteG.add(meteoroid)
                    self.allSprites.add(self.meteoriteG)
                    self.timer = py.time.get_ticks()
            if self.score > 2000:
                meteoroid = Meteoroids(randrange(10, 20), self.screen)
                if py.time.get_ticks() - self.timer > 700:
                    self.meteoriteG.add(meteoroid)
                    self.allSprites.add(self.meteoriteG)
                    self.timer = py.time.get_ticks()
            if self.score > 3000:
                meteoroid = Meteoroids(randrange(1, 20), self.screen)
                self.meteoriteG.add(meteoroid)
                self.allSprites.add(self.meteoriteG)
                self.timer = py.time.get_ticks()

        def check_collisions(self):  # Detecta cada choque de un sprite con otro. eg.(choque de las balas con las naves)
            bullet_collide = py.sprite.groupcollide(self.bullets, self.invadersBullets, True, False)
            if bullet_collide:
                for value in bullet_collide.values():
                    for currentSprite in value:
                        self.invadersBullets.remove(currentSprite)
                        self.allSprites.remove(currentSprite)

            bullet_collide2 = py.sprite.groupcollide(self.bullets, self.meteoriteG, True, False)
            if bullet_collide2:
                for value in bullet_collide2.values():
                    for currentSprite in value:
                        self.sounds["invaderkilled"].play()
                        explosion = Explosion(currentSprite.rect.x, currentSprite.rect.y, 0, True, self.screen)
                        self.explosionsG.add(explosion)
                        self.meteoriteG.remove(currentSprite)
                        self.allSprites.remove(currentSprite)
                        self.score += 5

            enemies_collide = py.sprite.groupcollide(self.bullets, self.invaders, True, False)
            if enemies_collide:
                for value in enemies_collide.values():
                    for currentSprite in value:
                        self.sounds["invaderkilled"].play()
                        self.killed_row = currentSprite.row
                        self.killed_column = currentSprite.column
                        explosion = Explosion(currentSprite.rect.x, currentSprite.rect.y, currentSprite.row, False,
                                             self.screen)
                        self.explosionsG.add(explosion)
                        self.allSprites.remove(currentSprite)
                        self.invaders.remove(currentSprite)
                        self.game_timer = py.time.get_ticks()
                        self.score += 10
                        break

            player_collide = py.sprite.groupcollide(self.invadersBullets, self.playerG, True, False)
            if player_collide:
                for value in player_collide.values():
                    for playerShip in value:
                        if self.lives == 1:
                            self.lives -= 1
                        elif self.lives == 0:
                            self.gameOver = True
                            self.startGame = False
                        self.sounds["shipexplosion"].play()
                        explosion = Explosion(playerShip.rect.x, playerShip.rect.y, 0, True, self.screen)
                        self.explosionsG.add(explosion)
                        self.allSprites.remove(playerShip)
                        self.playerG.remove(playerShip)
                        self.makeNewShip = True
                        self.shipTimer = py.time.get_ticks()
                        self.shipAlive = False

            player_collide2 = py.sprite.groupcollide(self.invaders, self.playerG, True, False)
            if player_collide2:
                for value in player_collide2.values():
                    for currentSprite in value:
                        if self.lives == 1:
                            self.lives -= 1
                        elif self.lives == 0:
                            self.gameOver = True
                            self.startGame = False
                        self.sounds["shipexplosion"].play()
                        explosion = Explosion(currentSprite.rect.x, currentSprite.rect.y, 0, True, self.screen)
                        self.explosionsG.add(explosion)
                        self.allSprites.remove(currentSprite)
                        self.playerG.remove(currentSprite)
                        self.makeNewShip = True
                        self.shipTimer = py.time.get_ticks()
                        self.shipAlive = False

            player_collide3 = py.sprite.groupcollide(self.meteoriteG, self.playerG, True, False)
            if player_collide3:
                for value in player_collide3.values():
                    for currentSprite in value:
                        if self.lives == 1:
                            self.lives -= 1
                        elif self.lives == 0:
                            self.gameOver = True
                            self.startGame = False
                        self.sounds["shipexplosion"].play()
                        explosion = Explosion(currentSprite.rect.x, currentSprite.rect.y, 0, True, self.screen)
                        self.explosionsG.add(explosion)
                        self.allSprites.remove(currentSprite)
                        self.playerG.remove(currentSprite)
                        self.makeNewShip = True
                        self.shipTimer = py.time.get_ticks()
                        self.shipAlive = False

        def create_new_ship(self, createShip, current_time):  # Instancia de la nave defensora
            if createShip and current_time - self.shipTimer > 900:
                self.player = PlayerShip(self.screen)
                self.allSprites.add(self.player)
                self.playerG.add(self.player)
                self.makeNewShip = False
                self.shipAlive = True

        def json_load_file(self, json_file, place):
            with open(json_file) as json_file:
                json_data = json.load(json_file)
                json_file.close()
                return json_data[place]

        def json_dump_to_file(self, json_file, json_dict):
            with open(json_file, "w") as outfile:
                json.dump(json_dict, outfile)
                outfile.close()

        def save_scores(self, score):
            self.score_dict = {
                "first": score,
                "second": score,
                "third": score,
                "fourth": score,
                "fifth": score
            }
            self.json_dump_to_file("highscores.json", self.score_dict)

        def game_over(self, current_time):  # Fin del juego
            self.screen.blit(self.game_overText, (240, 155))
            if current_time - self.timer > 5000:  # Se espera 5s y reinicia el juego
                self.mainScreen = True

            for e in py.event.get():
                if e.type == py.QUIT:
                    self.quitgame()

        def play_game(self):  # Comienza el juego
            # Loop del juego
            while True:
                if self.mainScreen:
                    self.tries += 1
                    if self.tries > 1:
                        self.score = self.json_load_file("highscores.json", "first")
                        self.save_scores(self.score)
                    self.initial_position(0, 1)
                    self.screen.blit(self.background, (0, 0))
                    self.welcome_screen()
                elif self.startGame:
                    if len(self.invaders) == 0:
                        current_time = py.time.get_ticks()
                        if current_time - self.game_timer < 3000:
                            self.screen.blit(self.background, (0, 0))
                            self.controls_input()
                            self.initial_position(self.score, self.lives)
                            self.game_timer += 3000
                    else:
                        current_time = py.time.get_ticks()
                        self.screen.blit(self.background, (0, 0))
                        self.controls_input()
                        self.allSprites.update(current_time)
                        self.explosionsG.update(current_time)
                        self.check_collisions()
                        self.create_new_ship(self.makeNewShip, current_time)
                        self.scoretext = self.fontst.render("Score: " + str(self.score), True, self.WHITE)
                        self.screen.blit(self.scoretext, (5, 5))
                        self.update_enemy_speed()

                        if len(self.invaders) > 0:
                            self.make_enemies_shoot()
                            self.meteor_shower()

                elif self.gameOver:
                    current_time = py.time.get_ticks()
                    self.enemyPositionStart = self.enemyPositionDefault
                    self.game_over(current_time)
                    self.save_scores(self.score)

                py.display.update()
                self.fps.tick(60)

        def quitgame(self):
            py.quit()
            quit()


if __name__ == "__main__":
    game = SpaceInvaders()
    game.play_game()
