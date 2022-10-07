import pygame
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 700
        self.screen_height = 900
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 215, 0)
        self.blue = (30, 145, 250)