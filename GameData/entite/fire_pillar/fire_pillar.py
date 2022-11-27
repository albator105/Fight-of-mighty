import pygame
class fire_pillar(pygame.sprite.Sprite):
    def __init__(self,player,facing):
        super().__init__()
        self.player = player
        self.facing = facing
        self.image = pygame.image.load("GameData/entite/fire_pillar/1.png")
        self.rect = self.image.get_rect()
        self.rect.y = self.player.rect.y - 150
        if self.facing == 1:
            self.rect.x = self.player.rect.x
        elif self.facing == 2:
            self.rect.x = self.player.rect.x-100
        self.img = 1
        self.degat = 5
    def remover(self):
        self.player.all_fire_pillar.remove(self)

    def up_date(self):
        self.image=pygame.image.load("GameData/entite/fire_pillar/"+str(self.img)+".png")
        self.img += 1
        if self.img == 18:
            for fire_pillar in self.player.all_fire_pillar:
                fire_pillar.remover()