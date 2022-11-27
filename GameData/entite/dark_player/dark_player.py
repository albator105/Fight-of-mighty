import pygame

class dark_player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game =game
        self.image = pygame.image.load("GameData/entite/dark_player/arrival/1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 400
        self.facing = 2
        self.viemax = 1500
        self.vie = self.viemax
        self.force = 30
        self.vitesse = 8
        self.img = 0
        self.attaque = 0
        self.arrival_intro = False
        self.arrival = 1
        self.charging = 0




       
    
    def remover(self):
        self.game.all_dark_playeur.remove(self)

    def damage(self,amount):
        self.vie -= amount
        hit = pygame.mixer.Sound("Music/sound/sword_hit.mp3")
        hit.play()
        if self.vie <= 0:
            self.remover()
    
    def droite(self):
        self.img += 1
        if self.img == 9:
            self.img = 1
        self.image = pygame.image.load("GameData/entite/dark_player/run/"+str(self.img)+"_right.png")
        self.rect.x += self.vitesse
        self.facing = 1

    def gauche(self):
        self.img += 1
        if self.img == 9:
            self.img = 1
        self.image = pygame.image.load("GameData/entite/dark_player/run/"+str(self.img)+"_left.png")
        self.rect.x -= self.vitesse
        self.facing = 2


    def attack(self,facing):
        self.attaque+=1
        if  facing == 1:
            if self.attaque > 7:
                self.attaque = 1
                hit = pygame.mixer.Sound("Music/sound/sword_hit.mp3")
                hit.play()
                for player in pygame.sprite.spritecollide(self, self.game.all_playeur, False):
                    player.damage(self.force)

            self.image = pygame.image.load("GameData/entite/dark_player/attack/"+str(self.attaque)+"_right.png")
        elif facing == 2:
            if self.attaque > 7:
                self.attaque = 1
                hit = pygame.mixer.Sound("Music/sound/sword_hit.mp3")
                hit.play()
                for player in pygame.sprite.spritecollide(self, self.game.all_playeur, False):
                    player.damage(self.force)

            self.image = pygame.image.load("GameData/entite/dark_player/attack/"+str(self.attaque)+"_left.png")
    def up_date(self,surface):
        if self.arrival_intro == True:
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
            position_barre_3 = [0, surface.get_height()-20, self.vie / self.viemax * 1280, 20]
            position_barre4 = [0, surface.get_height()-20, self.viemax / self.viemax * 1280, 20]
            pygame.draw.rect(surface, (60, 63, 60), position_barre4)
            pygame.draw.rect(surface, (111, 210, 46), position_barre_3)
            if pygame.sprite.spritecollide(self, self.game.all_playeur, False): 
                self.attack(self.facing)
            elif self.game.player.rect.x > self.rect.x:
                self.droite()
            elif self.game.player.rect.x < self.rect.x:
                self.gauche()
            if self.charging >= 1280:
                self.rect = self.image.get_rect()
                self.charging = 0
                self.rect.y = 600
                self.rect.x = 1000
        elif  self.arrival_intro == False:
            self.image = pygame.transform.scale(pygame.image.load("GameData/entite/dark_player/arrival/"+str(self.arrival)+".png"),(300,300))
            self.arrival+= 1
            if self.arrival >= 16:
                self.arrival = 1
            self.charging+=10
            position_barre_2 = [0, surface.get_height()-10, self.charging, 10]
            position_barre = [0, surface.get_height()-10, 1280, 10]
            pygame.draw.rect(surface, (60, 63, 60), position_barre)
            pygame.draw.rect(surface, (255, 0, 0), position_barre_2)
            if self.charging >= 1280:
                self.arrival_intro = True
                self.rect.y = 600

        

