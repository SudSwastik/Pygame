import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50
change_x = 2
change_y = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    rect_x += change_x
    rect_y += change_y
    if rect_y > 350 or rect_y < 0:
        change_y = change_y * -1
    if rect_x > 750 or rect_x < 0:
        change_x = change_x * -1

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),[rect_x,rect_y,50,50])
    pygame.draw.rect(screen,(255,0,0),[rect_x+10,rect_y+10,30,30])
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
    

  
    
