import sys 
import pygame as pg 
from vector import Vector

movement = {
    pg.K_UP: Vector(0, -1),
    pg.K_DOWN: Vector(0, 1),
    pg.K_LEFT: Vector(-1, 0),
    pg.K_RIGHT: Vector(1, 0)
}

def check_keydown_events(event, settings, pacman):
    key = event.key
    
    if key in movement.keys():
        pacman.vel += settings.pacman_speed * movement[key]
        
def check_keyup_events(event, pacman):
    key = event.key
    
    if key in movement.keys():
        pacman.vel = Vector()

def check_events(settings, pacman):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event = event, settings = settings, pacman = pacman)
        elif event.type == pg.KEYUP:
            check_keyup_events(event= event, pacman= pacman)