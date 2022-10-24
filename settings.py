#Stephanie Becerra, id: 888771284
#Ryan Chen, id: 888611449
#

import pygame
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.tileWidth = 20
        self.tileHeight = 20
        self.rows = 36
        self.cols = 28
        self.screen_width = 570
        self.screen_height = 750
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 215, 0)
        self.red = (225, 5, 5)
        self.blue = (30, 145, 250)
        self.orange = (255, 145, 0)
        self.pink = (250, 100, 150)
        self.node_color = (225, 100, 100)
        #self.node_color = self.black
        self.bg = pygame.transform.rotozoom(pygame.image.load('images/pacmaze.png'), 0, 2.5)
        self.portal_value = 3
        self.small_dot = 1
        self.power_dot = 2
        self.ghost = 4
        
        
        self.yellow = (250, 250, 0)
        self.pacman_speed = 1