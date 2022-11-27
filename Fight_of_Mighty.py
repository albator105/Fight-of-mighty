
from tool.storage import*
chargeurstorage()
#importation des libs
import pygame,sys
from GameData.Niveaux.World_1.niveau_1.niveau_1 import niveau_1
niveau1 = niveau_1()
#importation des outils
from tool.button import Button


#initialisation des composant de pygame
pygame.init()

#definition de la fenètre du jeux
screen = pygame.display.set_mode((1280,700),pygame.FULLSCREEN)
pygame.display.set_icon(pygame.transform.scale(pygame.image.load("icon_exe.png"), (32,32)))
pygame.display.set_caption("FOM", "Fight Of Myghty")

#création d'un horloge
clock = pygame.time.Clock()

#musique du jeu
pygame.mixer.music.load("Music/main.mp3")
pygame.mixer.music.play()

#definition du menu principal
def main_menu():
    img_main_menu = pygame.transform.scale(pygame.image.load("Background/main_menu/1.png"),(screen.get_width(),screen.get_height()))
    while True:
        pos_souris = pygame.mouse.get_pos()
        clock.tick(10)
        screen.blit(img_main_menu,(0,0))
        Exit = Button(
            image=None,
            pos=(640, 500),
            text_input="EXIT",
            font=Button.get_font(60),
            base_color="Red",
            hovering_color=(131, 166, 151),
        )
        menu_game = Button(
            image=None,
            pos=(640, 200),
            text_input="JOUER",
            font=Button.get_font(60),
            base_color="Red",
            hovering_color=(131, 166, 151),
        )
        menu_stat = Button(
            image=None,
            pos=(640, 350),
            text_input="STAT",
            font=Button.get_font(60),
            base_color="Red",
            hovering_color=(131, 166, 151),
        )
        Exit.changeColor(pos_souris)
        Exit.update(screen)
        menu_game.changeColor(pos_souris)
        menu_game.update(screen)
        menu_stat.changeColor(pos_souris)
        menu_stat.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Exit.checkForInput(pos_souris):
                    pygame.quit()
                    sys.exit()
                if menu_game.checkForInput(pos_souris):
                    menu_play()
                if menu_stat.checkForInput(pos_souris):
                    stat_menu()
            
        
        pygame.display.flip()
def menu_play():
    niv1 = False
    while True:
        screen.blit(pygame.transform.scale(pygame.image.load("Background/menu_game/menu_game.png"),(screen.get_width(),screen.get_height())),(0,0))
        pos_souris = pygame.mouse.get_pos()
        if not niv1:
            Retour = Button(
            image=None,
            pos=(100, 100),
            text_input="RETOUR",
            font=Button.get_font(40),
            base_color="Red",
            hovering_color=(131, 166, 151),
        )
            niveau_1 = Button(
            image=pygame.image.load("Background/menu_game/start.png"),
            pos=(1100, 660),
            text_input="",
            font=Button.get_font(40),
            base_color="Red",
            hovering_color="Black",
        )
        if niv1:
            screen.blit(pygame.image.load("Background/menu_game/black.png"),(0,0))
            Free = Button(
            image=None,
            pos=(320, 350),
            text_input="LIBRE",
            font=Button.get_font(40),
            base_color="Red",
            hovering_color="Blue",
            )
            histoire = Button(
            image=None,
            pos=(960, 350),
            text_input="HISTOIRE",
            font=Button.get_font(40),
            base_color="Blue",
            hovering_color="Red",
            )
            histoire.changeColor(pos_souris)
            histoire.update(screen)
            Free.changeColor(pos_souris)
            Free.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Free.checkForInput(pos_souris):
                        niv1 =False
                        code = niveau1.niveau_1_1(False)
                        if code:
                            del code
                            code=niveau1.niveau_1_2()
                            if code:
                                del code
                                code=niveau1.niveau_1_3()
                                if code:
                                    del code
                                    code=niveau1.niveau_1_4()
                                    if code:
                                        del code
                                        code =niveau1.niveau_1_5()
                                        del code
                                        pygame.mixer.music.load("Music/main.mp3")
                                        pygame.mixer.music.play()
                    if histoire.checkForInput(pos_souris):
                        niv1 =False
                        code = niveau1.niveau_1_1(True)
                        if code:
                            del code
                            code=niveau1.niveau_1_2()
                            if code:
                                del code
                                code=niveau1.niveau_1_3()
                                if code:
                                    del code
                                    code=niveau1.niveau_1_4()
                                    if code:
                                        del code
                                        code = niveau1.niveau_1_5()
                                        del codee
                                        pygame.mixer.music.load("Music/main.mp3")
                                        pygame.mixer.music.play()
        if not niv1:
            Retour.changeColor(pos_souris)
            Retour.update(screen)
            niveau_1.changeColor(pos_souris)
            niveau_1.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Retour.checkForInput(pos_souris):
                    main_menu()
                if niveau_1.checkForInput(pos_souris):
                    niv1 = True
        pygame.display.flip()

