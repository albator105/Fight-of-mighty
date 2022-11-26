import pygame
class ice_spike(pygame.sprite.Sprite):
    def __init__(self,player,pos_player_x,pos_player_y,facing):
        super().__init__()
        self.player = player
        self.facing = facing
        self.image = pygame.image.load("GameData/entite/ice_spike/1.png")
        self.rect = self.image.get_rect()
        self.rect.y = pos_player_y - 200
        if self.facing == 1:
            self.rect.x = pos_player_x - 80
        elif self.facing == 2:
            self.rect.x = pos_player_x-216
        self.img = 1
        self.degat = 2
    def remover(self):
        self.player.all_ice_spike.remove(self)

    def up_date(self):
        self.image=pygame.image.load("GameData/entite/ice_spike/"+str(self.img)+".png")
        self.img += 1
        if self.img == 16:
            for ice_spike in self.player.all_ice_spike:
                ice_spike.remover()