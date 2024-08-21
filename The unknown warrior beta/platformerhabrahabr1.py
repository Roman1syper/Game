import pygame
#from player import Player
from blocks import *
#from random import randint
#from time import sleep
from text import witch_t, slaim_bro_t, assistant_t, slaim_t, moon_t
from main import *
from anim import NPS_MOON,NPS_CRYSTAL, NPS_SLAIM_BRO,NPS_SLAIM_BRO2, NPS_SLAIM,NPS_SLAIM2, NPS_ASSISTANT,NPS_ASSISTANT2,NPS_WITCH,NPS_WITCH2,slaim_icon,slaim_icon2,slaim_bro_icon,slaim_bro_icon2,witch_icon,witch_icon2,assistant_icon,assistant_icon2
from platformerhabrahabr0 import main0
from platformerhabrahabr0_2 import main0_2
from platformerhabrahabr2 import main2 
from platformerhabrahabr3 import main3
from platformerhabrahabr4 import main4 
from platformerhabrahabr5 import main5
from platformerhabrahabr5_2 import main5_2
from platformerhabrahabr6 import main6
from platformerhabrahabr6_2 import main6_2
from platformerhabrahabr6_3 import main6_3
from platformerhabrahabr7 import main7
from platformerhabrahabr8 import main8
from platformerhabrahabr9 import main9
from platformerhabrahabr_end import main_end 
import json
pygame.init()

WIN_WIDTH = 800 
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#124290"
winner = True

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


def loadLevel():
    levelFile = open('lvl/1.txt')
    line = " "
    commands = []
    while line[0] != "/": # пока не нашли символ завершения файла
        line = levelFile.readline() #считываем построчно
        if line[0] == "[": # если нашли символ начала уровня
            while line[0] != "]": # то, пока не нашли символ конца уровня
                line = levelFile.readline() # считываем построчно уровень
                if line[0] != "]": # и если нет символа конца уровня
                    endLine = line.find("|") # то ищем символ конца строки
                    level.append(line[0: endLine]) # и добавляем в уровень строку от начала до символа "|"

        #if line[0] != "": # если строка не пустая
        # commands = line.split() # разбиваем ее на отдельные команды
        # if len(commands) > 1: # если количество команд > 1, то ищем эти команды
        #    if commands[0] == "player": # если первая команда - player
        #        playerX = int(commands[1]) # то записываем координаты героя
        #        playerY = int(commands[2])

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius) #круги
    surf.set_colorkey((0, 0, 0))
    return surf

def draw_health_bar(health, x, y, max,screen):
    ratio = health / max
    pygame.draw.rect(screen, (0,0,0), (x - 2, y - 2, 204, 34))
    pygame.draw.rect(screen, (200,0,0), (x, y, 200, 30))
    pygame.draw.rect(screen, (250,250,25), (x, y, 200 * ratio, 30))
