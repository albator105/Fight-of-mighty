import pygame
from random import randint
class Gobelin(pygame.sprite.Sprite):
    def __init__(self,game,niveau):
        super().__init__()
        self.level = niveau
        self.game = game
        self.image = pygame.image.load("GameData/entite/gobelin/run/1_left.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(1000,2000)
        self.rect.y = 620
        self.viemax = 50*niveau
        self.vie = self.viemax
        self.force = 3*niveau
        self.vitesse = randint(5,10)
        self.facing = 2
        self.img = 0
        self.attack = 0
        self.xp = 10
    def damage(self,amount):
        self.vie -= amount
        if self.vie <= 0:
            self.game.player.xp += self.xp*self.level
            self.remover()
    def remover(self):
        self.game.all_gobelin.remove(self)

    def update_health_barre(self, surface):
        lvl = pygame.font.Font("tool/police/font.ttf", 20).render(str(self.level), True, (223, 255, 0))
        surface.blit(lvl, (self.rect.x+20, self.rect.y-40))
        position_barre_2 = [self.rect.x, self.rect.y-20, self.vie / self.viemax * 50, 5]
        position_barre = [self.rect.x, self.rect.y-20, self.viemax / self.viemax * 50, 5]
        pygame.draw.rect(surface, (60, 63, 60), position_barre)
        pygame.draw.rect(surface, (111, 210, 46), position_barre_2)
        
    def deplacement_general(self,player_position):
        if pygame.sprite.spritecollide(self, self.game.player.all_earthquake, False):
            self.damage(self.game.player.earth_quake.degat)
        if pygame.sprite.spritecollide(self, self.game.player.all_fire_pillar, False):
            self.damage(self.game.player.fire_pillar.degat)
        if pygame.sprite.spritecollide(self, self.game.player.all_ice_spike, False):
            self.damage(self.game.player.ice_spike.degat)
            self.vitesse = 2
        if pygame.sprite.spritecollide(self, self.game.player.all_tornado, False):
            self.damage(self.game.player.tornado.degat)
            if self.facing == 1:
                self.rect.x -= 7
            if self.facing == 2:
                self.rect.x += 7
        if pygame.sprite.spritecollide(self, self.game.all_playeur, False):       
                self.attack +=1
                if self.facing == 1:
                    self.image = pygame.image.load("GameData/entite/gobelin/attack/"+str(self.attack)+"_right.png")
                if self.facing == 2:
                    self.image = pygame.image.load("GameData/entite/gobelin/attack/"+str(self.attack)+"_left.png")
                if self.attack == 16:
                    self.game.player.damage(self.force)
                    self.attack = 0
        elif player_position > self.rect.x:
            self.img += 1
            if self.img == 17:
                self.img = 1
            self.image = pygame.image.load("GameData/entite/gobelin/run/"+str(self.img)+"_right.png")
            self.rect.x += self.vitesse
            self.facing = 1


        elif player_position < self.rect.x:
            self.img += 1
            if self.img == 17:
                self.img = 1
            self.image = pygame.image.load("GameData/entite/gobelin/run/"+str(self.img)+"_left.png")
            self.rect.x -= self.vitesse
            self.facing == 2


