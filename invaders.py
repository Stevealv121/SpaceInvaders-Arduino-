import pygame as py


class Invader(py.sprite.Sprite):

    def __init__(self, row, column, main_screen, moveTime):
        py.sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.image = py.image.load("imagenes/invader.png")
        self.image = py.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.direction = 1
        self.rightMoves = 50
        self.leftMoves = 155
        self.moveNumber = 0
        self.moveTime = moveTime
        self.firstTime = True
        self.columns = [False] * 10
        self.aliveColumns = [True] * 10
        self.addRightMoves = False
        self.addLeftMoves = False
        self.numOfRightMoves = 0
        self.numOfLeftMoves = 0
        self.main_screen = main_screen
        self.timer = py.time.get_ticks()

    def update(self, *args):  # Definicion moviento de las naves invasoras
        if self.moveTime == 600:
            if self.moveNumber >= self.rightMoves and self.direction == 1:
                self.direction *= -1
                self.moveNumber = 0
                if self.addRightMoves:
                    self.rightMoves += self.numOfRightMoves
                if self.firstTime:
                    self.rightMoves = self.leftMoves
                    self.firstTime = False
            if self.moveNumber >= self.leftMoves and self.direction == -1:
                self.direction *= -1
                self.moveNumber = 0
                if self.addLeftMoves:
                    self.leftMoves += self.numOfLeftMoves
            if self.moveNumber < self.rightMoves and self.direction == 1:
                self.rect.x += 1
                self.moveNumber += 1
            if self.moveNumber < self.leftMoves and self.direction == -1:
                self.rect.x -= 1
                self.moveNumber += 1

            self.timer += self.moveTime
        if self.moveTime == 700:
            if self.moveNumber >= self.rightMoves and self.direction == 1:
                self.direction *= -1
                self.moveNumber = 0
                if self.addRightMoves:
                    self.rightMoves += self.numOfRightMoves
                if self.firstTime:
                    self.rightMoves = self.leftMoves
                    self.firstTime = False
            if self.moveNumber >= self.leftMoves and self.direction == -1:
                self.direction *= -1
                self.moveNumber = 0
                if self.addLeftMoves:
                    self.leftMoves += self.numOfLeftMoves
            if self.moveNumber < self.rightMoves and self.direction == 1:
                self.rect.x += 5
                self.moveNumber += 5
            if self.moveNumber < self.leftMoves and self.direction == -1:
                self.rect.x -= 5
                self.moveNumber += 5
            self.timer += self.moveTime
        if self.moveTime == 800:
            if self.moveNumber >= self.rightMoves and self.direction == 1:
                self.direction *= -1
                self.moveNumber = 0
                if self.addRightMoves:
                    self.rightMoves += self.numOfRightMoves
                if self.firstTime:
                    self.rightMoves = self.leftMoves
                    self.firstTime = False
            if self.moveNumber >= self.leftMoves and self.direction == -1:
                self.direction *= -1
                self.moveNumber = 0
                if self.addLeftMoves:
                    self.leftMoves += self.numOfLeftMoves
            if self.moveNumber < self.rightMoves and self.direction == 1:
                self.rect.x += 15
                self.moveNumber += 15
            if self.moveNumber < self.leftMoves and self.direction == -1:
                self.rect.x -= 15
                self.moveNumber += 15
            self.timer += self.moveTime
        self.main_screen.blit(self.image, self.rect)

    def check_column_deletion(self):

        for i in range(3):
            if all([self.columns[x] for x in range(i + 1)]) and self.aliveColumns[i]:
                self.leftMoves += 5
                self.aliveColumns[i] = False
                if self.direction == -1:
                    self.rightMoves += 5
                else:
                    self.addRightMoves = True
                    self.numOfRightMoves += 5

        for i in range(3):
            if all([self.columns[x] for x in range(9, 8 - i, -1)]) and self.aliveColumns[9 - i]:
                self.aliveColumns[9 - i] = False
                self.rightMoves += 5
                if self.direction == 1:
                    self.leftMoves += 5
                else:
                    self.addLeftMoves = True
                    self.numOfLeftMoves += 5
