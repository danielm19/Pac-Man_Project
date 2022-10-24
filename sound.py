#Stephanie Becerra, id: 888771284
#Ryan Chen, id: 888611449
#Daniel Moran, id: 888769718

import pygame as pg
import time

class Sound:
    def __init__(self):
        pg.mixer.init()
        self.playerMovement_sound =  pg.mixer.Sound('sounds/Wakawaka.mp3')
        self.gameover_sound = pg.mixer.Sound('sounds/Pac-Man dying sound effects.mp3')
        self.ghostMovement_sound = pg.mixer.Sound('sounds/Ghost sound.mp3')
        self.blueghost_sound = pg.mixer.Sound('sounds/Ghost sound.mp3')
        self.eye_sound = pg.mixer.Sound('sounds/Ghost to base.mp3')
        self.ghost = {'ghost': self.ghostMovement_sound, 'blue': self.blueghost_sound, 'eye': self.eye_sound}

    #hopeing to switch between all the ghost sounds stored in a dictunary how ever I will make other functions for each sound to allow -
    #another way to do the same thing if I can't figure out the problem 
    def play_ghost_sounds(self):
        #for temp reason will make it only play the ghost movement
        sound = pg.mixer.Sound.get_num_channels(self.ghost['ghost'])
        if sound < 1 :
            pg.mixer.Sound.play(self.ghost['ghost'])

    def stop_ghost_sounds(self):
        sound = pg.mixer.Sound.get_num_channels(self.ghost['ghost'])
        if sound < 1 :
            pg.mixer.Sound.stop(self.ghost['ghost'])

    def play_player_sound(self):
        sound = pg.mixer.Sound.get_num_channels(self.playerMovement_sound)
        if sound < 1 :
            pg.mixer.Sound.play(self.playerMovement_sound)

    def stop_player_sound(self):
        sound = pg.mixer.Sound.get_num_channels(self.playerMovement_sound)
        if sound < 1 :
            pg.mixer.Sound.stop(self.playerMovement_sound)
        