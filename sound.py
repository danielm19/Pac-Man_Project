import pygame as pg
import time

class Sound:
    def __init__(self):
        pg.mixer.init()
        playerMovement_sound =  pg.mixer.Sound('sounds/Wakawaka.mp3')
        gameover_sound = pg.mixer.Sound('sounds/Pac-Man dying sound effects.mp3')
        ghostMovement_sound = pg.mixer.Sound('sounds/Ghost sound.mp3')
        blueghost_sound = pg.mixer.Sound('sounds/Ghost sound.mp3')
        eye_sound = pg.mixer.Sound('sounds/Ghost to base.mp3')
        self.ghost = {'ghost': ghostMovement_sound, 'blue': blueghost_sound, 'eye': eye_sound}

    def play_ghost_sounds(self):
        #for temp reason will make it only play the ghost movement
        pg.mixer.Sound.play(self.ghost['ghost'])

        