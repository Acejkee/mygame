import pygame
from ball import Ball
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

BLACK = (0, 0, 0)

W, H = 1200, 580
sc = pygame.display.set_mode((W, H))

bg = pygame.image.load('C:\\Users\\belou\Desktop\\images\\back1.jpg').convert()

clock = pygame.time.Clock()
FPS = 60

balls_images = ['ball_bear.png', 'ball_fox.png', 'ball_panda.png']
balls_surf = [pygame.image.load('C:\\Users\\belou\Desktop\\images\\' + path).convert_alpha() for path in balls_images]

balls = pygame.sprite.Group()

def createBall(group):
    indx = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], group)


createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    sc.blit(bg, (0, 0))
    balls.draw(sc)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)
