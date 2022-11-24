import pygame
from tool.storage import*
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game =game
        self.image = pygame.image.load("GameData/entite/player/Idle/1_right.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 600
        self.data = obtenir_toute_data()
        self.viemax = self.data["vie_max"]
        self.vie = self.data["vie_max"]
        self.force = self.data["force"]
        self.vitesse = 8
        self.player_kill = False
        self.img = 0
        self.attaque = 0
        self.regen_vie = self.viemax/600
        self.level = self.data["niveau"]
        self.need_exp = self.data["next_lvl_up"]
        self.xp = self.data["experience"]
        self.skill_point = self.data["skill_point"]
    
    def remover(self):
        for player in self.game.all_playeur:
            player.remove()

    def damage(self,amount):
        self.vie -= amount
        hit = pygame.mixer.Sound("Music/sound/sword_hit.mp3")
        hit.play()
        if self.vie <= 0:
            self.player_kill = True
    
    def droite(self):
        self.img += 1
        if self.img == 9:
            self.img = 1
        self.image = pygame.image.load("GameData/entite/player/run/"+str(self.img)+"_right.png")
        self.rect.x += self.vitesse

    def gauche(self):
        self.img += 1
        if self.img == 9:
            self.img = 1
        self.image = pygame.image.load("GameData/entite/player/run/"+str(self.img)+"_left.png")
        self.rect.x -= self.vitesse


    def idle(self,facing):
        self.img += 1
        if self.img == 9:
            self.img = 1
        if facing == 1:
            self.image = pygame.image.load("GameData/entite/player/Idle/"+str(self.img)+"_right.png")
        elif facing == 2:
            self.image = pygame.image.load("GameData/entite/player/Idle/"+str(self.img)+"_left.png")
        else : 
            pass
    def attack(self,facing):
        self.attaque+=1
        if  facing == 1:
            if self.attaque > 7:
                self.attaque = 1
                hit = pygame.mixer.Sound("Music/sound/player_sword.mp3")
                hit.play()
                for gobelin in pygame.sprite.spritecollide(self, self.game.all_gobelin, False):
                    gobelin.damage(self.force)

            self.image = pygame.image.load("GameData/entite/player/attack/"+str(self.attaque)+"_right.png")
        elif facing == 2:
            if self.attaque > 7:
                self.attaque = 1
                hit = pygame.mixer.Sound("Music/sound/player_sword.mp3")
                hit.play()
                for gobelin in pygame.sprite.spritecollide(self, self.game.all_gobelin, False):
                    gobelin.damage(self.force)

            self.image = pygame.image.load("GameData/entite/player/attack/"+str(self.attaque)+"_left.png")




    def up_date(self, surface):
        if self.xp >= self.need_exp:
            self.level += 1
            self.xp = int(self.xp - self.need_exp)
            self.need_exp = int(self.need_exp*1.05)
            self.skill_point += 1
            stocke_data("niveau", self.level)
            stocke_data("next_lvl_up",self.need_exp)
            stocke_data("skill_point",self.skill_point)
        stocke_data("experience",self.xp)
        lvl = pygame.font.Font("tool/police/font.ttf", 20).render(str(self.level), True, "Blue")
        surface.blit(lvl, (310, 0))
        if self.vie < self.viemax:
            self.vie += self.regen_vie
        if self.vie > self.viemax:
            self.vie = self.viemax
        position_barre_3 = [0, 20, self.xp / self.need_exp * 300, 20]
        position_barre4 = [0, 20, self.need_exp / self.need_exp * 300, 20]
        pygame.draw.rect(surface, (60, 63, 60), position_barre4)
        pygame.draw.rect(surface, (49, 140, 231), position_barre_3)
        position_barre_2 = [0, 0, self.vie / self.viemax * 300, 20]
        position_barre = [0, 0, self.viemax / self.viemax * 300, 20]
        pygame.draw.rect(surface, (60, 63, 60), position_barre)
        pygame.draw.rect(surface, (111, 210, 46), position_barre_2)
        xp = pygame.font.Font("tool/police/font.ttf", 20).render(str(self.xp)+"/"+str(self.need_exp), True,(240, 195, 0))
        surface.blit(xp, (150, 20))