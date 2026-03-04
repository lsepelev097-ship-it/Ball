from Ball import *
import pygame
import sys

# Инициализируем и создаём окно pygame
pygame.init()

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Just it Ball")

clock = pygame.time.Clock()

display_color = "Black"
ConditionGame = "Base"

# Загружаем фото и звук скримера 
scrimer = pygame.transform.scale(pygame.image.load("Scrimer/scrimer.jpg"), (WIDTH, HEIGHT))
scrimer_volume = pygame.mixer.Sound("Scrimer/scrimer_volume.mp3")

# Создаём звук дня выключателя света
clac = pygame.mixer.Sound("Svet_on_off/on_off.mp3")
color_next = 0 # Если число чётно двум, то мы будем окрашивать в белый цвет, иначе в чёрный(Экран)

# Создаём Объект(Указываем кол-во кружков)
Spisok = []
for i in range(20):
    oBall = Ball(screen, WIDTH, HEIGHT, "White")
    Spisok.append(oBall)

while True:

    if ConditionGame == "Base":

        screen.fill(display_color)

        for oBall in Spisok:
            oBall.circle_position_update()
            oBall.update()

        mouse = pygame.mouse.get_pos()
        for oblect in Spisok:
            if oblect.rect.collidepoint(mouse):
                ConditionGame = "Game_Over"
                scrimer_volume.play()
    
    elif ConditionGame == "Game_Over":
        screen.blit(scrimer, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            clac.play() # Издаём звук выключателя
            if color_next % 2 == 0:
                display_color = "White"
                for object in Spisok:
                    object.color = "Black"
            else:
                display_color = "Black"
                for object in Spisok:
                    object.color = "White"
            color_next += 1
                   
    pygame.display.update()
    clock.tick(60)