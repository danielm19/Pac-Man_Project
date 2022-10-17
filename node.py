import pygame as pg
from settings import Settings
from vector import Vector



class Node:
    def __init__(self, game, x, y):
        self.screen = game.screen
        self.settings = Settings()
        self.pos = Vector(x, y) #vector to keep the position of the node 
        self.neighbors = { #dictionary to determine the neighbors of a single node
            'UP': None,
            'DOWN': None,
            'LEFT': None,
            'RIGHT': None
        }
        
    def draw(self):
        for n in self.neighbors.keys():
            if self.neighbors[n] != None:
                line_start = self.pos.convert_tuple()
                line_end = self.neighbors[n].pos.convert_tuple()
                pg.draw.line(surface= self.screen, color= self.settings.blue, start_pos= line_start, end_pos= line_end, width= 2)
                pg.draw.circle(surface= self.screen, color= self.settings.node_color, center=self.pos.convert_tuple_int(), radius= 10)

class Nodes:
    def __init__(self, game):
        self.node_list = []
        self.game = game
        
    def test_nodes(self):
        nodeA = Node(game= self.game, x= 80, y= 80)
        nodeB = Node(game= self.game, x= 160, y= 80)
        nodeC = Node(game= self.game, x= 80, y= 160)
        nodeD = Node(game= self.game, x= 160, y= 160)
        nodeE = Node(game= self.game, x= 208, y= 160)
        nodeF = Node(game= self.game, x= 80, y= 320)
        nodeG = Node(game= self.game, x= 208, y= 320)
        
        nodeA.neighbors['RIGHT'] = nodeB
        nodeA.neighbors['DOWN'] = nodeC
        nodeB.neighbors['LEFT'] = nodeA
        nodeB.neighbors['DOWN'] = nodeD
        nodeC.neighbors['UP'] = nodeA
        nodeC.neighbors['RIGHT'] = nodeD
        nodeC.neighbors['DOWN'] = nodeF
        nodeD.neighbors['UP'] = nodeB
        nodeD.neighbors['LEFT'] = nodeC
        nodeD.neighbors['RIGHT'] = nodeE
        nodeE.neighbors['LEFT'] = nodeD
        nodeE.neighbors['DOWN'] = nodeG
        nodeF.neighbors['UP'] = nodeC
        nodeF.neighbors['RIGHT'] = nodeG
        nodeG.neighbors['UP'] = nodeE
        nodeG.neighbors['LEFT'] = nodeF
        
        self.node_list = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]
        
    def draw(self):
        for node in self.node_list:
            node.draw()