import random

import pygame

from game_classes import Player


def main():
    # Constants
    FPS = 60
    RESOLUTION = {
        'width': 1600,
        'height': 900
    }
    COLORS = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'grey': (128, 128, 128),
        'yellow': (255, 255, 0),
    }
    
    # Basic settings
    pygame.init()
    screen = pygame.display.set_mode((RESOLUTION['width'], 
                                      RESOLUTION['height']))
    pygame.display.set_caption('Shmup!')
    clock = pygame.time.Clock()

    # Creation of sprites

    # Game loop
    is_active = True
    while is_active:
        # Game input processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False

        # Game values calculation

        # Drawing results
        screen.fill(COLORS['grey'])
        pygame.display.flip()

        # Setting FPS
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
