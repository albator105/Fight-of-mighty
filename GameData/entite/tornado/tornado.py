import pygame
class Tornado(pygame.sprite.Sprite):
    def __init__(self,player,facing):
        super().__init__()
        self.player = player
        self.facing = facing
        self.image = pygame.image.load("GameData/entite/tornado/run/1.png")
        self.rect = self.image.get_rect()
        self.rect.y = self.player.rect.y-280
        self.rect.x = self.player.rect.x
        self.img = 1
        self.degat = 2
        self.speed = 10
    def remover(self):
        self.player.all_tornado.remove(self)

    def up_date(self):
        if self.facing == 1:
            self.rect.x += self.speed
            if self.rect.x == 1300:
                self.player.all_tornado.remove(self)
        if self.facing == 2:
            self.rect.x -= self.speed
            if self.rect.x == -100:
                self.player.all_tornado.remove(self)
        if self.img < 79:
            self.image=pygame.image.load("GameData/entite/tornado/run/"+str(self.img)+".png")
        if self.img > 78:
            for tornado in self.player.all_tornado:
                tornado.remover()
        self.img += 1
