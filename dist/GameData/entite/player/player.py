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
        print(self.attaque)
        self.attaque+=1
        if  facing == 1:
            if self.attaque > 14:
                self.attaque = 1
                hit = pygame.mixer.Sound("Music/sound/player_sword.mp3")
                hit.play()
                for gobelin in pygame.sprite.spritecollide(self, self.game.all_gobelin, False):
                    gobelin.damage(self.force)

            self.image = pygame.image.load("GameData/entite/player/attack/"+str(self.attaque)+"_right.png")
        elif facing == 2:
            if self.attaque > 14:
                self.attaque = 1
                hit = pygame.mixer.Sound("Music/sound/player_sword.mp3")
                hit.play()
                for gobelin in pygame.sprite.spritecollide(self, self.game.all_gobelin, False):
                    gobelin.damage(self.force)

            self.image = pygame.image.load("GameData/entite/player/attack/"+str(self.attaque)+"_left.png")




    def update_health_barre(self, surface):
        position_barre_2 = [0, 0, self.vie / self.viemax * 300, 20]
        position_barre = [0, 0, self.viemax / self.viemax * 300, 20]
        pygame.draw.rect(surface, (60, 63, 60), position_barre)
        pygame.draw.rect(surface, (111, 210, 46), position_barre_2)