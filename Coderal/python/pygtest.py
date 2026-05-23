import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo')

player = pygame.Rect((300, 250, 50, 50))

clock = pygame.time.Clock()

#game loop

run = True
while run:

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_UP] == True:
        player.move_ip(0, -1)

    # print(player.x, player.y)

    if player.x < 0:
        player.x = 0
    elif player.x > 750:
        player.x = 750

    if player.y < 0:
        player.y = 0
    elif player.y > 550:
        player.y = 550

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    # set frame rate
    clock.tick(120)

pygame.quit()

