#Stephanie Becerra, id: 888771284
#Ryan Chen, id: 888611449
#Daniel Moran, id: 888769718

import pygame as pg
from pygame.locals import *
from vector import Vector
from settings import Settings
from random import randint

class Character:
    def __init__(self, game, node):
        self.settings = game.settings
        self.name = None
        self.goal = None
        self.directions = {
                'STOP': Vector(),
                'UP': Vector(0, -1),
                'DOWN': Vector(0, 1),
                'LEFT': Vector(-1, 0),
                'RIGHT': Vector(1, 0)
        }
        self.direction = 'STOP'
        self.radius = 12
        self.collide_radius = 4
        self.position = Vector()
        self.node = node
        self.set_pos()
        self.targetNode = node
        self.visible = True
        self.disablePortal = False
        
    #sets a character position to a node on the map 
    def set_pos(self):
        self.position = self.node.pos.copy()
    
    #checks to see if the direction is valid by checking the directions dict 
    def valid_direction(self, direction):
        if direction != 'STOP':
            if self.node.neighbors[direction] != None:
                return True
        return False
    
    def movetoNewNode(self, direction):
        if self.valid_direction(direction):
            return self.node.neighbors[direction]
        return self.node
    
    def moved_passed_node(self):
        if self.targetNode != None:
            v1 = self.targetNode.pos - self.node.pos
            v2 = self.position - self.node.pos
            node_to_target_node = v1.mag_sq()
            node_to_current_node = v2.mag_sq()
            return node_to_current_node >= node_to_target_node
        return False
    
    #reverses the direction of pacman 
    def reverse_direction(self):
        self.direction *= -1
        temp_node = self.node
        self.node = self.targetNode
        self.targetNode = temp_node
    
    #check if input direction is the opposite of pacman's current direction
    def oppositeDirection(self, direction):
        if direction != 'STOP':
            if direction == self.direction * -1:
                return True
        return False
    
    def setSpeed(self, speed):
        self.speed = speed * self.settings.tileWidth / 16
        
    def validDirections(self):
        directions = []
        for key in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            if self.valid_direction(key):
                if key != self.direction * -1:
                    directions.append(key)
        if len(directions) == 0:
            directions.append(self.direction * -1)
        return directions
    
    def randomDirection(self, directions):
        return directions[randint(0, len(directions)-1)]
    
    def update(self):
        self.position += self.directions[self.direction] * self.settings.pacman_speed
         
        if self.moved_passed_node():
            self.node = self.targetNode
            directions = self.validDirections()
            direction = self.randomDirection(directions)   
            if not self.disablePortal:
                if self.node.neighbors['PORTAL'] is not None:
                    self.node = self.node.neighbors['PORTAL']
            self.targetNode = self.movetoNewNode(direction)
            if self.targetNode != self.node:
                self.direction = direction
            else:
                self.targetNode = self.movetoNewNode(self.direction)

            self.set_pos()
        
    def draw(self, screen, color):
        pos = self.position.convert_tuple_int()
        pg.draw.circle(screen, color, pos, self.radius)