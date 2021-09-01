import random
from collections import namedtuple

import pygame

import config
import sprites
import classes


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, 
                                      config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    clock = pygame.time.Clock()

    # Sprites
    player = classes.Player()
    sprites.sprites.add(player)
    
    spawn_mobs(count=8)

    # Game loop
    is_active = True
    while is_active:
        # Game input processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    player.shoot()

        # Game values calculation
        sprites.sprites.update()
        hits = pygame.sprite.spritecollide(player, 
                                           sprites.mobs, 
                                           False)
        is_active = not bool(hits)

        kills = pygame.sprite.groupcollide(sprites.bullets, 
                                           sprites.mobs, 
                                           True, True)
        spawn_mobs(count=len(kills))

        # Drawing results
        screen.fill(config.COLORS['grey'])
        sprites.sprites.draw(screen)
        pygame.display.flip()

        # Setting FPS
        clock.tick(config.FPS)

    pygame.quit()


def spawn_mobs(count):
    for _ in range(count):
        mob = classes.Mob()
        sprites.mobs.add(mob)
        sprites.sprites.add(mob)


if __name__ == '__main__':
    main()