def stat_menu():
    img_main_menu = pygame.transform.scale(pygame.image.load("Background/menu_stat/stat_menu.png"),(screen.get_width(),screen.get_height()))
    while True:
        pos_souris = pygame.mouse.get_pos()
        clock.tick(10)
        screen.blit(img_main_menu,(0,0))
        screen.blit(pygame.image.load("Background/menu_stat/stat_panel.png"),(100,100))
        data=obtenir_toute_data()
        if (data["niveau"]) > 99999999999999999999:
            niveau_playeur = "99999999999999999..."
        else:
            niveau_playeur = str((data["niveau"]))
        if (data["skill_point"]) > 999999999999999999999:
            skill_point_playeur = "999999999999999999..."
        else:
            skill_point_playeur = str((data["skill_point"]))
        if (data["vie_max"]) > 9999999999999999999:
            vie_max_playeur = "9999999999999999..."
        else:
            vie_max_playeur = str((data["vie_max"]))
        if (data["force"]) > 9999999999999999999999:
            force_playeur = "9999999999999999999..."
        else:
            force_playeur = str((data["force"]))
        if (data["mana"]) > 99999999999999999999:
            mana_playeur = "99999999999999999..."
        else:
            mana_playeur = str((data["mana"]))
        niveau = pygame.font.Font("tool/police/font.ttf", 20).render((data["name"]), True,"Black")
        screen.blit(niveau, (150, 110))
        niveau = pygame.font.Font("tool/police/font.ttf", 20).render("Niveau : "+niveau_playeur, True,"Black")
        screen.blit(niveau, (110, 140))
        skill_point = pygame.font.Font("tool/police/font.ttf", 20).render("Skill point : "+skill_point_playeur, True,"Black")
        screen.blit(skill_point, (110, 160))
        vie = pygame.font.Font("tool/police/font.ttf", 20).render("Vie : "+vie_max_playeur, True,"Black")
        screen.blit(vie, (110, 180))
        force = pygame.font.Font("tool/police/font.ttf", 20).render("Force : "+force_playeur, True,"Black")
        screen.blit(force, (110, 200))
        mana = pygame.font.Font("tool/police/font.ttf", 20).render("Mana : "+mana_playeur, True,"Black")
        screen.blit(mana, (110, 220))
        element = pygame.font.Font("tool/police/font.ttf", 20).render("Type : "+data["element"], True,"Black")
        screen.blit(element, (110, 240))

        retour = Button(
            image=None,
            pos=(100, 700),
            text_input="retour",
            font=Button.get_font(30),
            base_color="Red",
            hovering_color=(131, 166, 151),
        )
        Force_UP = Button(
            image=pygame.image.load("Background/menu_stat/button.png"),
            pos=(1000, 100),
            text_input="Force UP",
            font=Button.get_font(15),
            base_color="Red",
            hovering_color="Red",
        )
        Life_UP = Button(
            image=pygame.image.load("Background/menu_stat/button.png"),
            pos=(1000, 200),
            text_input="Health UP",
            font=Button.get_font(15),
            base_color="Red",
            hovering_color="Red",
        )
        Mana_UP = Button(
            image=pygame.image.load("Background/menu_stat/button.png"),
            pos=(1000, 300),
            text_input="Mana UP",
            font=Button.get_font(15),
            base_color="Red",
            hovering_color="Red",
        )
        Element_button = Button(
            image=pygame.image.load("Background/menu_stat/button.png"),
            pos=(1080, 600),
            text_input="Elements",
            font=Button.get_font(15),
            base_color="Red",
            hovering_color="Red",
        )

        retour.changeColor(pos_souris)
        retour.update(screen)
        Force_UP.changeColor(pos_souris)
        Force_UP.update(screen)
        Life_UP.changeColor(pos_souris)
        Life_UP.update(screen)
        Mana_UP.changeColor(pos_souris)
        Mana_UP.update(screen)
        Element_button.changeColor(pos_souris)
        Element_button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour.checkForInput(pos_souris):
                    main_menu()
                if Element_button.checkForInput(pos_souris):
                    element_select()
                if Force_UP.checkForInput(pos_souris):
                    if data["skill_point"] > 0:
                        stocke_data("skill_point",obtenir_data("skill_point")-1)
                        stocke_data("force",obtenir_data("force")+2)
                if Life_UP.checkForInput(pos_souris):
                    if data["skill_point"] > 0:
                        stocke_data("skill_point",obtenir_data("skill_point")-1)
                        stocke_data("vie_max",obtenir_data("vie_max")+10)
                if Mana_UP.checkForInput(pos_souris):
                    if data["skill_point"] > 0:
                        stocke_data("skill_point",obtenir_data("skill_point")-1)
                        stocke_data("mana",obtenir_data("mana")+3)
        pygame.display.flip()
