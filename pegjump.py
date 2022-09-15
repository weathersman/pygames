# Peg Jump Game
import math
import pygame
from pygame.locals import *

pygame.mixer.init()

class Peg(pygame.sprite.Sprite):

    def __init__(self, p):
        super(Peg, self).__init__()
        self.image = pygame.image.load('ycircle.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = p
        self.name = None

    def update(self):
        pass


class Hole(pygame.sprite.Sprite):
    def __init__(self, p):
        super(Hole, self).__init__()
        self.image = pygame.image.load('bcircle.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = p
        self.peg = None
        self.name = None
        self.neighborone = list()
        self.neighbortwo = list()
        self.neighborthree = list()
        self.neighborfour = list()

    def update(self):
        pass


class Board:
    def __init__(self):
        super(Board, self).__init__()

    activehole = None
    activepeg = None
    won = False

    pegs = pygame.sprite.RenderPlain()
    holes = pygame.sprite.RenderPlain()
    pegsound = pygame.mixer.Sound("joy.wav")
    winsound = pygame.mixer.Sound("yeahbaby.wav")

    # for debugging purposes
    def displayvalues(self):
        print("***********************")
        if self.activehole is not None:
            print("Active Hole: " + self.activehole.name)
        else:
            print("Active Hole is None")

        if self.activepeg is not None:
            print("Active Peg: " + self.activepeg.name)
        else:
            print("Active Peg is None")

        for hole in self.holes:
            if hole.peg is not None:
                print(hole.name + " contains " + hole.peg.name)
            else:
                print(hole.name + " contains None")
        print("***********************")

    def move(self, targethole):
        if(self.activehole is not None) and (self.activepeg is not None):
            if (len(self.activehole.neighborone) > 0) and (self.activehole.neighborone[1] is targethole) and (targethole.peg is None) and (self.activehole.neighborone[0].peg is not None):
                self.activepeg.rect.x = targethole.rect.x - 8
                self.activepeg.rect.y = targethole.rect.y - 8
                pygame.mixer.Sound.play(self.pegsound)
                targethole.peg = self.activepeg
                self.pegs.remove(self.activehole.neighborone[0].peg)
                self.activehole.neighborone[0].peg = None
                self.activehole.peg = None
            elif (len(self.activehole.neighbortwo) > 0) and (self.activehole.neighbortwo[1] is targethole) and (targethole.peg is None) and (self.activehole.neighbortwo[0].peg is not None):
                self.activepeg.rect.x = targethole.rect.x - 8
                self.activepeg.rect.y = targethole.rect.y - 8
                pygame.mixer.Sound.play(self.pegsound)
                targethole.peg = self.activepeg
                self.pegs.remove(self.activehole.neighbortwo[0].peg)
                self.activehole.neighbortwo[0].peg = None
                self.activehole.peg = None
            elif (len(self.activehole.neighborthree) > 0) and (self.activehole.neighborthree[1] is targethole) and (targethole.peg is None) and (self.activehole.neighborthree[0].peg is not None):
                self.activepeg.rect.x = targethole.rect.x - 8
                self.activepeg.rect.y = targethole.rect.y - 8
                pygame.mixer.Sound.play(self.pegsound)
                targethole.peg = self.activepeg
                self.pegs.remove(self.activehole.neighborthree[0].peg)
                self.activehole.neighborthree[0].peg = None
                self.activehole.peg = None
            elif (len(self.activehole.neighborfour) > 0) and (self.activehole.neighborfour[1] is targethole) and (targethole.peg is None) and (self.activehole.neighborfour[0].peg is not None):
                self.activepeg.rect.x = targethole.rect.x - 8
                self.activepeg.rect.y = targethole.rect.y - 8
                pygame.mixer.Sound.play(self.pegsound)
                targethole.peg = self.activepeg
                self.pegs.remove(self.activehole.neighborfour[0].peg)
                self.activehole.neighborfour[0].peg = None
                self.activehole.peg = None
            else:
                self.activepeg.rect.x = self.activehole.rect.x - 8
                self.activepeg.rect.y = self.activehole.rect.y - 8

            self.activehole = None
            self.activepeg = None
        else:
            print("Invalid parameters sent to move()")

    def clear(self):
        for h in self.holes:
            self.holes.remove(h)
        for p in self.pegs:
            self.pegs.remove(p)
        self.pegs = None
        self.holes = None

    def update(self):
        pass


def setupgame():
    pegboard = Board()
    pegboard.won = False

    hole1 = Hole((75, 370))
    hole1.name = "hole1"
    pegboard.holes.add(hole1)
    hole2 = Hole((155, 370))
    hole2.name = "hole2"
    pegboard.holes.add(hole2)
    hole3 = Hole((250, 370))
    hole3.name = "hole3"
    pegboard.holes.add(hole3)
    hole4 = Hole((345, 370))
    hole4.name = "hole4"
    pegboard.holes.add(hole4)
    hole5 = Hole((425, 370))
    hole5.name = "hole5"
    pegboard.holes.add(hole5)

    hole6 = Hole((120, 300))
    hole6.name = "hole6"
    pegboard.holes.add(hole6)
    hole7 = Hole((205, 300))
    hole7.name = "hole7"
    pegboard.holes.add(hole7)
    hole8 = Hole((295, 300))
    hole8.name = "hole8"
    pegboard.holes.add(hole8)
    hole9 = Hole((380, 300))
    hole9.name = "hole9"
    pegboard.holes.add(hole9)

    hole10 = Hole((160, 235))
    hole10.name = "hole10"
    pegboard.holes.add(hole10)
    hole11 = Hole((250, 235))
    hole11.name = "hole11"
    pegboard.holes.add(hole11)
    hole12 = Hole((340, 235))
    hole12.name = "hole12"
    pegboard.holes.add(hole12)

    hole13 = Hole((205, 165))
    hole13.name = "hole13"
    pegboard.holes.add(hole13)
    hole14 = Hole((295, 165))
    hole14.name = "hole14"
    pegboard.holes.add(hole14)

    hole15 = Hole((250, 100))
    hole15.name = "hole15"
    pegboard.holes.add(hole15)

    hole1.neighborone.insert(0, hole2)
    hole1.neighborone.insert(1, hole3)
    hole1.neighbortwo.insert(0, hole6)
    hole1.neighbortwo.insert(1, hole10)

    hole2.neighborone.insert(0, hole3)
    hole2.neighborone.insert(1, hole4)
    hole2.neighbortwo.insert(0, hole7)
    hole2.neighbortwo.insert(1, hole11)

    hole3.neighborone.insert(0, hole2)
    hole3.neighborone.insert(1, hole1)
    hole3.neighbortwo.insert(0, hole7)
    hole3.neighbortwo.insert(1, hole10)
    hole3.neighborthree.insert(0, hole8)
    hole3.neighborthree.insert(1, hole12)
    hole3.neighborfour.insert(0, hole4)
    hole3.neighborfour.insert(1, hole5)

    hole4.neighborone.insert(0, hole3)
    hole4.neighborone.insert(1, hole2)
    hole4.neighbortwo.insert(0, hole8)
    hole4.neighbortwo.insert(1, hole11)

    hole5.neighborone.insert(0, hole4)
    hole5.neighborone.insert(1, hole3)
    hole5.neighbortwo.insert(0, hole9)
    hole5.neighbortwo.insert(1, hole12)

    hole6.neighborone.insert(0, hole7)
    hole6.neighborone.insert(1, hole8)
    hole6.neighbortwo.insert(0, hole10)
    hole6.neighbortwo.insert(1, hole13)

    hole7.neighborone.insert(0, hole8)
    hole7.neighborone.insert(1, hole9)
    hole7.neighbortwo.insert(0, hole11)
    hole7.neighbortwo.insert(1, hole14)

    hole8.neighborone.insert(0, hole7)
    hole8.neighborone.insert(1, hole6)
    hole8.neighbortwo.insert(0, hole11)
    hole8.neighbortwo.insert(1, hole13)

    hole9.neighborone.insert(0, hole8)
    hole9.neighborone.insert(1, hole7)
    hole9.neighbortwo.insert(0, hole12)
    hole9.neighbortwo.insert(1, hole14)

    hole10.neighborone.insert(0, hole6)
    hole10.neighborone.insert(1, hole1)
    hole10.neighbortwo.insert(0, hole13)
    hole10.neighbortwo.insert(1, hole15)
    hole10.neighborthree.insert(0, hole7)
    hole10.neighborthree.insert(1, hole3)
    hole10.neighborfour.insert(0, hole11)
    hole10.neighborfour.insert(1, hole12)

    hole11.neighborone.insert(0, hole7)
    hole11.neighborone.insert(1, hole2)
    hole11.neighbortwo.insert(0, hole8)
    hole11.neighbortwo.insert(1, hole4)

    hole12.neighborone.insert(0, hole9)
    hole12.neighborone.insert(1, hole5)
    hole12.neighbortwo.insert(0, hole14)
    hole12.neighbortwo.insert(1, hole15)
    hole12.neighborthree.insert(0, hole8)
    hole12.neighborthree.insert(1, hole3)
    hole12.neighborfour.insert(0, hole11)
    hole12.neighborfour.insert(1, hole10)

    hole13.neighborone.insert(0, hole10)
    hole13.neighborone.insert(1, hole6)
    hole13.neighbortwo.insert(0, hole11)
    hole13.neighbortwo.insert(1, hole8)

    hole14.neighborone.insert(0, hole11)
    hole14.neighborone.insert(1, hole7)
    hole14.neighbortwo.insert(0, hole12)
    hole14.neighbortwo.insert(1, hole9)

    hole15.neighborone.insert(0, hole13)
    hole15.neighborone.insert(1, hole10)
    hole15.neighbortwo.insert(0, hole14)
    hole15.neighbortwo.insert(1, hole12)

    peg1 = Peg((75, 370))
    peg1.name = "peg1"
    pegboard.pegs.add(peg1)
    hole1.peg = peg1
    peg2 = Peg((155, 370))
    peg2.name = "peg2"
    pegboard.pegs.add(peg2)
    hole2.peg = peg2
    peg3 = Peg((250, 370))
    peg3.name = "peg3"
    pegboard.pegs.add(peg3)
    hole3.peg = peg3
    peg4 = Peg((345, 370))
    peg4.name = "peg4"
    pegboard.pegs.add(peg4)
    hole4.peg = peg4
    peg5 = Peg((425, 370))
    peg5.name = "peg5"
    pegboard.pegs.add(peg5)
    hole5.peg = peg5

    peg6 = Peg((120, 300))
    peg6.name = "peg6"
    pegboard.pegs.add(peg6)
    hole6.peg = peg6
    peg7 = Peg((205, 300))
    peg7.name = "peg7"
    pegboard.pegs.add(peg7)
    hole7.peg = peg7
    peg8 = Peg((295, 300))
    peg8.name = "peg8"
    pegboard.pegs.add(peg8)
    hole8.peg = peg8
    peg9 = Peg((380, 300))
    peg9.name = "peg9"
    pegboard.pegs.add(peg9)
    hole9.peg = peg9

    peg10 = Peg((160, 235))
    peg10.name = "peg10"
    pegboard.pegs.add(peg10)
    hole10.peg = peg10

    peg11 = Peg((250, 235))
    peg11.name = "peg11"
    pegboard.pegs.add(peg11)
    hole11.peg = peg11

    peg12 = Peg((340, 235))
    peg12.name = "peg12"
    pegboard.pegs.add(peg12)
    hole12.peg = peg12

    peg13 = Peg((205, 165))
    peg13.name = "peg13"
    pegboard.pegs.add(peg13)
    hole13.peg = peg13

    peg14 = Peg((295, 165))
    peg14.name = "peg14"
    pegboard.pegs.add(peg14)
    hole14.peg = peg14

    hole15.peg = None
    pegboard.activehole = None
    pegboard.activepeg = None

    return pegboard


# initialize game
pygame.init()
screen = pygame.display.set_mode([500, 500])
board = setupgame()

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                board.clear()
                board = setupgame()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for hole in board.holes:
                if hole.rect.collidepoint(pos):
                    if hole.peg is not None:
                        board.activepeg = hole.peg
                        board.activehole = hole
            #board.displayvalues()
        if event.type == pygame.MOUSEBUTTONUP:
            if (board.activepeg is not None) and (board.activehole is not None):
                pos = pygame.mouse.get_pos()
                for hole in board.holes:
                    # is peg dropped close enough to hole?
                    dist = math.sqrt(math.pow(hole.rect.x - pos[0], 2) + math.pow(hole.rect.y - pos[1], 2))
                    if dist < 50:
                        board.move(hole)
            #board.displayvalues()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if board.activepeg is not None:
                board.activepeg.rect.x = pos[0]
                board.activepeg.rect.y = pos[1]

    # draw the game elements
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, 'black', [(35, 410), (490, 410), (265, 60)])
    pygame.draw.polygon(screen, 'black', [(35, 410), (45, 400), (25, 400)])
    pygame.draw.line(screen, 'slategray', (490, 410), (475, 400))
    pygame.draw.polygon(screen, 'black', [(265, 60), (250, 50), (250, 80)])
    pygame.draw.polygon(screen, 'lightsalmon4', [(25, 400), (475, 400), (250, 50)])
    board.holes.draw(screen)
    board.pegs.draw(screen)

    font = pygame.font.SysFont('arial', 14)
    text1 = font.render('Jump pegs by click, drag, and release on an adjacent empty hole', True, (0, 0, 0), (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.x = 40
    textRect1.y = 440

    text2 = font.render('Use Escape key to reset game', True, (0, 0, 0), (255, 255, 255))
    textRect2 = text2.get_rect()
    textRect2.x = 40
    textRect2.y = 460

    font2 = pygame.font.SysFont('Verdana', 26)
    text3 = font2.render('Peg Jump', True, (0, 0, 0), (255, 255, 255))
    textRect3 = text3.get_rect()
    textRect3.x = 10
    textRect3.y = 10

    font3 = pygame.font.SysFont('Verdana', 30)
    text4 = font3.render('You Win!', True, (0, 0, 205), (255, 255, 255))
    textRect4 = text4.get_rect()
    textRect4.x = 320
    textRect4.y = 50

    text5 = font.render('Leave Just One!', True, (0, 0, 0), (255, 255, 255))
    textRect5 = text5.get_rect()
    textRect5.x = 50
    textRect5.y = 50

    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)

    if len(board.pegs) == 1:
        screen.blit(text4, textRect4)
        if not board.won:
            pygame.mixer.Sound.play(board.winsound)
            board.won = True

    screen.blit(text5, textRect5)

    # Update the display
    pygame.display.flip()

pygame.quit()
