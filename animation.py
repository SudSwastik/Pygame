import pygame,sys
from pygame.locals import *
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('animation')

white = (255,255,255)


catx = 10
caty = 10
catImg = pygame.image.load('ball.png')
dir = 'right'

while True:
    DISPLAYSURF.fill(white)
   

    if dir == 'right':
        catx += 5
        if catx == 280:
            dir == 'down'
    elif dir == 'down':
        caty += 5
        if caty == 220:
            dir == 'left'
    elif dir == 'left':
        catx -= 5
        if catx == 10:
            dir == 'up'
    elif dir == 'up':
        caty -= 5
        if caty == 10:
            dir = 'right'

    DISPLAYSURF.blit(catImg,(catx,caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
            
    
    
    
