from Ball import *
import pygame
import sys

# Инициализируем и создаём окно pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Just it Ball")

clock = pygame.time.Clock()

# Создаём Объект(Указываем кол-во кружков)
Spisok = []
for i in range(5):
    oBall = Ball(screen, WIDTH, HEIGHT)
    Spisok.append(oBall)

while True:

    screen.fill("Black")

    for oBall in Spisok:
        oBall.circle_position_update()
        oBall.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)