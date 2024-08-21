import pygame
#from player import Player
from blocks import *
#from random import randint
from text import text_e
#from main import *
from anim import *
pygame.init()

WIN_WIDTH = 800 
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
        
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)  

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius) #круги
    surf.set_colorkey((0, 0, 0))
    return surf

def main_end(hero,screen,death_list):
    global level
    level = []
    entities2 = pygame.sprite.Group()
    animatedEntities2 = pygame.sprite.Group()

    #entities.add(hero)
    bg_img = f'assets/background_end/background{hero.end}.png'
    text_end = text_e[hero.end]
    text1 = text_end[0]
    text2 = text_end[1]
    text3 = text_end[2]
    text4 = text_end[3]
    test = -1
    test2 = -1
    test3 = -1
    test4 = -1
    list_t = str()
    list_t2 = str()
    list_t3 = str()
    list_t4 = str()
    last = 1
    bg = image.load(bg_img).convert_alpha()
    timer = pygame.time.Clock()
    hero.rect.x = 100
    hero.rect.y = 100
    total_level_width  = 800# Высчитываем фактическую ширину уровня
    total_level_height = 640   # высоту
    dialogue = 1

    camera = Camera(camera_configure, total_level_width, total_level_height) 
    pygame.mixer.pre_init()
    pygame.time.set_timer(pygame.USEREVENT, 120)
    #font = pygame.font.Font(None, 36)
    cooldown_run = 40
    size_t = 28
    score_font = pygame.font.Font("fonts/game.ttf", size_t)
    button = Img_button(760,10,32,32,'assets/button/close.png','assets/button/close.png')
    end = 0
    while not hero.winner:
        timer.tick(60)
        screen.blit(bg,(0,0))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN and e.key == K_r and hero.end == 0:
                dialogue += 1
        if dialogue == 2:
            dialogue += 1
            if death_list['slaim_death'] == 1 and death_list['slaim_bro_death'] != 1:
                text1 = text_end[4]
                text2 = text_end[5]
                text3 = text_end[6]
                text4 = text_end[7]
            elif death_list['slaim_death'] == 1 and death_list['slaim_bro_death'] == 1:
                text1 = text_end[8]
                text2 = text_end[9]
                text3 = text_end[10]
                text4 = text_end[11]
            elif death_list['slaim_bro_death'] == 1 and death_list['slaim_death'] != 1:
                text1 = text_end[12]
                text2 = text_end[13]
                text3 = text_end[14]
                text4 = text_end[15]
            else:
                text1 = text_end[16]
                text2 = text_end[17]
                text3 = text_end[18]
                text4 = text_end[19]
            test = -1
            test2 = -1
            test3 = -1
            test4 = -1
            list_t = str()
            list_t2 = str()
            list_t3 = str()
            list_t4 = str()
        elif dialogue == 4:
            dialogue += 1
            if death_list['fire_mag_quest'] != 1:
                text1 = text_end[20]
                text2 = text_end[21]
                if death_list['people1_win'] == 1 or death_list['people2_win'] == 1 or death_list['people3_win'] == 1:
                    text3 = text_end[22]
                    text4 = text_end[23]
                else:
                    text3 = ''
                    text4 = ''
            elif death_list['fire_mag_quest'] == 1 and death_list['location'] < 15:
                text1 = text_end[24]
                text2 = text_end[25]
                text3 = text_end[26]
                text4 = text_end[27]
            else:
                text1 = text_end[28]
                text2 = text_end[29]
                text3 = text_end[30]
                text4 = text_end[31]
            test = -1
            test2 = -1
            test3 = -1
            test4 = -1
            list_t = str()
            list_t2 = str()
            list_t3 = str()
            list_t4 = str()
        elif dialogue == 6:
            dialogue += 1
            if death_list['ninja2_1_win'] != 1 and death_list['ninja2_2_win'] != 1 and death_list['ninja2_3_win'] != 1:
                text1 = text_end[32]
                text2 = text_end[33]
                text3 = text_end[34]
                text4 = text_end[35]
            elif death_list['ninja2_1_win'] == 1 and death_list['ninja2_2_win'] == 1 and death_list['ninja2_3_win'] == 1 and not 1 in death_list['slaim_rustic_win']: 
                text1 = text_end[36]
                text2 = text_end[37]
                text3 = text_end[38]
                text4 = text_end[39]
            else:
                text1 = text_end[40]
                text2 = text_end[41]
                text3 = text_end[42]
                text4 = text_end[43]
            test = -1
            test2 = -1
            test3 = -1
            test4 = -1
            list_t = str()
            list_t2 = str()
            list_t3 = str()
            list_t4 = str()
        elif dialogue == 8:
            dialogue += 1
            text1 = text_end[44]
            text2 = text_end[45]
            if (death_list['king_death'] == 1 and death_list['assistant_quest3'] != 1) or (death_list['king_death'] == 1 and death_list['assistant_win'] == 1):
                text3 = text_end[46]
                end = 1
            elif (death_list['king_death'] != 1 and death_list['assistant_quest3'] != 1) or (death_list['king_death'] != 1 and death_list['assistant_win'] == 1):
                text3 = text_end[47]
                end = 2
            else:
                text3 = text_end[48]
                end = 3
            text4 = ''
            test = -1
            test2 = -1
            test3 = -1
            test4 = -1
            list_t = str()
            list_t2 = str()
            list_t3 = str()
            list_t4 = str()
        elif dialogue == 10:
            dialogue += 1
            if end == 1:
                text1 = text_end[49]
                text2 = text_end[50]
                text3 = text_end[51]
                text4 = text_end[52]
            elif end == 2:
                text1 = text_end[61]
                text2 = text_end[62]
                text3 = text_end[63]
                text4 = text_end[64]
            else:
                text1 = text_end[77]
                text2 = text_end[78]
                text3 = text_end[79]
                text4 = text_end[80]
            test = -1
            test2 = -1
            test3 = -1
            test4 = -1
            list_t = str()
            list_t2 = str()
            list_t3 = str()
            list_t4 = str()
        elif dialogue == 12:
            dialogue += 1
            end_good = 0
            if death_list['king_death'] != 1:
                end_good += 2
            if death_list['ninja2_1_win'] == 1 and death_list['ninja2_2_win'] == 1 and death_list['ninja2_3_win'] == 1:
                end_good += 3
            if death_list['slaim_bro_win'] == 1:
                end_good += 1
            if death_list['assistant_win'] == 1:
                end_good += 1
            if death_list['ninja_evil_win'] == 1:
                end_good += 1
            if death_list['fire_mag_win2'] == 1:
                end_good += 2
            for i in death_list:
                if 'death' in i and not 'ninja2' in i and not 'ninja' in i and not 'worm' in i:
                    if death_list[i] == 1:
                        end_good -= 1
            if death_list['witch_win'] == 1:
                end_good -= 1
            if death_list['slaim_farmer_quest'] == 1:
                end_good -= 1
            if end == 1 and end_good >= 5:
                text1 = text_end[53]
                text2 = text_end[54]
                text3 = text_end[55]
                text4 = text_end[56]
            elif end == 1 and end_good < 5:
                text1 = text_end[57]
                text2 = text_end[58]
                text3 = text_end[59]
                text4 = text_end[60]
            elif end == 2 and end_good >= 5: 
                text1 = text_end[65]
                text2 = text_end[66]
                text3 = text_end[67]
                text4 = text_end[68]
            elif end == 2 and end_good < 5 and end_good >= 0: 
                text1 = text_end[69]
                text2 = text_end[70]
                text3 = text_end[71]
                text4 = text_end[72]
            elif end == 2 and end_good < 0: 
                text1 = text_end[73]
                text2 = text_end[74]
                text3 = text_end[75]
                text4 = text_end[76]
            else:
                text1 = text_end[81]
                text2 = text_end[82]
                text3 = text_end[83]
                text4 = text_end[84]
            test = -1
            test2 = -1
            test3 = -1
            test4 = -1
            list_t = str()
            list_t2 = str()
            list_t3 = str()
            list_t4 = str()
        elif dialogue == 14:
            dialogue += 1
            text1 = text_end[85]
            text2 = text_end[86]
            text3 = ''
            text4 = ''
            test = -1
            test2 = -1
            test3 = -1
            test4 = -1
            list_t = str()
            list_t2 = str()
            list_t3 = str()
            list_t4 = str()
        now = pygame.time.get_ticks()
        if now - last >= cooldown_run:
            last = now
            if len(text1) != test:
                test += 1
            if len(text1) > test:
                list_t += text1[test]
            if len(text1) == test:
                if len(text2) != test2:
                    test2 += 1
                if len(text2) > test2:
                    list_t2 += text2[test2]
                if len(text2) == test2:
                    if len(text3) != test3:
                        test3 += 1
                    if len(text3) > test3:
                        list_t3 += text3[test3]
                    if len(text3) == test3:
                        test4 += 1
                        if len(text4) > test4:
                            list_t4 += text4[test4]
        text_surface = score_font.render(list_t, False, (240, 240, 240))
        text_surface2 = score_font.render(list_t2, False, (240, 240, 240))
        text_surface3 = score_font.render(list_t3, False, (240, 240, 240))
        text_surface4 = score_font.render(list_t4, False, (240, 240, 240))
        screen.blit(text_surface, (10, 460 + size_t - 10))
        screen.blit(text_surface2, (10, 460 + size_t * 2))
        screen.blit(text_surface3, (10, 460 + size_t * 3 + 10))
        screen.blit(text_surface4, (10, 460 + size_t * 4 + 20))
        for e in entities2:
            screen.blit(e.image, camera.apply(e))
        animatedEntities2.update()
        button.draw(screen,hero,-1)
        pygame.display.update()
    return hero
level = []
entities = pygame.sprite.Group()
animatedEntities = pygame.sprite.Group() # все анимированные объекты, за исключением героя
platforms = [] # то, во что мы будем врезаться или опираться
PLATFORM_COLOR = "#000000"
test1 = 0