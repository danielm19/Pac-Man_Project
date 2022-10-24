#Stephanie Becerra, id: 888771284
#Ryan Chen, id: 888611449
#

import sys 
import pygame as pg 
from vector import Vector

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            
def check_pellets_eaten(pacman, pellets):
    pellet = pacman.eat_pellets(pellets.pellet_list)
    if pellet is not None:
        pellets.pellets_eaten += 1
        pellets.pellet_list.remove(pellet)