import pygame


pygame.init()
speed = [1, 1]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_COLOR = (255, 100, 80)
# pygame.time.Clock().tick(fps)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((350, 580, 100, 20))
ball = pygame.image.load("img/ball.png")
ballrect = ball.get_rect()
ballrect.x, ballrect.y = 370, 525

wall = []
start_width = 1
start_height = 2
for i in range(3):
    tile_line = []
    for _ in range(20):
        tile = pygame.Rect((start_width, start_height, 38, 38))
        tile_line.append(tile)
        start_width += 40
    start_width = 1
    start_height += 40
    wall.append(tile_line)

run = True
while run:

    screen.fill((90, 90, 200))

    #  Shape drawing
    pygame.draw.rect(screen, (0, 200, 90), player)
    pygame.draw.rect(screen, (240, 25, 100), ballrect, border_radius=20)
    for tile_line in wall:
        for tile in tile_line:
            pygame.draw.rect(screen, TILE_COLOR, tile, border_radius=5)
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and player.x >= 0:
        player.move_ip(-2, 0)
    elif key[pygame.K_RIGHT] and player.x <= SCREEN_WIDTH - 100:
        player.move_ip(2, 0)
    # if key[pygame.K_UP] and player.y >= 0:
    #     player.move_ip(0, -1)
    # if key[pygame.K_DOWN] and player.y <= SCREEN_HEIGHT - 20:
    #     player.move_ip(0, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > SCREEN_WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > SCREEN_HEIGHT:
        speed[1] = -speed[1]

    if ballrect.colliderect(player):
        speed[1] = -speed[1]
    for tile_line in wall:
        for tile in tile_line:
            if ballrect.colliderect(tile):
                speed[1] = -speed[1]

    screen.blit(ball, ballrect)
    pygame.display.flip()
    # pygame.display.update()


pygame.quit()
