import pygame

pygame.init()

W, H = 600, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("My first game :)")

FPS = 60
clock = pygame.time.Clock()
x = W // 2
y = H // 2
speed = 5
move = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and event.mod == pygame.KMOD_LCTRL:
                move = -speed
            elif event.key == pygame.K_RIGHT and event.mod == pygame.KMOD_LCTRL:
                move = speed
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                move = 0
    x += move

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)
