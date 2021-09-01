import pygame

import classes


sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = classes.Player()
sprites.add(player)

mob_count = 8
for _ in range(mob_count):
    mob = classes.Mob()
    sprites.add(mob)
    mobs.add(mob)
