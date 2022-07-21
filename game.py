import pygame
pygame.init()

screen = pygame.display.set_mode((600, 500))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (200, 0, 0), (250, 250), 80)
    pygame.display.flip()

pygame.quit()