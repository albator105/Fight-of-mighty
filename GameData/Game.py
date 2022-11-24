import pygame,sys
from random import randint
from GameData.entite.player.player import Player
from GameData.entite.gobelin.gobelin import Gobelin
class Game():
    def __init__(self):
        self.player = Player(self)
        self.all_playeur = pygame.sprite.Group()
        self.gobelin = Gobelin(self,1)
        self.all_gobelin = pygame.sprite.Group()
        self.pressed = {}
    
    def spawn_gobelin(self,min_lv,max_lv):
        self.all_gobelin.add(Gobelin(self,randint(min_lv,max_lv)))
    
    def remove_ennemie(self):
        for gobelin in self.all_gobelin:
            gobelin.remover()
    def Touche(self, facing):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

