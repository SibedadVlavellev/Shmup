import random
from collections import namedtuple

import pygame

import config
import classes
import sprites


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, 
                                      config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    clock = pygame.time.Clock()

    # Game loop
    is_active = True
    while is_active:
        # Game input processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False

        # Game values calculation
        sprites.sprites.update()
        hits = pygame.sprite.spritecollide(sprites.player, 
                                           sprites.mobs, 
                                           dokill=False)
        if hits:
            is_active = False

        # Drawing results
        screen.fill(config.COLORS['grey'])
        sprites.sprites.draw(screen)
        pygame.display.flip()

        # Setting FPS
        clock.tick(config.FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
