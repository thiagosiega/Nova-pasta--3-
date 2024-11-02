import pygame

pygame.init()

# Set up the display
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
x = 50
y = 50
width = 40
height = 60
vel = 5

# Set up the game loop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()