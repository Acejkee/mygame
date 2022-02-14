import pygame

pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("My first game :)")

pygame.draw.rect(sc, (255, 255, 255), (10, 10, 50, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()