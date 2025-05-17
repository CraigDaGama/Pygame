import pygame

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Simple object movement')
clock = pygame.time.Clock()
running = True

# delta time
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running : 
    # poll for events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    
    screen.fill("silver")

    pygame.draw.circle(screen, "blue", player_pos, 40)

    # movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 *dt
    if keys[pygame.K_DOWN]:
         player_pos.y += 300 *dt
    if keys[pygame.K_LEFT]:
         player_pos.x -= 300 *dt
    if keys[pygame.K_RIGHT]:
         player_pos.x += 300 *dt

    pygame.display.flip()

    # framerate independent physics
    dt = clock.tick(60) / 1000

pygame.quit()