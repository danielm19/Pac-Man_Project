#Stephanie Becerra, id: 888771284
#Ryan Chen, id: 888611449
#Daniel Moran, id: 888769718

import pygame
from vector import Vector
from settings import Settings
import numpy 

class Pellet:
    def __init__(self, row, column):
        self.settings = Settings()
        self.position = Vector(column*self.settings.tileWidth, row*self.settings.tileHeight)
        self.color = self.settings.white
        self.radius = int(4 * self.settings.tileWidth / 16)
        self.collideRadius = int(4 * self.settings.tileWidth / 16)
        self.points = 25
        self.visible = True
        
    def draw(self, screen):
        if self.visible:
            pos = self.position.convert_tuple_int()
            pygame.draw.circle(screen, self.color, pos, self.radius)
            

class PowerPellet(Pellet):
    def __init__(self, row, column):
        Pellet.__init__(self, row , column + 0.5)
        self.radius = int(8 * self.settings.tileWidth / 16)
        self.points = 50
        self.flashTime = 100
        self.timer= 0
        
    def update(self, dt):
        self.timer += dt
        if self.timer >= self.flashTime:
            self.visible = not self.visible
            self.timer = 0    
            
class PelletGroup:
    def __init__(self, pfile):
        self.pellet_list = []
        self.powerpellets = []
        self.createPelletList(pfile)
        self.pellets_eaten = 0

    def update(self, dt):
        for powerpellet in self.powerpellets:
            powerpellet.update(dt)
                
    def createPelletList(self, pfile):
        data = self.readPelletfile(pfile)        
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                if data[row][col] in ['.', '+']:
                    self.pellet_list.append(Pellet(row, col + 0.5))
                elif data[row][col] in ['P', 'p']:
                    powerp = PowerPellet(row, col)
                    self.pellet_list.append(powerp)
                    self.powerpellets.append(powerp)
                    
    def readPelletfile(self, txtfile):
        return numpy.loadtxt(txtfile, dtype='<U1')
    
    def isEmpty(self):
        if len(self.pellet_list) == 0:
            return True
        return False
    
    def draw(self, screen):
        for pellet in self.pellet_list:
            pellet.draw(screen)
    
    
        