from tool.storage import stocke_data
import pygame,sys
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,100))
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(user_text)
            stocke_data("name",user_text)
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
    if active:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(screen,color,input_rect)
    text_surface = base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surface,(0,0))
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()
    clock.tick(20)
    






