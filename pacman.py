import pygame as pg 
from pygame.locals import *
from settings import Settings
from vector import Vector
import gamefunctions as gf

class Pacman:
    def __init__(self, game, node):
        self.settings = Settings()
        self.screen = game.screen
        self.position = Vector()
        self.radius = 15
        self.color = self.settings.yellow
        self.node = node
        self.directions = {
                'STOP': Vector(),
                'UP': Vector(0, -1),
                'DOWN': Vector(0, 1),
                'LEFT': Vector(-1, 0),
                'RIGHT': Vector(1, 0)
        }
        self.direction = 'STOP'
        self.targetNode = node
        self.set_pos()
        
    def set_pos(self):
        self.position = self.node.pos.copy()
    
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
        tempNode = self.node
        self.node = self.targetNode
        self.targetNode = node 
    
    #check if input direction is the opposite of pacman's current direction
    def move_opposite_direction(self, direction):
        if self.direction != 'STOP':
            if self.direction == self.direction * -1:
                return True
        return False
    
    def update(self):
        self.position += self.directions[self.direction] * self.settings.pacman_speed
        direction = self.get_keys()
        #self.direction = direction 
        #self.node = self.movetoNewNode(direction) #moves to next node
        #self.set_pos() #set pacman pos to new node pos
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
            if self.move_opposite_direction(direction):
                self.reverse_direction()
                
        self.draw()
        
    def draw(self):
        pman = pg.draw.circle(self.screen, self.color, (self.position.x, self.position.y), self.radius)