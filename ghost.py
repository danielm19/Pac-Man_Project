import pygame as pg
from pygame.locals import *
from vector import Vector
from settings import Settings
from character import Character

class Ghost(Character):
    def __init__(self, game, node):
        Character.__init__(self, game, node)
        self.points = 250

# need to create a function to calculate the movement
# need the update function and draw

    