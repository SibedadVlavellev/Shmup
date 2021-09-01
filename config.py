import os

import pygame

FPS = 60
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'grey': (128, 128, 128),
    'yellow': (255, 255, 0),
    'lincoln_green': (38, 77, 0)
}

TITLE = "Shmup!"

DIRS = {}
DIRS['game'] = os.path.dirname(__file__)
DIRS['data'] = os.path.join(DIRS['game'], 'data')
DIRS['backgrounds'] = os.path.join(DIRS['data'], 'Backgrounds')
DIRS['png'] = os.path.join(DIRS['data'], 'PNG')
DIRS['enemies'] = os.path.join(DIRS['png'], 'Enemies')
DIRS['meteors'] = os.path.join(DIRS['png'], 'Meteors')
DIRS['lasers'] = os.path.join(DIRS['png'], 'Lasers')

FILES = {}
FILES['background'] = os.path.join(DIRS['backgrounds'], 'blue.png')
FILES['player_ship'] = os.path.join(DIRS['png'], 'playerShip1_green.png')
FILES['meteor'] = os.path.join(DIRS['meteors'], 'meteorBrown_big3.png')
FILES['laser'] = os.path.join(DIRS['lasers'], 'laserGreen06.png')

IMAGES = {
    name: pygame.image.load(FILES[name])
    for name in [
        'background',
        'laser',
        'player_ship',
        'meteor',
    ]
}

for image in IMAGES.values():
    image.set_colorkey(COLORS['black'])
