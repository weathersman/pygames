# Simple pygame program
import math
# Import and initialize the pygame library
import pygame
from pygame.locals import *


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
        self.image = pygame.image.load('bsquare.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = p
        self.peg = None
        self.name = None
        self.neighborone = list()
        self.neighbortwo = list()

    def update(self):
        pass


class Board:
    def __init__(self):
        super(Board, self).__init__()

    activehole = None
    activepeg = None

    pegs = pygame.sprite.RenderPlain()
    holes = pygame.sprite.RenderPlain()

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
        if (self.activehole.neighborone[1] is targethole) and (targethole.peg is None):
            if self.activehole.neighborone[0].peg is not None:
                self.activepeg.rect.x = targethole.rect.x - 8
                self.activepeg.rect.y = targethole.rect.y - 8
                targethole.peg = self.activepeg
                self.pegs.remove(self.activehole.neighborone[0].peg)
                self.activehole.neighborone[0].peg = None
                self.activehole.peg = None
        elif (self.activehole.neighbortwo[1] is targethole) and (targethole.peg is None):
            if self.activehole.neighbortwo[0].peg is not None:
                self.activepeg.rect.x = targethole.rect.x - 8
                self.activepeg.rect.y = targethole.rect.y - 8
                targethole.peg = self.activepeg
                self.pegs.remove(self.activehole.neighbortwo[0].peg)
                self.activehole.neighbortwo[0].peg = None
                self.activehole.peg = None
        else:
            self.activepeg.rect.x = self.activehole.rect.x - 8
            self.activepeg.rect.y = self.activehole.rect.y - 8

        self.activehole = None
        self.activepeg = None

    def update(self):
        pass


def setupgame():
    pegboard = Board()

    hole1 = Hole((100, 370))
    hole1.name = "hole1"
    pegboard.holes.add(hole1)
    hole2 = Hole((200, 370))
    hole2.name = "hole2"
    pegboard.holes.add(hole2)
    hole3 = Hole((300, 370))
    hole3.name = "hole3"
    pegboard.holes.add(hole3)
    hole4 = Hole((400, 370))
    hole4.name = "hole4"
    pegboard.holes.add(hole4)
    hole5 = Hole((150, 285))
    hole5.name = "hole5"
    pegboard.holes.add(hole5)
    hole6 = Hole((250, 285))
    hole6.name = "hole6"
    pegboard.holes.add(hole6)
    hole7 = Hole((350, 285))
    hole7.name = "hole7"
    pegboard.holes.add(hole7)
    hole8 = Hole((200, 200))
    hole8.name = "hole8"
    pegboard.holes.add(hole8)
    hole9 = Hole((300, 200))
    hole9.name = "hole9"
    pegboard.holes.add(hole9)
    hole10 = Hole((250, 125))
    hole10.name = "hole10"
    pegboard.holes.add(hole10)

    hole1.neighborone.insert(0, hole2)
    hole1.neighborone.insert(1, hole3)
    hole1.neighbortwo.insert(0, hole5)
    hole1.neighbortwo.insert(1, hole8)

    hole2.neighborone.insert(0, hole3)
    hole2.neighborone.insert(1, hole4)
    hole2.neighbortwo.insert(0, hole5)
    hole2.neighbortwo.insert(1, hole9)

    hole3.neighborone.insert(0, hole2)
    hole3.neighborone.insert(1, hole1)
    hole3.neighbortwo.insert(0, hole6)
    hole3.neighbortwo.insert(1, hole8)

    hole4.neighborone.insert(0, hole3)
    hole4.neighborone.insert(1, hole2)
    hole4.neighbortwo.insert(0, hole7)
    hole4.neighbortwo.insert(1, hole9)

    hole5.neighborone.insert(0, hole6)
    hole5.neighborone.insert(1, hole7)
    hole5.neighbortwo.insert(0, hole8)
    hole5.neighbortwo.insert(1, hole10)

    hole6.neighborone.insert(0, None)
    hole6.neighborone.insert(1, None)
    hole6.neighbortwo.insert(0, None)
    hole6.neighbortwo.insert(1, None)

    hole7.neighborone.insert(0, hole6)
    hole7.neighborone.insert(1, hole5)
    hole7.neighbortwo.insert(0, hole9)
    hole7.neighbortwo.insert(1, hole10)

    hole8.neighborone.insert(0, hole5)
    hole8.neighborone.insert(1, hole1)
    hole8.neighbortwo.insert(0, hole6)
    hole8.neighbortwo.insert(1, hole3)

    hole9.neighborone.insert(0, hole6)
    hole9.neighborone.insert(1, hole2)
    hole9.neighbortwo.insert(0, hole7)
    hole9.neighbortwo.insert(1, hole4)

    hole10.neighborone.insert(0, hole8)
    hole10.neighborone.insert(1, hole5)
    hole10.neighbortwo.insert(0, hole9)
    hole10.neighbortwo.insert(1, hole7)

    peg1 = Peg((99, 368))
    peg1.name = "peg1"
    pegboard.pegs.add(peg1)
    hole1.peg = peg1
    peg2 = Peg((199, 368))
    peg2.name = "peg2"
    pegboard.pegs.add(peg2)
    hole2.peg = peg2
    peg3 = Peg((299, 368))
    peg3.name = "peg3"
    pegboard.pegs.add(peg3)
    hole3.peg = peg3
    peg4 = Peg((399, 368))
    peg4.name = "peg4"
    pegboard.pegs.add(peg4)
    hole4.peg = peg4
    peg5 = Peg((149, 283))
    peg5.name = "peg5"
    pegboard.pegs.add(peg5)
    hole5.peg = peg5
    peg6 = Peg((249, 283))
    peg6.name = "peg6"
    pegboard.pegs.add(peg6)
    hole6.peg = peg6
    peg7 = Peg((349, 283))
    peg7.name = "peg7"
    pegboard.pegs.add(peg7)
    hole7.peg = peg7
    peg8 = Peg((199, 198))
    peg8.name = "peg8"
    pegboard.pegs.add(peg8)
    hole8.peg = peg8
    peg9 = Peg((299, 198))
    peg9.name = "peg9"
    pegboard.pegs.add(peg9)
    hole9.peg = peg9
    hole10.peg = None

    pegboard.activehole = None
    pegboard.activepeg = None

    return pegboard


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
board = setupgame()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                for hole in board.holes:
                    board.holes.remove(hole)
                for peg in board.pegs:
                    board.pegs.remove(peg)
                board.pegs = None
                board.holes = None
                board = setupgame()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for hole in board.holes:
                if hole.rect.collidepoint(pos):
                    if hole.peg is not None:
                        board.activepeg = hole.peg
                        board.activehole = hole
            board.displayvalues()
        if event.type == pygame.MOUSEBUTTONUP:
            if board.activepeg is not None:
                pos = pygame.mouse.get_pos()
                for hole in board.holes:
                    dist = math.sqrt(math.pow(hole.rect.x - pos[0], 2) + math.pow(hole.rect.y - pos[1], 2))
                    if dist < 50:
                        board.move(hole)
                        board.activepeg = None
                        board.activehole = None
            board.displayvalues()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if board.activepeg is not None:
                board.activepeg.rect.x = pos[0]
                board.activepeg.rect.y = pos[1]

    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, 'black', [(30, 410), (490, 410), (265, 60)])
    pygame.draw.polygon(screen, 'black', [(30, 410), (40, 400), (25, 400)])
    pygame.draw.polygon(screen, 'black', [(265, 60), (250, 50), (250, 80)])
    pygame.draw.polygon(screen, 'lightsalmon4', [(25, 400), (475, 400), (250, 50)])
    board.holes.draw(screen)
    board.pegs.draw(screen)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
