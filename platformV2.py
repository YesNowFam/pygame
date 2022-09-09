import pygame
from random import randint
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.y_max = 500- self.rect.height
        self.x_max = 600 - self.rect.width
        self.rect.x = x
        self.rect.y = y
        self.vel = pygame.math.Vector2((0, 0))
        self.t = 0

    def update(self, keys):
        if keys[pygame.K_d]:
            self.rect.x += 5

        if keys[pygame.K_a]:
            self.rect.x += -5

        if keys[pygame.K_SPACE] and self.rect.y >= self.y_max:
            self.vel.y = 10

        self.vel.y += 0.25 * -9.81 * self.t
        print(f"position: {self.rect.y}")
        self.t += 1/60
        self.rect.x += self.vel.x
        self.rect.y -= self.vel.y

        if self.rect.x <= 0: self.rect.x = 0
        elif self.rect.x >= self.x_max: self.rect.x = self.x_max
        
        if self.rect.y >= self.y_max:
            self.rect.y = self.y_max
            self.vel.y = 0
            self.t = 0

image = pygame.image.load(r"C:\Users\ugail\Documents\pyg\player.png")
player = Player(image, 200, 200)

class Platform(pygame.Rect):
    def __init__(self, y):
        super().__init__(500, y, 100, 20)
        self.color = (255,0,255)
        self.t = 0

    def update(self, screen):
        self.x -= 2 #Move platform to the left 

        if self.x <= -(self.width + 100):
            self.x = 600

        pygame.draw.rect(screen, self.color, self)

plat = Platform(400)

all_group = pygame.sprite.Group()
all_group.add(player)


screen = pygame.display.set_mode((600, 500))
running = True

fps_clock = pygame.time.Clock()
fps = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys=pygame.key.get_pressed()

    screen.fill((255, 255, 255))
    all_group.update(keys)

    #Here
    if plat.colliderect(player.rect):
        if plat.left - player.rect.width <= player.rect.x <= plat.right + player.rect.width:
            if plat.top <= player.rect.bottom:
                player.y_max = plat.top - player.rect.height + 1
    else:
        player.y_max = 500 - player.rect.height

    all_group.draw(screen)
    plat.update(screen)

    pygame.display.flip()
    fps_clock.tick(fps)

pygame.quit()