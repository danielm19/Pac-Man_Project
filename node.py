import pygame as pg
from settings import Settings
from vector import Vector
import numpy
from random import randint



class Node:
    def __init__(self, game, x, y):
        self.screen = game.screen
        self.settings = Settings()
        self.pos = Vector(x, y) #vector to keep the position of the node 
        self.neighbors = { #dictionary to determine the neighbors of a single node
            'UP': None,
            'DOWN': None,
            'LEFT': None,
            'RIGHT': None,
            'PORTAL': None
        }
        
    def draw(self):
        for n in self.neighbors.keys():
            if self.neighbors[n] != None:
                line_start = self.pos.convert_tuple()
                line_end = self.neighbors[n].pos.convert_tuple()
                pg.draw.line(surface= self.screen, color= self.settings.green, start_pos= line_start, end_pos= line_end, width= 2)
                pg.draw.circle(surface= self.screen, color= self.settings.node_color, center=self.pos.convert_tuple_int(), radius= 10)

class Nodes:
    def __init__(self, game, maze):
        self.game = game
        self.maze = maze
        self.settings = Settings()
        self.nodes_dict = {} #dictionary containing all the nodes 
        self.node_symbols = ['+', 'P', 'n']
        self.path_symbols = ['.', '-', '|', 'p', '=']
        self.path_symbols_special = '=' 
        self.homekey = None
        maze_data = self.readMazeFile(maze)
        self.create_node_dict(maze_data)
        self.setup_horizontal_nodes(maze_data)
        self.setup_vertical_nodes(maze_data)
        
    def readMazeFile(self, file):
        #dtype U1 so file will not read data as float values 
        #returns a 2d array useful for creating the node dict
        return numpy.loadtxt(fname= file, dtype= '<U1')
    
    #creates node dict keys are x, y pos and value will be nodes
    def create_node_dict(self, mazedata, delta_x= 0.5, delta_y= 0):
        #loop through the file by rows and cols
        for row in list(range(mazedata.shape[0])):
            for col in list(range(mazedata.shape[1])):
                if mazedata[row][col] in self.node_symbols:
                    x, y = self.create_key(col + delta_x, row + delta_y)
                    self.nodes_dict[(x, y)] = Node(game= self.game, x= x, y= y)
                    
    def create_key(self, x, y):
        return x * self.settings.tileWidth, y * self.settings.tileHeight
    
    def setup_horizontal_nodes(self, mazedata, delta_x= 0.5, delta_y= 0):
        for row in list(range(mazedata.shape[0])):
            key = None
            for col in list(range(mazedata.shape[1])):
                if mazedata[row][col] in self.node_symbols:
                    if key == None:
                        key = self.create_key(x= col + delta_x, y= row + delta_y)
                    else:
                        other_key = self.create_key(x= col + delta_x, y= row + delta_y)
                        #makes the connection between left and right nodes on the screen
                        self.nodes_dict[key].neighbors['RIGHT'] = self.nodes_dict[other_key]
                        self.nodes_dict[other_key].neighbors['LEFT'] = self.nodes_dict[key]
                        key = other_key
                        
                elif mazedata[row][col] not in self.path_symbols:
                    key = None
                    
    def setup_vertical_nodes(self, mazedata, delta_x= 0.5, delta_y= 0):
        # instead ofr (i, j) it will be (j, i) eaiser to connect up and down nodes
        vert_maze_data = mazedata.transpose()
        for col in list(range(vert_maze_data.shape[0])):
            key = None
            for row in list(range(vert_maze_data.shape[1])):
                if vert_maze_data[col][row] in self.node_symbols:
                    if key == None:
                        key = self.create_key(x= col + delta_x, y= row + delta_y)
                    else:
                        other_key = self.create_key(x= col + delta_x , y= row + delta_y)
                        #make connection with nodes above and below each other 
                        self.nodes_dict[key].neighbors['DOWN'] = self.nodes_dict[other_key]
                        self.nodes_dict[other_key].neighbors['UP'] = self.nodes_dict[key]
                        key = other_key
                        
                elif vert_maze_data[col][row] not in self.path_symbols:
                    key = None
                    
    def createHomeNodes(self, delta_x= 0, delta_y= 0):
        homedata = numpy.array([['X','X','X','+','X','X','X','X'],
                                ['X','X','X','.','X','X','X','X'],
                                ['X','+','X','.','X','+','X','X'],
                                ['X','+','.','+','.','+','X','X'],
                                ['X','+','X','X','X','+','X','X']])

        self.create_node_dict(homedata, delta_x, delta_y)
        self.setup_horizontal_nodes(homedata, delta_x, delta_y)
        self.setup_vertical_nodes(homedata, delta_x, delta_y)
        self.homekey = self.create_key(delta_x + 2, delta_y)
        print(self.homekey)
        return self.homekey

    
    def connectHomeNodes(self, homekey, otherkey, direction):     
        key = self.create_key(*otherkey)
        self.nodes_dict[homekey].neighbors[direction] = self.nodes_dict[key]
        self.nodes_dict[key].neighbors[direction*-1] = self.nodes_dict[homekey]
        print(self.nodes_dict[homekey].pos)
        print(self.nodes_dict[key].pos)
    
    def getNodeFromPoint(self, xpoint, ypoint):
        if (xpoint, ypoint) in self.nodes_dict.keys():
            return self.nodes_dict[(xpoint, ypoint)]
        return None
    
    def getNodeFromTiles(self, row, col):
        x, y = self.create_key(x= col, y= row)
        if (x, y) in self.nodes_dict.keys():
            return self.nodes_dict[(x, y)]
        return None
    
    def getStartNode(self):
        nodes = list(self.nodes_dict.values())
        return nodes[0]
    
    def getRandom_node(self):
        nodes = list(self.nodes_dict.values())
        random_node = randint(0, len(nodes))
        return nodes[random_node]
    
    def set_portal_node_pair(self, npair1, npair2):
        first_key = self.create_key(*npair1)
        second_key = self.create_key(*npair2)
        
        #check if both points of the portal are in the dict
        if first_key in self.nodes_dict.keys() and second_key in self.nodes_dict.keys():
            #connect the two protals in the dictionary
            self.nodes_dict[first_key].neighbors['PORTAL'] = self.nodes_dict[second_key]
            self.nodes_dict[second_key].neighbors['PORTAL'] = self.nodes_dict[first_key]
        
    def draw(self):
        for node in self.nodes_dict.values():
            node.draw()