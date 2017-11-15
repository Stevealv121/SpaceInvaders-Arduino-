import pygame as py


class Vars:

    def __init__(self):
        # Ancho y altura de la pantalla
        self.WIDTH = 800
        self.HEIGHT = 600
        # Color           R    G    B
        self.WHITE = (255, 255, 255)
        self.GREEN = (78, 255, 87)
        self.YELLOW = (241, 255, 0)
        self.BLUE = (80, 255, 239)
        self.PURPLE = (203, 0, 255)
        self.RED = (237, 28, 36)
        self.BLACK = (0, 0, 0)
        # FPS
        self.fps = py.time.Clock()
        # Fuente de letra
        py.font.init()
        self.FONT = "fuente/space_invaders.ttf"
        # Texto
        self.fonttT = py.font.Font(self.FONT, 50)
        self.titleText = self.fonttT.render("Space Invaders", True, self.WHITE)
        self.fonttT2 = py.font.Font(self.FONT, 15)
        self.titleText2w = self.fonttT2.render("Presiona cualquier tecla para continuar", True, self.WHITE)
        self.titleText2b = self.fonttT2.render("Presiona cualquier tecla para continuar", True, self.BLACK)
        self.fonthsT = py.font.Font(self.FONT, 15)
        self.highscoreText = self.fonthsT.render("Highscores", True, self.WHITE)
        self.game_overText = self.fonttT.render("Game Over", True, self.WHITE)
        self.fontst = py.font.Font(self.FONT, 20)
        self.fonthst = py.font.Font(self.FONT, 10)
        self.highscore1 = self.fonthst.render("1. " + str(self.json_load_file("highscores.json", "first")), True, self.BLUE)
        self.highscore2 = self.fonthst.render("2. " + str(self.json_load_file("highscores.json", "second")), True, self.PURPLE)
        self.highscore3 = self.fonthst.render("3. " + str(self.json_load_file("highscores.json", "third")), True, self.RED)
        self.highscore4 = self.fonthst.render("4. " + str(self.json_load_file("highscores.json", "fourth")), True, self.YELLOW)
        self.highscore5 = self.fonthst.render("5. " + str(self.json_load_file("highscores.json", "fifth")), True, self.GREEN)
        # Miscelaneas
        self.iconimg = py.image.load("imagenes/icon.png")
        self.icon = py.display.set_icon(self.iconimg)
        self.caption = py.display.set_caption("Space Invaders")
        self.screen = py.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = py.image.load("imagenes/background6.jpg")
        # Variables auxiliares
        self.startGame = False
        self.mainScreen = True
        self.gameExit = False
        self.gameOver = False
        self.change_text = 0
        self.enemyPositionDefault = 65
        self.enemyPositionStart = self.enemyPositionDefault
        self.enemyPosition = self.enemyPositionStart
        self.score_dict = {}
        self.tries = 0
        self.sounds = {}
