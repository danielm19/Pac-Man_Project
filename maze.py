#Stephanie Becerra, id: 888771284
#Ryan Chen, id: 888611449
#Daniel Moran, id: 888769718

import sys
import pygame as pg 
from node import Node
from pygame.locals import *
from settings import Settings
from vector import Vector
import gamefunctions as gf

class maze:
    def __init__(self, game, file, node):
        self.screen = game.screen
        self.walls = []
        
        with open(file) as f:
            contents = f.read()

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "0":
                        row.append(True)
                    else:
                        row.append(False)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        