import pygame
from random import *

class Ball:
    def __init__(self, window, wigth, heigth):
        pygame.init()
        # Инициализируем 
        self.window = window # экран
        self.wigth = wigth # Длину
        self.heigth = heigth # Ширину

        # Атрибуты круга
        self.x = randrange(40, (self.wigth - 80))
        self.y = randrange(40, (self.heigth - 80))

        variable_speed = [-4, -2, 2, 4]

        self.speed_x = choice(variable_speed)
        self.speed_y = choice(variable_speed)

        self.boom = pygame.mixer.Sound("VolumeBall/Ball_BUm.mp3")

    def circle_position_update(self):
        # Отслеживаем кординаты
        # Если коснулся края, то меняем направление
        if (self.x < 40) or (self.x > (self.wigth - 40)):
            self.speed_x *= -1
            self.boom.play()
        if (self.y < 40) or (self.y > (self.heigth - 40)):
            self.speed_y *= -1
            self.boom.play()
        
        # Меняем значение кординат
        self.x += self.speed_x
        self.y += self.speed_y
        
    
    def update(self):
        # Отображаем на экране
        pygame.draw.circle(self.window, "White", (self.x, self.y), 40)