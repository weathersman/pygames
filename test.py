# Simple pygame program

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

    def update(self):
        pass


class Hole(pygame.sprite.Sprite):
    def __init__(self, p):
        super(Hole, self).__init__()
        self.image = pygame.image.load('bsquare.png')
        self.image = pygame.transform.scale(self.image, (28, 28))
        self.rect = self.image.get_rect()
        self.rect.center = p
        self.peg = None
        self.neighborOne = None
        self.neighborTwo = None

    def update(self):
        pass


class Board():
    def __init__(self):
        super(Board, self).__init__()

    positions = list()
    activeHole = None
    activePeg = None

    def move(self, h):
        if self.activeHole.neighborOne is h or self.activeHole.neighborTwo is h:
            if self.activeHole.peg is not None and h.peg is None:
                h.peg = self.activePeg
                self.activeHole.peg = None
                h.peg.rect.x = h.rect.x
                h.peg.rect.y = h.rect.y
                self.activeHole = None
                self.activePeg = None

    def update(self):
        pass


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Create sprites
pegs = pygame.sprite.RenderPlain()
holes = pygame.sprite.RenderPlain()

hole1 = Hole((100, 370))
holes.add(hole1)
hole2 = Hole((200, 370))
holes.add(hole2)
hole3 = Hole((300, 370))
holes.add(hole3)
hole4 = Hole((400, 370))
holes.add(hole4)
hole5 = Hole((150, 285))
holes.add(hole5)
hole6 = Hole((250, 285))
holes.add(hole6)
hole7 = Hole((350, 285))
holes.add(hole7)
hole8 = Hole((200, 200))
holes.add(hole8)
hole9 = Hole((300, 200))
holes.add(hole9)
hole10 = Hole((250, 125))
holes.add(hole10)

hole1.neighborOne = hole3
hole1.neighborTwo = hole8

hole2.neighborOne = hole4
hole2.neighborTwo = hole9

hole3.neighborOne = hole1
hole3.neighborTwo = hole8

hole4.neighborOne = hole2
hole4.neighborTwo = hole9

hole5.neighborOne = hole7
hole5.neighborTwo = hole10

hole7.neighborOne = hole5
hole7.neighborTwo = hole10

hole8.neighborOne = hole1
hole8.neighborTwo = hole3

hole9.neighborOne = hole2
hole9.neighborTwo = hole9

hole10.neighborOne = hole5
hole10.neighborTwo = hole7

board = Board()
board.positions.insert(0, hole1)
board.positions.insert(1, hole2)
board.positions.insert(2, hole3)
board.positions.insert(3, hole4)
board.positions.insert(4, hole5)
board.positions.insert(5, hole6)
board.positions.insert(6, hole7)
board.positions.insert(7, hole8)
board.positions.insert(8, hole9)
board.positions.insert(9, hole10)

peg1 = Peg((99, 368))
pegs.add(peg1)
hole1.Peg = peg1
peg2 = Peg((199, 368))
pegs.add(peg2)
hole2.Peg = peg2
peg3 = Peg((299, 368))
pegs.add(peg3)
hole3.Peg = peg3
peg4 = Peg((399, 368))
pegs.add(peg4)
hole4.Peg = peg4
peg5 = Peg((149, 283))
pegs.add(peg5)
hole5.Peg = peg5
peg6 = Peg((249, 283))
pegs.add(peg6)
hole6.Peg = peg6
peg7 = Peg((349, 283))
pegs.add(peg7)
hole7.Peg = peg7
peg8 = Peg((199, 198))
pegs.add(peg8)
hole8.Peg = peg8
peg9 = Peg((299, 198))
pegs.add(peg9)
hole9.Peg = None

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for hole in holes:
                if hole.rect.collidepoint(pos) and hole.peg is not None:
                    board.activePeg = hole.peg
                    board.activeHole = hole
        if event.type == pygame.MOUSEBUTTONUP:
            if board.activePeg is not None:
                pos = pygame.mouse.get_pos()
                for hole in holes:
                    if hole.rect.collidepoint(pos):
                        board.move(hole)
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if board.activePeg is not None:
                board.activePeg.rect.x = pos[0]
                board.activePeg.rect.y = pos[1]

    screen.fill((255, 255, 255))

    pygame.draw.polygon(screen, 'brown', [(25, 400), (475,400), (250, 50)])

    holes.draw(screen)
    pegs.draw(screen)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()