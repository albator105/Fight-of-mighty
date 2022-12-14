import pygame, sys
from GameData.Game import Game
from random import randint
from time import sleep
from tool.storage import stocke_data
class niveau_1:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 710))
        self.game = Game()
        self.facing = 1
        self.clock = pygame.time.Clock()

    def niveau_1_1(self,type):
        music = True
        if type:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Music/intro_w1_niveau_1-1.mp3")
            pygame.mixer.music.play()
            self.screen.blit(pygame.transform.scale(pygame.image.load("Background/menu_game/histoire_1.png"),(1280,710)),(0,0))
            pygame.display.flip()
            sleep(6)
            music = False
        image = pygame.image.load("GameData/Niveaux/World_1/niveau_1/niveau_1-1.png")
        self.game.player.__init__(self.game)
        self.game.all_playeur.add(self.game.player)
        self.facing = 1
        if music:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Music/intro_w1_niveau_1-1.mp3")
            pygame.mixer.music.play()
        self.game.player.vie = self.game.player.viemax
        self.game.player.player_kill = False
        self.game.player.rect.x = 100
        self.game.player.rect.y = 600
        self.game.remove_ennemie()
        self.game.all_remove()
        for i in range (randint(1,2)):
            self.game.spawn_gobelin(1,4)
        self.game.pressed.clear()
        while True:
            self.clock.tick(16)
            self.screen.blit(image, (0, 0))
            for player in self.game.all_playeur:
                player.up_date(self.screen)
                if player.player_kill == True:
                    pygame.mixer.music.load("Music/main.mp3")
                    pygame.mixer.music.play()
                    self.game.player.remover()
                    return False
                if self.game.player.rect.x >= 1220 and len(self.game.all_gobelin) == 0:
                    return True
            for gobelin in self.game.all_gobelin:
                gobelin.deplacement_general(self.game.player.rect.x)
                gobelin.update_health_barre(self.screen)
            for earthquake in self.game.player.all_earthquake:
                earthquake.up_date()
            for ice_spike in self.game.player.all_ice_spike:
                ice_spike.up_date()
            for tornado in self.game.player.all_tornado:
                tornado.up_date()
            for fire_pillar in self.game.player.all_fire_pillar:
                fire_pillar.up_date()
            
            self.game.all_gobelin.draw(self.screen)
            self.game.all_playeur.draw(self.screen)
            self.game.player.all_earthquake.draw(self.screen)
            self.game.player.all_ice_spike.draw(self.screen)
            self.game.player.all_tornado.draw(self.screen)
            self.game.player.all_fire_pillar.draw(self.screen)

            
            if self.game.pressed.get(pygame.K_TAB):
                self.game.pressed[pygame.K_TAB] = False
                pygame.mixer.music.load("Music/main.mp3")
                pygame.mixer.music.play()
                self.game.player.remove()
                return False
            if self.game.pressed.get(pygame.K_m) == True or self.game.pressed.get(pygame.K_z) == True:
                self.game.player.attack(self.facing)
            elif self.game.pressed.get(pygame.K_w) == True and self.game.pressed.get(pygame.K_x) == True:
                stocke_data("element", "ADMIN")
                self.game.player.__init__(self.game)
            elif self.game.pressed.get(pygame.K_d) == True:
                self.game.player.power_1()
            elif self.game.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x <= 1240 or self.game.pressed.get(pygame.K_e) and self.game.player.rect.x <= 1240 :
                self.game.player.droite()
                self.facing = 1
            elif self.game.pressed.get(pygame.K_LEFT) and self.game.player.rect.x >= 0 or self.game.pressed.get(pygame.K_a) and self.game.player.rect.x >= 0:
                self.facing = 2
                self.game.player.gauche()
            else : 
                self.game.player.idle(self.facing)
            self.game.Touche(self.facing)
            pygame.display.flip()


    def niveau_1_2(self):
        image = pygame.image.load("GameData/Niveaux/World_1/niveau_1/niveau_1-2.png")
        self.facing = 1
        self.game.player.rect.x = 100
        self.game.player.rect.y = 600
        self.game.remove_ennemie()
        for i in range (randint(1,3)):
            self.game.spawn_gobelin(2,5)
        self.game.pressed.clear()
        self.game.all_remove()
        while True:
            self.clock.tick(16)
            self.screen.blit(image, (0, 0))
            for player in self.game.all_playeur:
                player.up_date(self.screen)
                if player.player_kill == True:
                    pygame.mixer.music.load("Music/main.mp3")
                    pygame.mixer.music.play()
                    self.game.player.remover()
                    return False
                if self.game.player.rect.x >= 1220 and len(self.game.all_gobelin) == 0:
                    return True
            for gobelin in self.game.all_gobelin:
                gobelin.deplacement_general(self.game.player.rect.x)
                gobelin.update_health_barre(self.screen)
            for earthquake in self.game.player.all_earthquake:
                earthquake.up_date()
            for ice_spike in self.game.player.all_ice_spike:
                ice_spike.up_date()
            for tornado in self.game.player.all_tornado:
                tornado.up_date()
            for fire_pillar in self.game.player.all_fire_pillar:
                fire_pillar.up_date()

            
            self.game.all_gobelin.draw(self.screen)
            self.game.all_playeur.draw(self.screen)
            self.game.player.all_earthquake.draw(self.screen)
            self.game.player.all_ice_spike.draw(self.screen)
            self.game.player.all_tornado.draw(self.screen)
            self.game.player.all_fire_pillar.draw(self.screen)

            
            if self.game.pressed.get(pygame.K_TAB):
                self.game.pressed[pygame.K_TAB] = False
                pygame.mixer.music.load("Music/main.mp3")
                pygame.mixer.music.play()
                self.game.player.remove()
                return False
            if self.game.pressed.get(pygame.K_m) == True or self.game.pressed.get(pygame.K_z) == True:
                self.game.player.attack(self.facing)
            elif self.game.pressed.get(pygame.K_w) == True and self.game.pressed.get(pygame.K_x) == True:
                stocke_data("element", "ADMIN")
                self.game.player.__init__(self.game)
            elif self.game.pressed.get(pygame.K_d) == True:
                self.game.player.power_1()
            elif self.game.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x <= 1240 or self.game.pressed.get(pygame.K_e) and self.game.player.rect.x <= 1240 :
                self.game.player.droite()
                self.facing = 1
            elif self.game.pressed.get(pygame.K_LEFT) and self.game.player.rect.x >= 0 or self.game.pressed.get(pygame.K_a) and self.game.player.rect.x >= 0:
                self.facing = 2
                self.game.player.gauche()
            else : 
                self.game.player.idle(self.facing)
            self.game.Touche(self.facing)
            pygame.display.flip()

    def niveau_1_3(self):
        image = pygame.image.load("GameData/Niveaux/World_1/niveau_1/niveau_1-3.png")
        self.facing = 1
        self.game.player.rect.x = 100
        self.game.player.rect.y = 600
        self.game.remove_ennemie()
        for i in range (randint(2,3)):
            self.game.spawn_gobelin(3,5)
        self.game.pressed.clear()
        self.game.all_remove()
        while True:
            self.clock.tick(16)
            self.screen.blit(image, (0, 0))
            for player in self.game.all_playeur:
                player.up_date(self.screen)
                if player.player_kill == True:
                    pygame.mixer.music.load("Music/main.mp3")
                    pygame.mixer.music.play()
                    self.game.player.remover()
                    return False
                if self.game.player.rect.x >= 1220 and len(self.game.all_gobelin) == 0:
                    return True
            for gobelin in self.game.all_gobelin:
                gobelin.deplacement_general(self.game.player.rect.x)
                gobelin.update_health_barre(self.screen)
            for earthquake in self.game.player.all_earthquake:
                earthquake.up_date()
            for ice_spike in self.game.player.all_ice_spike:
                ice_spike.up_date()
            for tornado in self.game.player.all_tornado:
                tornado.up_date()
            for fire_pillar in self.game.player.all_fire_pillar:
                fire_pillar.up_date()
            
            self.game.all_gobelin.draw(self.screen)
            self.game.all_playeur.draw(self.screen)
            self.game.player.all_earthquake.draw(self.screen)
            self.game.player.all_ice_spike.draw(self.screen)
            self.game.player.all_tornado.draw(self.screen)
            self.game.player.all_fire_pillar.draw(self.screen)

            
            if self.game.pressed.get(pygame.K_TAB):
                self.game.pressed[pygame.K_TAB] = False
                pygame.mixer.music.load("Music/main.mp3")
                pygame.mixer.music.play()
                self.game.player.remove()
                return False
            if self.game.pressed.get(pygame.K_m) == True or self.game.pressed.get(pygame.K_z) == True:
                self.game.player.attack(self.facing)
            elif self.game.pressed.get(pygame.K_w) == True and self.game.pressed.get(pygame.K_x) == True:
                stocke_data("element", "ADMIN")
                self.game.player.__init__(self.game)
            elif self.game.pressed.get(pygame.K_d) == True:
                self.game.player.power_1()
            elif self.game.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x <= 1240 or self.game.pressed.get(pygame.K_e) and self.game.player.rect.x <= 1240 :
                self.game.player.droite()
                self.facing = 1
            elif self.game.pressed.get(pygame.K_LEFT) and self.game.player.rect.x >= 0 or self.game.pressed.get(pygame.K_a) and self.game.player.rect.x >= 0:
                self.facing = 2
                self.game.player.gauche()
            else : 
                self.game.player.idle(self.facing)
            self.game.Touche(self.facing)
            pygame.display.flip()

    def niveau_1_4(self):
        image = pygame.image.load("GameData/Niveaux/World_1/niveau_1/niveau_1-4.png")
        self.facing = 1
        self.game.player.rect.x = 100
        self.game.player.rect.y = 600
        self.game.remove_ennemie()
        for i in range (randint(2,4)):
            self.game.spawn_gobelin(4,7)
        self.game.pressed.clear()
        self.game.all_remove()
        while True:
            self.clock.tick(16)
            self.screen.blit(image, (0, 0))
            for player in self.game.all_playeur:
                player.up_date(self.screen)
                if player.player_kill == True:
                    pygame.mixer.music.load("Music/main.mp3")
                    pygame.mixer.music.play()
                    self.game.player.remover()
                    return False
                if self.game.player.rect.x >= 1220 and len(self.game.all_gobelin) == 0:
                    return True
            for gobelin in self.game.all_gobelin:
                gobelin.deplacement_general(self.game.player.rect.x)
                gobelin.update_health_barre(self.screen)
            for earthquake in self.game.player.all_earthquake:
                earthquake.up_date()
            for ice_spike in self.game.player.all_ice_spike:
                ice_spike.up_date()
            for tornado in self.game.player.all_tornado:
                tornado.up_date()
            for fire_pillar in self.game.player.all_fire_pillar:
                fire_pillar.up_date()
            
            self.game.all_gobelin.draw(self.screen)
            self.game.all_playeur.draw(self.screen)
            self.game.player.all_earthquake.draw(self.screen)
            self.game.player.all_ice_spike.draw(self.screen)
            self.game.player.all_tornado.draw(self.screen)
            self.game.player.all_fire_pillar.draw(self.screen)

            
            if self.game.pressed.get(pygame.K_TAB):
                self.game.pressed[pygame.K_TAB] = False
                pygame.mixer.music.load("Music/main.mp3")
                pygame.mixer.music.play()
                self.game.player.remove()
                return False
            if self.game.pressed.get(pygame.K_m) == True or self.game.pressed.get(pygame.K_z) == True:
                self.game.player.attack(self.facing)
            elif self.game.pressed.get(pygame.K_w) == True and self.game.pressed.get(pygame.K_x) == True:
                stocke_data("element", "ADMIN")
                self.game.player.__init__(self.game)
            elif self.game.pressed.get(pygame.K_d) == True:
                self.game.player.power_1()
            elif self.game.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x <= 1240 or self.game.pressed.get(pygame.K_e) and self.game.player.rect.x <= 1240 :
                self.game.player.droite()
                self.facing = 1
            elif self.game.pressed.get(pygame.K_LEFT) and self.game.player.rect.x >= 0 or self.game.pressed.get(pygame.K_a) and self.game.player.rect.x >= 0:
                self.facing = 2
                self.game.player.gauche()
            else : 
                self.game.player.idle(self.facing)
            self.game.Touche(self.facing)
            pygame.display.flip()


    def niveau_1_5(self):
        image = pygame.image.load("GameData/Niveaux/World_1/niveau_1/niveau_1-5.png")
        self.facing = 1
        self.game.player.rect.x = 100
        self.game.player.rect.y = 600
        self.game.remove_ennemie()
        for i in range (randint(1,3)):
            self.game.spawn_gobelin(9,11)
        self.game.pressed.clear()
        self.game.all_remove()
        self.game.spawn_dark_player()
        pygame.mixer.music.load("Music/boss_fight.mp3")
        pygame.mixer.music.play()
        while True:
            self.clock.tick(16)
            self.screen.blit(image, (0, 0))
            for player in self.game.all_playeur:
                player.up_date(self.screen)
                if player.player_kill == True:
                    pygame.mixer.music.load("Music/main.mp3")
                    pygame.mixer.music.play()
                    self.game.player.remover()
                    return False
                if self.game.player.rect.x >= 1220 and len(self.game.all_dark_playeur) == 0:
                    return True
            for dark_player in self.game.all_dark_playeur:
                dark_player.up_date(self.screen)
            for earthquake in self.game.player.all_earthquake:
                earthquake.up_date()
            for ice_spike in self.game.player.all_ice_spike:
                ice_spike.up_date()
            for tornado in self.game.player.all_tornado:
                tornado.up_date()
            for fire_pillar in self.game.player.all_fire_pillar:
                fire_pillar.up_date()
            
            self.game.all_dark_playeur.draw(self.screen)
            self.game.all_playeur.draw(self.screen)
            self.game.player.all_earthquake.draw(self.screen)
            self.game.player.all_ice_spike.draw(self.screen)
            self.game.player.all_tornado.draw(self.screen)
            self.game.player.all_fire_pillar.draw(self.screen)

            
            if self.game.pressed.get(pygame.K_TAB):
                self.game.pressed[pygame.K_TAB] = False
                pygame.mixer.music.load("Music/main.mp3")
                pygame.mixer.music.play()
                self.game.player.remove()
                return False
            if self.game.pressed.get(pygame.K_m) == True or self.game.pressed.get(pygame.K_z) == True:
                self.game.player.attack(self.facing)
            elif self.game.pressed.get(pygame.K_w) == True and self.game.pressed.get(pygame.K_x) == True:
                stocke_data("element", "ADMIN")
                self.game.player.__init__(self.game)
            elif self.game.pressed.get(pygame.K_d) == True:
                self.game.player.power_1()
            elif self.game.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x <= 1240 or self.game.pressed.get(pygame.K_e) and self.game.player.rect.x <= 1240 :
                self.game.player.droite()
                self.facing = 1
            elif self.game.pressed.get(pygame.K_LEFT) and self.game.player.rect.x >= 0 or self.game.pressed.get(pygame.K_a) and self.game.player.rect.x >= 0:
                self.facing = 2
                self.game.player.gauche()
            else : 
                self.game.player.idle(self.facing)
            self.game.Touche(self.facing)
            pygame.display.flip()