def main(hero,screen,death_list):
    global level
    level = []
    entities = pygame.sprite.Group()
    entities2 = pygame.sprite.Group()
    entities3 = pygame.sprite.Group()
    break_object = pygame.sprite.Group()
    animatedEntities = pygame.sprite.Group()
    animatedEntities2 = pygame.sprite.Group()
    fait_character = []
    platforms = [] 
    loadLevel()

    left = right = False # по умолчанию - стоим
    up = down = False

    bg = Surface(DISPLAY)
    bg.fill((104,159,56))
    
    timer = pygame.time.Clock()
    x=y=0 # координаты
    random_tree = 0
    random_mushroom = 0
    random_mushroom2 = 0
    random_mushroom3 = 0
    random_grass = 0
    for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
                pf = Img_stat(x,y,32,32,'assets/other/not_in.png')
                platforms.append(pf)
            elif col == "=" and death_list['slaim_win'] != 1:
                s_pf = Img_stat(x,y,32,224,'assets/other/not_in.png')
                platforms.append(s_pf)
            elif col == "_" and hero.hard >= 3:
                pf = Img_stat(x,y,640,32,'assets/other/not_in.png')
                platforms.append(pf)
            elif col == "+" and death_list['slaim_bro_death'] != 1:
                pf_s = Img_stat(x,y,320,32,'assets/other/not_in.png')
                platforms.append(pf_s)
            elif col == "*":
                pf = Anim_img(x, y, 32, 32, NPS_CRYSTAL)
                animatedEntities.add(pf)
                entities.add(pf)
            elif col == " ":
                random_grass += 1
                number_grass = 0
                if random_grass % death_list['random'][2][0] == 0:
                    number_grass = 1
                elif random_grass % death_list['random'][2][1] == 0:
                    number_grass = 2
                elif random_grass % death_list['random'][2][2] == 0:
                    number_grass = 3
                elif random_grass % death_list['random'][2][3] == 0:
                    number_grass = 4
                elif random_grass % death_list['random'][2][4] == 0:
                    number_grass = 5
                elif random_grass % death_list['random'][2][5] == 0:
                    number_grass = 6
                elif random_grass % death_list['random'][2][6] == 0:
                    number_grass = 7
                elif random_grass % death_list['random'][2][7] == 0:
                    number_grass = 8
                elif random_grass % death_list['random'][2][8] == 0:
                    number_grass = 9
                elif random_grass % death_list['random'][2][9] == 0:
                    number_grass = 10
                if random_grass % death_list['random'][2][10] == 0:
                    flip_x = True
                else:
                    flip_x = False
                if number_grass != 0:
                    t = f'assets/grass/grass{number_grass}.png'
                    pf = Img_stat(x,y,32,32,t,flip_x)
                    entities.add(pf)
            elif col == "8":
                random_tree += 1
                if random_tree >= 21:
                    random_tree = 0
                tree_2 = 'assets/tree/tree_min1.png'
                hp_max = 0
                if random_tree % death_list['random'][0][2] == 0:
                    tree = 'assets/tree/tree_min4.png'
                    tree_2 = 'assets/tree/tree_min0.png'
                    hp = 20
                elif random_tree % death_list['random'][0][1] == 0:
                    tree = 'assets/tree/tree_min5.png'
                    hp = 16
                elif random_tree % death_list['random'][0][0] == 0:
                    tree = 'assets/tree/tree_min3.png'
                    hp = 12
                else:
                    tree = 'assets/tree/tree_min2.png'
                    hp = 10
                #flip1 = randint(1,2)
                if random_tree % death_list['random'][0][3] == 0:
                    flip_x = True
                else:
                    flip_x = False
                pf = Img_break(x - 22,y - 28,152,178,tree, 60, tree_2,hp,hp_max,0,flip_x)
                platforms.append(pf)
                entities3.add(pf)
                break_object.add(pf)
            elif col == "9" and hero.hard >= 4:
                tree = 'assets/tree/tree_min2.png'
                pf = Img_break(x - 22,y - 28,152,178,tree, 60, 'assets/tree/tree_min1.png',15,0)
                entities3.add(pf)
                platforms.append(pf)
                break_object.add(pf)
            elif col == "t":
                random_mushroom2 += 1
                if random_mushroom2 % death_list['random'][1][1] == 0:
                    mushroom = 'assets/tree/mushroom_min.png'
                    hp = -22
                    hp_max = 0
                elif random_mushroom2 % death_list['random'][1][0] == 0:
                    mushroom = 'assets/tree/mushroom_min_violet.png'
                    hp = -int(hero.health_max // 5)
                    hp_max = 3
                else:
                    mushroom = 'assets/tree/mushroom_min_gold.png'
                    hp = 20
                    hp_max = -5
                if random_mushroom2 % death_list['random'][1][2] == 0:
                    flip_x = True
                else:
                    flip_x = False
                pf = Img_break(x - 20,y - 23,72,78,mushroom,20,'assets/tree/mushroom_min_death.png',hp,hp_max,1,flip_x)
                break_object.add(pf)
                entities2.add(pf)
            elif col == "T":
                random_mushroom += 1
                if random_mushroom % death_list['random'][1][1] == 0:
                    mushroom = 'assets/tree/mushroom_violet.png'
                    hp = -int(hero.health_max // 4)
                    hp_max = 5
                elif random_mushroom % death_list['random'][1][0] == 0:
                    mushroom = 'assets/tree/mushroom_gold.png'
                    hp = 40
                    hp_max = -9
                else:
                    mushroom = 'assets/tree/mushroom.png'
                    hp = -33
                    hp_max = 0
                if random_mushroom % death_list['random'][1][2] == 0:
                    flip_x = True
                else:
                    flip_x = False
                pf = Img_break(x - 56,y - 62,144,156,mushroom,40,'assets/tree/mushroom_death.png',hp,hp_max,1,flip_x)
                entities2.add(pf)
                break_object.add(pf)
            elif col == "1":
                random_mushroom3 += 1
                if random_mushroom3 % death_list['random'][3][2] == 0:
                    flip_x = True
                else:
                    flip_x = False
                if random_mushroom3 % death_list['random'][3][0] == 0:
                    if random_mushroom3 >= 30 and random_mushroom3 <= 50:
                        mushroom = 'assets/tree/mushroom_min0.png'
                        hp = -int(hero.health_max // 10)
                        hp_max = 2
                    elif random_mushroom3 <= 20:
                        mushroom = 'assets/tree/mushroom_min1.png'
                        hp = 10
                        hp_max = -1
                    else:
                        mushroom = 'assets/tree/mushroom_min2.png'
                        hp = -10
                        hp_max = 0
                    pf = Img_break(x,y,32,32,mushroom,5,'assets/tree/mushroom_min3.png',hp,hp_max,1,flip_x)
                    entities2.add(pf)
                    break_object.add(pf)
                elif random_mushroom3 % death_list['random'][3][1] == 0:
                    if random_mushroom3 < 10 or (random_mushroom3 > 30 and random_mushroom3 < 50):
                        bush = 'assets/tree/bush2.png'
                    else:
                        bush = 'assets/tree/bush.png'
                    pf = Img_break(x,y,32,32,bush,10,'assets/tree/bush_without_foliage.png',2.5,0,flip_x)
                    entities2.add(pf)
                    break_object.add(pf)
            elif col == "B":
                slaim_bro = Dialogue_img(x,y - 5,96,32,NPS_SLAIM_BRO,NPS_SLAIM_BRO2,0,slaim_bro_icon,slaim_bro_icon2,0,9,30,1,'slaim_bro',slaim_bro_t)
                animatedEntities2.add(slaim_bro)
                entities2.add(slaim_bro)
                fait_character.append(slaim_bro)
            elif col == "W" and death_list['witch_win'] != 1 and death_list['assistant_quest'] != 1 and death_list['witch_dialogue'] == -1:
                w = Dialogue_img(x - 16,y - 32,64,96,NPS_WITCH,NPS_WITCH2,0,witch_icon,witch_icon2,0,5,27,1,'witch',witch_t,True)
                animatedEntities2.add(w)
                entities2.add(w)
                fait_character.append(w)
            elif col == "S":
                slaim = Dialogue_img(x - 32,y - 5,96,32,NPS_SLAIM,NPS_SLAIM2,0,slaim_icon,slaim_icon2,0,1,28,1,'slaim',slaim_t)
                animatedEntities2.add(slaim)
                entities2.add(slaim)
                fait_character.append(slaim)
            elif col == "A" and death_list['assistant_quest'] != 1 and death_list['witch_dialogue'] == -1:
                assistant = Dialogue_img(x - 16,y - 16,96,96,NPS_ASSISTANT,NPS_ASSISTANT2,0,assistant_icon,assistant_icon2,0,10,28,1,'assistant',assistant_t,False,False,True,90,90)
                animatedEntities2.add(assistant)
                entities2.add(assistant)
                fait_character.append(assistant)
   
            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT    #то же самое и с высотой
        x = 0                   #на каждой новой строчке начинаем с нуля
    for character in fait_character:
        character.death = death_list[f'{character.character}_death']
        character.win = death_list[f'{character.character}_win']
        character.quest = death_list[f'{character.character}_quest']
    total_level_width  = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
    total_level_height = len(level)*PLATFORM_HEIGHT   # высоту
    
    camera = Camera(camera_configure, total_level_width, total_level_height) 
    pygame.mixer.pre_init()
    pygame.time.set_timer(pygame.USEREVENT, 120)
    #font = pygame.font.Font(None, 36)
    button1 = Img_button(760,10,32,32,'assets/button/pause.png','assets/button/pause2.png')
    button2 = Img_button(250,400,300,130,'assets/button/home.png','assets/button/home2.png')
    pause_b = Img_stat2(0,0,800,640,'assets/other/pause.png')
    slider = Img_t(250,225,'assets/button/test1.png','assets/button/test2.png')
    slider2 = Img_t(250,350,'assets/button/test1.png','assets/button/test2.png')
    text = ['громкость музыки:','громкость эффектов:']
    score_font = pygame.font.Font("fonts/game.ttf", 28)
    score_font2 = pygame.font.Font("fonts/game.ttf", 25)
    t = 0
    while not hero.winner:
        timer.tick(60)
        screen.blit(bg,(0,0))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_d and hero.pause == -1:
                if hero.attacking == False:
                    g = hero.test(screen,camera.state)
                    break_object.update(g,hero)
                    for character in fait_character:
                        if pygame.sprite.collide_rect(g,character):
                            if character.death != 1 and character.win != 1:
                                character.dialogue = 1
                                test = fait(screen,hero,character.fait)
                                hero.health = test[0]
                                character.win = test[1]
                                death_list[f'{character.character}_win'] = test[1]
                                if death_list['slaim_death'] != 1:
                                    if slaim.win == 1:
                                        s_pf.rect.x += 500
                                if death_list['witch_win'] == 1:
                                    death_list['assistant_quest'] = -1
                                    death_list['fire_mag_quest2'] = 1
                                right = False
                                left = False
                                down = False
                                up = False
                                pygame.mixer.music.load("sound/sound_son.mp3")
                                pygame.mixer.music.set_volume(hero.musec)
                                pygame.mixer.music.play(-1, 0.0, 5000)
                            elif character.win == 1:
                                death_list[f'{character.character}_death'] = 1
                                character.death = 1
                                if death_list['slaim_bro_death'] == 1:
                                    slaim.quest = 1
                                    slaim.dialogue = 1
                                    pf_s.rect.y -= 300
                                    death_list[f'{slaim.character}_quest'] = 1
                hero.attack_type = 1
            if e.type == KEYUP and e.key == K_RIGHT or hero.pause == 1:
                right = False
            if e.type == KEYUP and e.key == K_LEFT or hero.pause == 1:
                left = False
            if e.type == KEYUP and e.key == K_DOWN or hero.pause == 1:
                down = False
            if e.type == KEYUP and e.key == K_UP or hero.pause == 1:
                up = False
        if death_list['witch_death'] != 1 and death_list['assistant_quest'] != 1:
            for character in fait_character:
                if character.character == 'witch':
                    if pygame.sprite.collide_rect(hero,w):
                        if death_list['assistant_death'] != 1:
                            assistant.quest = 1
                            assistant.dialogue = 1
                        death_list['assistant_quest'] = 1
                        death_list['witch_dialogue'] = 1
        if death_list['witch_death'] != 1 and death_list['witch_quest'] != 1:
            if hero.health >= hero.health_max - 20:
                for character in fait_character:
                    if character.character == 'witch':
                        w.quest = 1
                        w.dialogue = 1
                        death_list['witch_quest'] = 1
        if death_list['slaim_bro_death'] != 1:
            if slaim_bro.quest == 1 and t == 0:
                t = 1
                s_pf.rect.x += 500
        camera.update(hero) 
        animatedEntities.update() 
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        hero.draw(screen, camera.state, circle_surf)
        hero.update(left, right, up, down, screen, platforms, camera.state)
        for e in entities2:
            screen.blit(e.image, camera.apply(e))
        for e in entities3:
            screen.blit(e.image, (camera.apply(e)[0] - e.rect.width * 0.3,camera.apply(e)[1] - (e.rect.height * 0.15)))
        draw_health_bar(hero.health, 10, 10,hero.health_max,screen)
        text_surface_hp = score_font2.render(f'{int(hero.health)}', False, (20, 20, 20)) #/{int(hero.health_max)}
        text_surface_hp2 = score_font2.render('/', False, (20, 20, 20))
        text_surface_hp3 = score_font2.render(f'{int(hero.health_max)}', False, (20, 20, 20))
        screen.blit(text_surface_hp,(50,10))
        screen.blit(text_surface_hp2,(100,10))
        screen.blit(text_surface_hp3,(120,10))
        animatedEntities2.update(hero,screen)
        button1.draw(screen,hero,1)
        if hero.pause == 1:
            pause_b.draw(screen)
            button2.draw(screen,hero,2)
            text_surface = score_font.render(text[0], False, (230, 230, 230))
            screen.blit(text_surface,(225,175))
            text_surface2 = score_font.render(text[1], False, (230, 230, 230))
            screen.blit(text_surface2,(210,300))
            g = hero.musec
            g2 = hero.effect
            hero.musec = slider.draw(screen,hero.musec)
            hero.effect = slider2.draw(screen,hero.effect)
            if g != hero.musec or g2 != hero.effect:
                pygame.mixer.music.set_volume(hero.musec)
                hero.attack_sound.set_volume(hero.effect)
        if hero.health <= 0:
            hero.winner = True
        if hero.rect.x >= total_level_width:
            hero.rect.x = 80
            hero.rect.y = 1210
            hero.location = 4
            hero.winner = True
        elif hero.rect.y >= total_level_height:
            hero.rect.x = 170
            hero.rect.y = 100
            hero.location = 2
            hero.winner = True
        elif hero.rect.y < 0:
            hero.rect.x = 210
            hero.rect.y = 700
            hero.location = 20
            hero.winner = True
        elif hero.rect.x < 0:
            hero.rect.x = 1350
            hero.rect.y = 300
            hero.location = 0
            hero.winner = True
        pygame.display.update()
    if death_list['fire_mag_quest'] == 1 and death_list['fire_mag_win'] != 1 and death_list['fire_mag_win2'] != 1:
        death_list['location'] += 1
    return hero
level = []
entities = pygame.sprite.Group()
animatedEntities = pygame.sprite.Group() # все анимированные объекты, за исключением героя
platforms = [] # то, во что мы будем врезаться или опираться
PLATFORM_COLOR = "#000000"

def play(hero,screen,death_list):
    test1 = 0
    while test1 != 1:
        if (hero.location == 1 and hero.health > 0 and hero.end == -1) or (death_list['moon'] == 1 and hero.health <= 0 and hero.end == -1):
            hero.winner = False  
            if death_list['moon'] == 1 and hero.health <= 0:
                hero.rect.x = 300
                hero.rect.y = 300
                hero.health = 1
                with open('save.txt') as load_file:
                    death_list = json.load(load_file)
            main(hero,screen,death_list)
        elif hero.location == 0 and hero.health > 0: 
            hero.winner = False  
            main0(hero,screen,death_list)
        elif hero.location == 20 and hero.health > 0: 
            hero.winner = False  
            main0_2(hero,screen,death_list)
        elif (hero.location == 2 and hero.health > 0 and hero.end == -1) or (death_list['moon'] == 2 and hero.health <= 0 and hero.end == -1): 
            hero.winner = False  
            if death_list['moon'] == 2 and hero.health <= 0:
                hero.rect.x = 200
                hero.rect.y = 400
                hero.health = 10
                with open('save.txt') as load_file:
                    death_list = json.load(load_file)
            main2(hero,screen,death_list)
        elif hero.location == 3 and hero.health > 0: 
            hero.winner = False  
            main3(hero,screen,death_list)
        elif hero.location == 4 and hero.health > 0: 
            hero.winner = False  
            main4(hero,screen,death_list)
        elif (hero.location == 5 and hero.health > 0 and hero.end == -1) or (death_list['moon'] == 3 and hero.health <= 0 and hero.end == -1): 
            hero.winner = False  
            if death_list['moon'] == 3 and hero.health <= 0:
                hero.rect.x = 200
                hero.rect.y = 400
                hero.health = 10
                with open('save.txt') as load_file:
                    death_list = json.load(load_file)
            main5(hero,screen,death_list)
        elif hero.location == 52 and hero.health > 0: 
            hero.winner = False  
            main5_2(hero,screen,death_list)
        elif hero.location == 6 and hero.health > 0: 
            hero.winner = False  
            main6(hero,screen,death_list)
        elif hero.location == 62 and hero.health > 0: 
            hero.winner = False  
            main6_2(hero,screen,death_list)
        elif hero.location == 63 and hero.health > 0: 
            hero.winner = False  
            main6_3(hero,screen,death_list)
        elif hero.location == 7 and hero.health > 0: 
            hero.winner = False  
            main7(hero,screen,death_list)
        elif hero.location == 8 and hero.health > 0: 
            hero.winner = False  
            main8(hero,screen,death_list)
        elif hero.location == 9 and hero.health > 0: 
            hero.winner = False  
            main9(hero,screen,death_list)
        elif hero.health <= 0 and hero.end != -1:
            hero.winner = False  
            main_end(hero,screen,death_list)
            test1 = 1 
        else:
            test1 = 1 