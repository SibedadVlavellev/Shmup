import random

import pygame

import config
import sprites


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__set_image()
        self.__set_rect()
        self.speed_x = 20

    def __set_image(self):
        self.image = config.IMAGES['player_ship']

    def __set_rect(self):
        offset_y = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = config.SCREEN_WIDTH // 2
        self.rect.bottom = config.SCREEN_HEIGHT - offset_y

    def __set_position(self):
        keystate = pygame.key.get_pressed()

        a_is_pressed = keystate[pygame.K_a]
        d_is_pressed = keystate[pygame.K_d]

        if a_is_pressed and d_is_pressed:
            return
        
        # Calculating next position of the player
        if a_is_pressed:
            self.rect.x += self.speed_x * (-1)
        elif d_is_pressed:
            self.rect.x += self.speed_x
        
        # Cheking the position's validity
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        sprites.sprites.add(bullet)
        sprites.bullets.add(bullet)
       
    def update(self):
        self.__set_position()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
       super().__init__() 
       self.__set_image()
       self.__set_rect()
       self.__set_speed()

    def __set_image(self):
        self.image = config.IMAGES['meteor']

    def __set_rect(self):
        self.rect = self.image.get_rect()
        self.__set_position()

    def __set_position(self):
        x_min, x_max = 0, config.SCREEN_WIDTH - self.rect.width
        y_offset_min, y_offset_max = -80, -30
        self.rect.x = random.randint(x_min, x_max)
        self.rect.bottom = random.randint(y_offset_min, y_offset_max)

    def __set_speed(self):
        speed_y_min, speed_y_max = 3, 8
        self.speed_y = random.randint(speed_y_min, speed_y_max)
        speed_x_min, speed_x_max = -3, 3
        self.speed_x = random.randint(speed_x_min, speed_x_max)

    def update(self):
       self.rect.y += self.speed_y 
       self.rect.x += self.speed_x

       if (self.rect.top > config.SCREEN_HEIGHT
               or self.rect.right < 0
               or self.rect.left > config.SCREEN_WIDTH):
           self.__set_position()
           self.__set_speed()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, center_x, bottom):
        super().__init__()
        self.__set_image()
        self.__set_rect(center_x, bottom)
        self.speed_y = 15

    def __set_image(self):
        self.image = config.IMAGES['laser']

    def __set_rect(self, center_x, bottom):
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.bottom = bottom 

    def update(self):
        self.rect.y -= self.speed_y

        if self.rect.bottom < 0:
            self.kill()
