import pygame as pg 
from pygame.locals import *
from settings import Settings
from vector import Vector
import gamefunctions as gf
from character import Character

class Pacman(Character):
    def __init__(self, game, node):
        Character.__init__(self, game, node)
        self.settings = Settings()
        self.screen = game.screen
        self.color = self.settings.yellow
        
    def eat_pellets(self, pelletlist):
        for pellet in pelletlist:
            distance = self.position - pellet.position
            distance_squared = distance.mag_sq()
            radius_squared = (pellet.radius + self.collide_radius) ** 2
            if distance_squared <= radius_squared:
                return pellet
        return None
        
    
    def get_keys(self):
        key_input = pg.key.get_pressed()
        
        if key_input[pg.K_UP]:
            return 'UP'
        if key_input[pg.K_DOWN]:
            return 'DOWN'
        if key_input[pg.K_LEFT]:
            return 'LEFT'
        if key_input[pg.K_RIGHT]:
            return 'RIGHT'
        return 'STOP'
    
    def update(self):
        self.position += self.directions[self.direction] * self.settings.pacman_speed
        direction = self.get_keys()
        if self.moved_passed_node():
            self.node = self.targetNode
            if self.node.neighbors['PORTAL'] is not None:
                self.node = self.node.neighbors['PORTAL']
                
            self.targetNode = self.movetoNewNode(direction)
            
            if self.targetNode != self.node:
                self.direction = direction
            else:
                self.targetNode = self.movetoNewNode(direction)
                
            if self.targetNode == self.node:
                self.direction = 'STOP'
            self.set_pos()
        else:
            if self.oppositeDirection(direction):
                self.reverse_direction()
                
        self.draw()
        
    def draw(self):
        pman = pg.draw.circle(self.screen, self.color, (self.position.x, self.position.y), self.radius)