import pygame

import config


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__set_image()
        self.__set_rect()
        self.speed_x = 20

    def __set_image(self):
        width, height = 70, 50
        self.image = pygame.surface.Surface((width, height))
        self.image.fill(config.COLORS['lincoln_green'])

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
       
    def update(self):
        self.__set_position()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def __set_image(self):
        pass

    def __set_rect(self):
        pass

    def __set_position(self):
        pass

    def update(self):
        pass