def element_select():
    img_main_menu = pygame.transform.scale(pygame.image.load("Background/menu_stat/stat_menu.png"),(screen.get_width(),screen.get_height()))
    while True:
        pos_souris = pygame.mouse.get_pos()
        clock.tick(10)
        screen.blit(img_main_menu,(0,0))
        Fire = Button(
            image=pygame.transform.scale(pygame.image.load("Background/menu_stat/icon/fire_icon.png"),(100,100)),
            pos=(180, 150),
            text_input="FEU",
            font=Button.get_font(20),
            base_color="Black",
            hovering_color="Red",
        )
        wind = Button(
            image=pygame.transform.scale(pygame.image.load("Background/menu_stat/icon/wind_icon.png"),(100,100)),
            pos=(480, 150),
            text_input="AIR",
            font=Button.get_font(20),
            base_color="Black",
            hovering_color="Green",
        ) 
        earth= Button(
            image=pygame.transform.scale(pygame.image.load("Background/menu_stat/icon/earth_icon.png"),(100,100)),
            pos=(780, 150),
            text_input="Terre",
            font=Button.get_font(20),
            base_color="Black",
            hovering_color="Brown",
        )
        eau= Button(
            image=pygame.transform.scale(pygame.image.load("Background/menu_stat/icon/water_icon.png"),(100,100)),
            pos=(1080, 150),
            text_input="EAU",
            font=Button.get_font(20),
            base_color="Black",
            hovering_color="Blue",
        )       

        retour = Button(
            image=None,
            pos=(100, 700),
            text_input="retour",
            font=Button.get_font(30),
            base_color="Red",
            hovering_color=(131, 166, 151),
        )

        retour.changeColor(pos_souris)
        retour.update(screen)
        earth.changeColor(pos_souris)
        earth.update(screen)
        wind.changeColor(pos_souris)
        wind.update(screen)
        eau.changeColor(pos_souris)
        eau.update(screen)
        Fire.changeColor(pos_souris)
        Fire.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour.checkForInput(pos_souris):
                    stat_menu()
                if earth.checkForInput(pos_souris):
                    stocke_data("element","earth")
                if eau.checkForInput(pos_souris):
                    stocke_data("element","water")
                if Fire.checkForInput(pos_souris):
                    stocke_data("element","fire")
                if wind.checkForInput(pos_souris):
                    stocke_data("element","wind")
        pygame.display.flip()

main_menu()

