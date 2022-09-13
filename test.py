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
        self.peg = Peg((0, 0))
        self.neighborOne = list()
        self.neighborTwo = list()

    def update(self):
        pass


class Board:
    def __init__(self):
        super(Board, self).__init__()

    activeHole = None
    activePeg = None

   # def move(self, h):


    def update(self):
        pass


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
board = Board()

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

hole1.neighborOne.insert(0, hole2)
hole1.neighborOne.insert(1, hole3)
hole1.neighborTwo.insert(0, hole5)
hole1.neighborTwo.insert(1, hole8)

hole2.neighborOne.insert(0, hole3)
hole2.neighborOne.insert(1, hole4)
hole2.neighborTwo.insert(0, hole5)
hole2.neighborTwo.insert(1, hole9)

hole3.neighborOne.insert(0, hole2)
hole3.neighborOne.insert(1, hole1)
hole3.neighborTwo.insert(0, hole6)
hole3.neighborTwo.insert(1, hole8)

hole4.neighborOne.insert(0, hole3)
hole4.neighborOne.insert(1, hole2)
hole4.neighborTwo.insert(0, hole7)
hole4.neighborTwo.insert(1, hole9)

hole5.neighborOne.insert(0, hole6)
hole5.neighborOne.insert(1, hole7)
hole5.neighborTwo.insert(0, hole8)
hole5.neighborTwo.insert(1, hole10)

hole7.neighborOne.insert(0, hole6)
hole7.neighborOne.insert(1, hole5)
hole7.neighborTwo.insert(0, hole9)
hole7.neighborTwo.insert(1, hole10)

hole8.neighborOne.insert(0, hole5)
hole8.neighborOne.insert(1, hole1)
hole8.neighborTwo.insert(0, hole6)
hole8.neighborTwo.insert(1, hole3)

hole9.neighborOne.insert(0, hole6)
hole9.neighborOne.insert(1, hole2)
hole9.neighborTwo.insert(0, hole7)
hole9.neighborTwo.insert(1, hole4)

hole10.neighborOne.insert(0, hole8)
hole10.neighborOne.insert(1, hole5)
hole10.neighborTwo.insert(0, hole9)
hole10.neighborTwo.insert(1, hole7)

peg1 = Peg((99, 368))
pegs.add(peg1)
hole1.peg = peg1
peg2 = Peg((199, 368))
pegs.add(peg2)
hole2.peg = peg2
peg3 = Peg((299, 368))
pegs.add(peg3)
hole3.peg = peg3
peg4 = Peg((399, 368))
pegs.add(peg4)
hole4.peg = peg4
peg5 = Peg((149, 283))
pegs.add(peg5)
hole5.peg = peg5
peg6 = Peg((249, 283))
pegs.add(peg6)
hole6.peg = peg6
peg7 = Peg((349, 283))
pegs.add(peg7)
hole7.peg = peg7
peg8 = Peg((199, 198))
pegs.add(peg8)
hole8.peg = peg8
peg9 = Peg((299, 198))
pegs.add(peg9)
hole9.peg = None

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            for hole in holes:
                if (hole.rect.collidepoint(pos)) and (hole.peg is not None):
                    board.activePeg = hole.peg
                    print("active peg set")
                    board.activeHole = hole
        if event.type == pygame.MOUSEBUTTONUP:
            if board.activePeg is not None:
                pos = pygame.mouse.get_pos()
                for hole in holes:
                    if hole.rect.collidepoint(pos):
                        board.activePeg.rect.x = hole.rect.x
                        board.activePeg.rect.y = hole.rect.y
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