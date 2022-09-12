# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame.locals import *


class Peg(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Peg, self).__init__()
        self.image = pygame.image.load('ycircle.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Create sprites
sgroup = pygame.sprite.RenderPlain()
peg1 = Peg((99, 368))
sgroup.add(peg1)
peg2 = Peg((199, 368))
sgroup.add(peg2)
peg3 = Peg((299, 368))
sgroup.add(peg3)
peg4 = Peg((399, 368))
sgroup.add(peg4)
peg5 = Peg((149, 283))
sgroup.add(peg5)
peg6 = Peg((249, 283))
sgroup.add(peg6)
peg7 = Peg((349, 283))
sgroup.add(peg7)
peg8 = Peg((199, 198))
sgroup.add(peg8)
peg9 = Peg((299, 198))
sgroup.add(peg9)

activePeg = Peg((0, 0))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for peg in sgroup:
                if peg.rect.collidepoint(pos):
                    activePeg = peg

    screen.fill((255, 255, 255))

    pygame.draw.polygon(screen, 'brown', [(25, 400), (475,400), (250, 50)])

    pygame.draw.circle(screen, 'black', (100, 370), 20)
    pygame.draw.circle(screen, 'black', (200, 370), 20)
    pygame.draw.circle(screen, 'black', (300, 370), 20)
    pygame.draw.circle(screen, 'black', (400, 370), 20)
    pygame.draw.circle(screen, 'black', (150, 285), 20)
    pygame.draw.circle(screen, 'black', (250, 285), 20)
    pygame.draw.circle(screen, 'black', (350, 285), 20)
    pygame.draw.circle(screen, 'black', (200, 200), 20)
    pygame.draw.circle(screen, 'black', (300, 200), 20)
    pygame.draw.circle(screen, 'black', (250, 125), 20)

    sgroup.draw(screen)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()