import pygame, time
from tool.storage import*
from GameData.entite.earthquake.earthquake import earthquake
from GameData.entite.ice_spike.ice_spike import ice_spike
from GameData.entite.tornado.tornado import Tornado
from GameData.entite.fire_pillar.fire_pillar import fire_pillar
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game =game
        self.image = pygame.image.load("GameData/entite/player/Idle/1_right.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 600
        self.facing = 1
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
        self.mana_max = self.data["mana"]
        self.mana = self.mana_max
        self.regen_mana = self.mana_max/1200
        self.all_earthquake = pygame.sprite.Group()
        self.earth_quake = earthquake(self,self.rect.x,self.rect.y,self.facing)
        self.all_ice_spike = pygame.sprite.Group()
        self.ice_spike = ice_spike(self,self.rect.x,self.rect.y,self.facing)
        self.all_tornado = pygame.sprite.Group()
        self.tornado = Tornado(self,self.facing)
        self.all_fire_pillar = pygame.sprite.Group()
        self.fire_pillar = fire_pillar(self,self.facing)


    def power_1(self):
        if self.data["element"] == "aucun":
            pass
        if self.data["element"] == "earth" or self.data["element"] == "ADMIN":
            if not self.all_earthquake and self.mana >= 100 :
                self.mana -= 100
                self.all_earthquake.add(earthquake(self,self.rect.x,self.rect.y,self.facing))
                earth = pygame.mixer.Sound("Music/sound/earthquake.mp3")
                earth.play()
        if self.data["element"] == "water" or self.data["element"] == "ADMIN":
            if not self.all_ice_spike and self.mana >= 100 :
                self.mana -= 100
                self.all_ice_spike.add(ice_spike(self,self.rect.x,self.rect.y,self.facing))
                water = pygame.mixer.Sound("Music/sound/ice_spike.mp3")
                water.play()
        if self.data["element"] == "wind" or self.data["element"] == "ADMIN":
            if not self.all_tornado and self.mana >= 100 :
                self.mana -= 100
                self.all_tornado.add(Tornado(self,self.facing))
                wind = pygame.mixer.Sound("Music/sound/tornado.mp3")
                wind.play()
        if self.data["element"] == "fire" or self.data["element"] == "ADMIN":
            if not self.all_fire_pillar and self.mana >= 100 :
                self.mana -= 100
                self.all_fire_pillar.add(fire_pillar(self,self.facing))
                fire = pygame.mixer.Sound("Music/sound/fire_pillar.mp3")
                fire.play()

       
    
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
        self.facing = 1

    def gauche(self):
        self.img += 1
        if self.img == 9:
            self.img = 1
        self.image = pygame.image.load("GameData/entite/player/run/"+str(self.img)+"_left.png")
        self.rect.x -= self.vitesse
        self.facing = 2


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
                hit = pygame.mixer.Sound("Music/sound/sword_hit.mp3")
                hit.play()
                for gobelin in pygame.sprite.spritecollide(self, self.game.all_gobelin, False):
                    gobelin.damage(self.force)

            self.image = pygame.image.load("GameData/entite/player/attack/"+str(self.attaque)+"_right.png")
        elif facing == 2:
            if self.attaque > 7:
                self.attaque = 1
                hit = pygame.mixer.Sound("Music/sound/sword_hit.mp3")
                hit.play()
                for gobelin in pygame.sprite.spritecollide(self, self.game.all_gobelin, False):
                    gobelin.damage(self.force)

            self.image = pygame.image.load("GameData/entite/player/attack/"+str(self.attaque)+"_left.png")




    def up_date(self, surface):
        if self.xp >= self.need_exp:
            self.level += 1
            self.xp = int(self.xp - self.need_exp)
            if  self.level <= 50:
                self.need_exp = int(self.need_exp*1.05)
            if self.level > 50:
                self.need_exp = int(self.need_exp*1.005)
            if self.level > 100:
                self.need_exp = int(self.need_exp*1.0005)
            if self.level > 150:
                self.need_exp = int(self.need_exp*1.00005)
            self.skill_point += 1
            stocke_data("niveau", self.level)
            stocke_data("next_lvl_up",self.need_exp)
            stocke_data("skill_point",self.skill_point)
        stocke_data("experience",self.xp)
        if self.vie < self.viemax:
            self.vie += self.regen_vie
        if self.vie > self.viemax:
            self.vie = self.viemax
        if self.mana < self.mana_max:
            self.mana += self.regen_mana
        if self.mana > self.mana_max:
            self.mana = self.mana_max
        if self.xp <= self.need_exp:
            taille = self.xp/self.need_exp*310
        elif self.xp > self.need_exp:
            taille = 310
        position_barre_5 = [0, 80, self.mana / self.mana_max * 310, 10]
        position_barre6 = [0, 80, self.mana_max / self.mana_max * 310, 10]
        pygame.draw.rect(surface, (60, 63, 60), position_barre6)
        pygame.draw.rect(surface, (49, 140, 231), position_barre_5)
        position_barre_3 = [0, 60, taille, 20]
        position_barre4 = [0, 60, 310, 20]
        pygame.draw.rect(surface, (60, 63, 60), position_barre4)
        pygame.draw.rect(surface, (49, 140, 231), position_barre_3)
        position_barre_2 = [80, 17, self.vie / self.viemax * 415, 30]
        position_barre = [80, 17, self.viemax / self.viemax * 415, 30]
        pygame.draw.rect(surface, (60, 63, 60), position_barre)
        pygame.draw.rect(surface, (111, 210, 46), position_barre_2)
        if self.level > 99999:
            self.level_print = "99999."
        else:
            self.level_print = self.level
        if self.data["element"] == "aucun":
            couleur = "white"
        elif self.data["element"] == "earth":
            couleur = "Brown"
        elif self.data["element"] == "water":
            couleur = "blue"
        elif self.data["element"] == "wind":
            couleur = "green"
        elif self.data["element"] == "fire":
            couleur = "Red"
        elif self.data["element"] == "ADMIN":
            couleur = "BLACK"
        else:
            couleur = "grey"

        surface.blit(pygame.image.load("Background/in_game/gui.png"),(0,0))
        surface.blit(pygame.font.Font("tool/police/font.ttf", 15).render(self.data["name"], True,"white"),(10,0))
        surface.blit(pygame.font.Font("tool/police/font.ttf", 10).render("xp : "+str(self.xp)+"/"+str(self.need_exp), True, "white"), (50, 70))
        surface.blit(pygame.font.Font("tool/police/font.ttf", 20).render(str(self.level_print), True, "White"), (460, 60))
        surface.blit(pygame.font.Font("tool/police/font.ttf", 20).render(self.data["element"], True, couleur), (320, 60))