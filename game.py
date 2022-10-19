import pygame as pg
import sys
from settings import Settings
from button import Button
from pacman import Pacman
from node import Nodes
from pellet import PelletGroup
from ghost import Ghost
import gamefunctions as gf
from sound import Sound

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.size = self.settings.screen_width, self.settings.screen_height
        self.screen = pg.display.set_mode(size=self.size)
        pg.display.set_caption("PAC-MAN")
        self.dt = 2
        
        self.nodes = Nodes(self, 'maze.txt')
        self.nodes.set_portal_node_pair((0.5, 17), (27.5, 17))
        self.pellets = PelletGroup('maze.txt')
        self.sound = Sound()
        self.pacman = Pacman(self, self.nodes.getStartNode())
        self.ghost = Ghost(self, self.nodes.getRandom_node())
        
        
        self.play_button = Button(screen= self.screen, text= 'Play', x= self.size[0] // 2, y= self.size[1] - 100)
        
    def play(self):
        while True:
         self.screen.fill(self.settings.black)
         self.screen.blit(self.settings.bg, (0, 30))
         self.nodes.draw()
         gf.check_events()
         gf.check_pellets_eaten(pacman= self.pacman, pellets= self.pellets)
         self.pacman.update()
         self.ghost.update()
         self.ghost.draw(self.screen)
         self.pellets.update(self.dt)
         self.pellets.draw(self.screen)
         pg.display.flip()
         
            
    def reset(self):
        pass
        
        
    def start_screen(self):
        
        font = pg.font.SysFont('lexend', 96)
        text = font.render('PA      MAN', True, self.settings.white)
        text_rect = text.get_rect()
        text_rect.center = ((self.settings.screen_width // 2, self.settings.screen_height // 10))
        
        pac_image = pg.transform.rotozoom(pg.image.load('images/pac-man-title.png'), 0, 0.2)
        pac_image_rect = pac_image.get_rect()
        pac_image_rect.center = (((self.settings.screen_width // 2) - 40, self.settings.screen_height // 9))
        
        center_image = pg.transform.rotozoom(pg.image.load('images/pac-man-center.png'), 0, 0.5)
        center_image_rect = center_image.get_rect()
        center_image_rect.center = ((self.settings.screen_width // 2, self.settings.screen_height // 2))
        
        button_click = False
        
        while button_click == False:
            self.screen.fill(self.settings.black)
            self.screen.blit(text, text_rect)
            self.screen.blit(pac_image, pac_image_rect)
            self.screen.blit(center_image, center_image_rect)
            self.play_button.draw()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mousepos = pg.mouse.get_pos()
                    if self.play_button.rect.collidepoint(mousepos):
                        button_click = True
                        self.play() 
            pg.display.update()
            
    
def main():
    g = Game()
    g.start_screen()
    
if __name__ == '__main__':
    main()