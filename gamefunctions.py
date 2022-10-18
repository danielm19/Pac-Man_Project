import sys 
import pygame as pg 
from vector import Vector

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()