import pygame as pg 
from pygame.locals import *
from settings import Settings
from vector import Vector

class Pacman(object):
    def __init__(self, game):
        self.settings = Settings()
        self.screen = game.screen
        self.position = Vector(350, 600)
        self.vel = Vector()
        self.radius = 15
        self.color = self.settings.yellow
        
    def update(self):
        self.position += self.vel
        self.draw()
        
    def draw(self):
        pman = pg.draw.circle(self.screen, self.color, (self.position.x, self.position.y), self.radius)