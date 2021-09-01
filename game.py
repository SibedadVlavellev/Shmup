import random
from collections import namedtuple

import pygame

import config
import classes


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, 
                                      config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    clock = pygame.time.Clock()

    # Creation of sprites
    player = classes.Player()
    all_sprites = pygame.sprite.Group(player)

    # Game loop
    is_active = True
    while is_active:
        # Game input processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False

        # Game values calculation
        all_sprites.update()

        # Drawing results
        screen.fill(config.COLORS['grey'])
        all_sprites.draw(screen)
        pygame.display.flip()

        # Setting FPS
        clock.tick(config.FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
