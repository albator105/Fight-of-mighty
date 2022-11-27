import pygame,sys
from random import randint
from GameData.entite.player.player import Player
from GameData.entite.gobelin.gobelin import Gobelin
from GameData.entite.dark_player.dark_player import dark_player
class Game():
    def __init__(self):
        self.player = Player(self)
        self.all_playeur = pygame.sprite.Group()
        self.gobelin = Gobelin(self,1)
        self.all_gobelin = pygame.sprite.Group()
        self.dark_player = dark_player(self)
        self.all_dark_playeur = pygame.sprite.Group()
        self.pressed = {}
    
    def spawn_gobelin(self,min_lv,max_lv):
        self.all_gobelin.add(Gobelin(self,randint(min_lv,max_lv)))
    def spawn_dark_player(self):
        self.all_dark_playeur.add(dark_player(self))
    
    def remove_ennemie(self):
        for gobelin in self.all_gobelin:
            gobelin.remover()
        for dark_playeur in self.all_dark_playeur:
            dark_playeur.remover()
    def Touche(self, facing):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

    def all_remove(self):
        for tornado in self.player.all_tornado:
            tornado.remover()
        for earthquake in self.player.all_earthquake:
            earthquake.remover()
        for ice_spike in self.player.all_ice_spike:
            ice_spike.remover()

