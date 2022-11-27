import pygame
class earthquake(pygame.sprite.Sprite):
    def __init__(self,player,pos_player_x,pos_player_y,facing):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("GameData/entite/earthquake/1_left.png")
        self.rect = self.image.get_rect()
        self.rect.y = pos_player_y - 25
        self.facing = facing
        if self.facing == 1:
            self.rect.x = pos_player_x
        elif self.facing == 2:
            self.rect.x = pos_player_x-416
        self.img = 1
        self.degat = 8
    def remover(self):
        self.player.all_earthquake.remove(self)

    def up_date(self):
        if self.facing == 1:
            self.image=pygame.image.load("GameData/entite/earthquake/"+str(self.img)+"_right.png")
        if self.facing == 2:
            self.image=pygame.image.load("GameData/entite/earthquake/"+str(self.img)+"_left.png")
        self.img += 1
        if self.img == 13:
            for earthquake in self.player.all_earthquake:
                earthquake.remover()