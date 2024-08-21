import pygame
#from player import Player
from blocks import *
from random import randint
from text import witch_t2, people_t1,people_1t1,people_t1_1, people_t2,people_2t1,people_t2_1, people_t3,people_3t1,people_t3_1, fire_mag_t,fire_mag_t1, worm_t
from main import *
from anim import NPS_CRYSTAL, NPS_FIRE_MAG,NPS_FIRE_MAG2,NPS_FIRE_MAG3,NPS_FIRE_MAG4, NPS_PEOPLE1_1,NPS_PEOPLE1_2,NPS_PEOPLE1_3, NPS_PEOPLE2_1,NPS_PEOPLE2_2,NPS_PEOPLE2_3, NPS_PEOPLE3_1,NPS_PEOPLE3_2,NPS_PEOPLE3_3, NPS_WITCH,NPS_WITCH2, NPS_WORM,NPS_WORM1,NPS_WORM2, witch_icon,witch_icon2, fire_mag_icon,fire_mag_icon2,fire_mag_icon3, people_icon1_1,people_icon1_2,people_icon1_3, people_icon2_1,people_icon2_2,people_icon2_3, people_icon3_1,people_icon3_2,people_icon3_3, worm_icon,worm_icon2,worm_icon3
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


def loadLevel():
    global playerX, playerY 
    levelFile = open('lvl/4.txt')
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

        if line[0] != "": # если строка не пустая
         commands = line.split() # разбиваем ее на отдельные команды
         if len(commands) > 1: # если количество команд > 1, то ищем эти команды
            if commands[0] == "player": # если первая команда - player
                playerX = int(commands[1]) # то записываем координаты героя
                playerY = int(commands[2])

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius) #круги
    surf.set_colorkey((0, 0, 0))
    return surf

def draw_health_bar(health, x, y,screen,max):
    ratio = health / max
    pygame.draw.rect(screen, (0,0,0), (x - 2, y - 2, 204, 34))
    pygame.draw.rect(screen, (200,0,0), (x, y, 200, 30))
    pygame.draw.rect(screen, (250,250,25), (x, y, 200 * ratio, 30))
def main4(hero,screen,death_list):
    global level
    #print(4)
    level = []
    entities = pygame.sprite.Group()
    entities2 = pygame.sprite.Group()
    entities3 = pygame.sprite.Group()
    entities4 = pygame.sprite.Group()
    break_object = pygame.sprite.Group()
    animatedEntities = pygame.sprite.Group()
    animatedEntities2 = pygame.sprite.Group()
    platforms = [] 
    fait_character = []
    fait_worm = []
    loadLevel()

    left = right = False # по умолчанию - стоим
    up = down = False
    attaka = 0
    bg = Surface(DISPLAY)
    bg.fill((104,159,56))
    number = 0
    number2 = 0
    
    timer = pygame.time.Clock()
    x=y=0 # координаты
    random_tree = 8
    random_mushroom = 8
    random_mushroom2 = 8
    random_mushroom3 = 8
    random_grass = 8
    for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
                pf = Img_stat(x,y,32,32,'assets/other/not_in.png')
                platforms.append(pf)
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
            elif col == "#":
                random1 = randint(11,13)
                flip1 = randint(1,2)
                if flip1 == 1:
                    flip_x = True
                else:
                    flip_x = False
                flip1 = randint(1,2)
                if flip1 == 1:
                    flip_y = True
                else:
                    flip_y = False
                t = f'assets/grass/grass{random1}.png'
                pf = Img_stat(x,y,32,32,t,flip_x,flip_y)
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
            elif col == "9" and hero.hard >= 2:
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
                if random_mushroom3 % death_list['random'][3][1] == 0:
                    if random_mushroom < 10 or (random_mushroom > 30 and random_mushroom < 50):
                        bush = 'assets/tree/bush2.png'
                    else:
                        bush = 'assets/tree/bush.png'
                    pf = Img_break(x,y,32,32,bush,10,'assets/tree/bush_without_foliage.png',2.5,0,flip_x)
                    entities2.add(pf)
                    break_object.add(pf)
            elif col == ">":
                number += 1
                if death_list['fire_mag_quest'] == 1 and death_list['fire_mag_win'] != 1 and death_list['location'] >= 15 and death_list['fire_mag_win2'] != 1:
                    if number == 5:
                        number = 1
                    pf = Img_stat(x - 64,y - 90,188,180,f'assets/building/house_{number}.png')
                else:
                    if number == 8:
                        number = 1
                    pf = Img_stat(x - 64,y - 90,188,180,f'assets/building/house{number}.png')
                entities4.add(pf)
                platforms.append(pf)
            elif col == "W" and death_list['witch_win'] != 1 and death_list['assistant_quest'] == 1 and death_list['witch_dialogue'] == 1:
                w = Dialogue_img(x - 16,y - 32,64,96,NPS_WITCH,NPS_WITCH2,0,witch_icon,witch_icon2,0,5,27,4,'witch',witch_t2)
                animatedEntities2.add(w)
                entities2.add(w)
                fait_character.append(w)
            if col == "F" and death_list['fire_mag_win'] != 1 and death_list['assistant_quest'] == 1 and death_list['fire_mag_quest'] == -1 and death_list['witch_dialogue'] == 1:
                fire_mag = Dialogue_img(x - 16,y - 32,135,105,NPS_FIRE_MAG,NPS_FIRE_MAG3,0,fire_mag_icon,fire_mag_icon2,0,6,27,3,'fire_mag',fire_mag_t,True,False,True,145,105)
                animatedEntities2.add(fire_mag)
                entities2.add(fire_mag)
                fait_character.append(fire_mag)
            elif col == "f" and death_list['fire_mag_win'] != 1 and death_list['assistant_quest'] != 1 and death_list['fire_mag_quest'] == -1:
                fire_mag = Dialogue_img(x - 16,y - 32,135,105,NPS_FIRE_MAG,NPS_FIRE_MAG3,0,fire_mag_icon,fire_mag_icon2,0,6,27,3,'fire_mag',fire_mag_t1,True,False,True,145,105)
                animatedEntities2.add(fire_mag)
                entities2.add(fire_mag)
                fait_character.append(fire_mag)
            if death_list['fire_mag_quest'] == 1 and death_list['fire_mag_win'] != 1 and death_list['fire_mag_win2'] != 1 and death_list['location'] < 15:
                if col == "v":
                    number2 += 1
                    if death_list[f'people{number2}_death'] != 1:
                        worm = Anim_img2(x - 32,y - 50,144,112,NPS_WORM,NPS_WORM1,2,True,False,True,144,112,f'people{number2}-2')
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_worm.append(worm)
                    else:
                        worm = Dialogue_img(x - 32,y - 50,144,112,NPS_WORM,NPS_WORM1,0,worm_icon,worm_icon3,0,4,27,3,f'worm{number2}',worm_t,True,False,True,144,112)
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_character.append(worm)
                elif col == "V":
                    number2 += 1
                    if death_list[f'people{number2}_death'] != 1:
                        worm = Anim_img2(x - 32,y - 50,144,112,NPS_WORM,NPS_WORM1,2,False,False,True,135,105,f'people{number2}-2')
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_worm.append(worm)
                    else:
                        worm = Dialogue_img(x - 32,y - 50,144,112,NPS_WORM,NPS_WORM1,0,worm_icon,worm_icon3,0,4,27,3,f'worm{number2}',worm_t,False,False,True,144,112)
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_character.append(worm)
            elif death_list['fire_mag_quest'] == 1 and death_list['fire_mag_win2'] == 1 and death_list['fire_mag_win'] != 1 and death_list['location'] < 15:
                if col == "v":
                    number2 += 1
                    if death_list[f'people{number2}_death'] != 1:
                        worm = Anim_img2(x - 32,y - 50,162,126,NPS_WORM2,NPS_WORM1,2,True,False,True,162,126,f'people{number2}-2')
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_worm.append(worm)
                    else:
                        worm = Dialogue_img(x - 32,y - 50,162,126,NPS_WORM2,NPS_WORM1,0,worm_icon2,worm_icon3,0,4,27,3,f'worm{number2}',worm_t,True,False,True,162,126)
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_character.append(worm)
                if col == "V":
                    number2 += 1
                    if death_list[f'people{number2}_death'] != 1:
                        worm = Anim_img2(x - 32,y - 50,171,133,NPS_WORM2,NPS_WORM1,2,False,False,True,171,133,f'people{number2}-2')
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_worm.append(worm)
                    else:
                        worm = Dialogue_img(x - 32,y - 50,171,133,NPS_WORM2,NPS_WORM1,0,worm_icon2,worm_icon3,0,4,27,3,f'worm{number2}',worm_t,False,False,True,171,133)
                        animatedEntities2.add(worm)
                        entities2.add(worm)
                        fait_character.append(worm)
            if death_list['fire_mag_quest'] == 1 and death_list['fire_mag_win'] != 1 and death_list['location'] < 15:
                if col == "P" and death_list['people1_death'] != 1:
                    people1 = Dialogue_img(x - 64,y - 64,166,125,NPS_PEOPLE1_2,NPS_PEOPLE1_1,NPS_PEOPLE1_1, people_icon1_2,people_icon1_1,people_icon1_1,414,27,3,'people1-2',people_t1,False,False,True,166,125,0.13)
                    animatedEntities2.add(people1)
                    entities2.add(people1)
                    fait_character.append(people1)
                    if death_list['fire_mag_win2'] == 1:
                        people1.fait = 4414
                if col == "p" and death_list['people2_death'] != 1:
                    people2 = Dialogue_img(x - 96,y - 86,204,129,NPS_PEOPLE2_2,NPS_PEOPLE2_1,NPS_PEOPLE2_1, people_icon2_2,people_icon2_1,people_icon2_1,415,27,3,'people2-2',people_t2,True,False,True,204,129,0.12)
                    animatedEntities2.add(people2)
                    entities2.add(people2)
                    fait_character.append(people2)
                    if death_list['fire_mag_win2'] == 1:
                        people2.fait = 4415
                if col == "e" and death_list['people3_death'] != 1:
                    people3 = Dialogue_img(x - 64,y - 64,225,120,NPS_PEOPLE3_2,NPS_PEOPLE3_1,NPS_PEOPLE3_1, people_icon3_2,people_icon3_1,people_icon3_1,416,27,3,'people3-2',people_t3,False,False,True,225,120,0.11)
                    animatedEntities2.add(people3)
                    entities2.add(people3)
                    fait_character.append(people3)
                    if death_list['fire_mag_win2'] == 1:
                        people3.fait = 4416
            elif death_list['fire_mag_quest'] == 1 and death_list['fire_mag_win'] != 1 and death_list['location'] >= 15:
                if col == "P":
                    people1 = Dialogue_img(x - 64,y - 64,166,125,NPS_PEOPLE1_1,NPS_PEOPLE1_3,0, people_icon1_1,people_icon1_3,0,14,27,3,'people1-2',people_t1_1,False,False,True,166,125)
                    animatedEntities2.add(people1)
                    entities2.add(people1)
                    fait_character.append(people1)
                if col == "p":
                    people2 = Dialogue_img(x - 96,y - 86,204,129,NPS_PEOPLE2_1,NPS_PEOPLE2_3,0, people_icon2_1,people_icon2_3,0,15,27,3,'people2-2',people_t2_1,True,False,True,204,129)
                    animatedEntities2.add(people2)
                    entities2.add(people2)
                    fait_character.append(people2)
                if col == "e":
                    people3 = Dialogue_img(x - 64,y - 64,225,120,NPS_PEOPLE3_1,NPS_PEOPLE3_3,0, people_icon3_1,people_icon3_3,0,16,27,3,'people3-2',people_t3_1,False,False,True,225,120)
                    animatedEntities2.add(people3)
                    entities2.add(people3)
                    fait_character.append(people3)
            else:
                if col == "P":
                    people1 = Dialogue_img(x - 64,y - 64,166,125,NPS_PEOPLE1_1,NPS_PEOPLE1_3,0, people_icon1_1,people_icon1_3,0,14,27,3,'people1',people_1t1,True,False,True,166,125,0.13)
                    animatedEntities2.add(people1)
                    entities2.add(people1)
                    fait_character.append(people1)
                if col == "p":
                    people2 = Dialogue_img(x - 96,y - 86,203,129,NPS_PEOPLE2_1,NPS_PEOPLE2_3,0, people_icon2_1,people_icon2_3,0,15,27,3,'people2',people_2t1,True,False,True,203,129,0.12)
                    animatedEntities2.add(people2)
                    entities2.add(people2)
                    fait_character.append(people2)
                if col == "e":
                    people3 = Dialogue_img(x - 64,y - 64,225,120,NPS_PEOPLE3_1,NPS_PEOPLE3_3,0, people_icon3_1,people_icon3_3,0,16,27,3,'people3',people_3t1,False,False,True,225,120,0.11)
                    animatedEntities2.add(people3)
                    entities2.add(people3)
                    fait_character.append(people3)
   
            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT    #то же самое и с высотой
        x = 0                   #на каждой новой строчке начинаем с нуля
    number2 = 0
    for worm in fait_worm:
        number2 += 1
        worm.win = death_list[f'people{number2}-2_win']
    for character in fait_character:
        character.death = death_list[f'{character.character}_death']
        if death_list['location'] >= 15 and 'people' in character.character and death_list['fire_mag_win2'] != 1:
            character.win = -death_list[f'{character.character}_win']
        else:
            if (death_list['worm1_win'] == 1 or death_list['people1-2_win'] == 1) and (death_list['worm2_win'] == 1 or death_list['people2-2_win'] == 1) and (death_list['worm3_win'] == 1 or death_list['people3-2_win'] == 1):
                character.win = death_list[f'{character.character}_win']
        if character.character == 'witch':
            character.quest = death_list[f'{character.character}_quest2']
            character.quest2 = death_list[f'{character.character}_quest2_2']
        elif character.text in fire_mag_t:
            character.quest = death_list[f'{character.character}_quest2']
        else:
            character.quest = death_list[f'{character.character}_quest']
    total_level_width  = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
    total_level_height = len(level)*PLATFORM_HEIGHT   # высоту
    
    camera = Camera(camera_configure, total_level_width, total_level_height) 
    pygame.mixer.pre_init()
    pygame.time.set_timer(pygame.USEREVENT, 120)
    font = pygame.font.Font(None, 36)

    button1 = Img_button(760,10,32,32,'assets/button/pause.png','assets/button/pause2.png')
    button2 = Img_button(250,400,300,130,'assets/button/home.png','assets/button/home2.png')
    pause_b = Img_stat2(0,0,800,640,'assets/other/pause.png')
    slider = Img_t(250,225,'assets/button/test1.png','assets/button/test2.png')
    slider2 = Img_t(250,350,'assets/button/test1.png','assets/button/test2.png')
    text = ['громкость музыки:','громкость эффектов:']
    score_font = pygame.font.Font("fonts/game.ttf", 28)
    score_font2 = pygame.font.Font("fonts/game.ttf", 25)
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
                    for character in fait_character:
                        if pygame.sprite.collide_rect(g,character):
                            if character.death != 1 and character.win != 1:
                                character.dialogue = 1
                                test = fait(screen,hero,character.fait)
                                hero.health = test[0]
                                character.win = test[1]
                                death_list[f'{character.character}_win'] = test[1]
                                for worm in fait_worm:
                                    if worm.character == character.character:
                                        worm.win = death_list[f'{character.character}_win']
                                right = False
                                left = False
                                down = False
                                up = False
                                if death_list['witch_win'] == 1:
                                    death_list['fire_mag_quest2'] = 1
                                    if death_list['fire_mag_win'] != 1 and death_list['fire_mag_quest'] != 1:
                                        fire_mag.dialogue = 1
                                        fire_mag.quest = 1
                                pygame.mixer.music.load("sound/sound_son.mp3")
                                pygame.mixer.music.set_volume(hero.musec)
                                pygame.mixer.music.play(-1, 0.0, 5000)
                            elif character.win == 1 and not 'people1-2' in character.character and not 'people2-2' in character.character and not 'people3-2' in character.character:
                                death_list[f'{character.character}_death'] = 1
                                character.death = 1
                    break_object.update(g,hero)
                hero.attack_type = 1

            if e.type == KEYUP and e.key == K_RIGHT or hero.pause == 1:
                right = False
            if e.type == KEYUP and e.key == K_LEFT or hero.pause == 1:
                left = False
            if e.type == KEYUP and e.key == K_DOWN or hero.pause == 1:
                down = False
            if e.type == KEYUP and e.key == K_UP or hero.pause == 1:
                up = False
        if death_list['fire_mag_death'] != 1 and death_list['assistant_quest'] != 1 and death_list['fire_mag_quest'] == -1:
            if pygame.sprite.collide_rect(hero,fire_mag):
                fire_mag.quest = 1
                death_list['fire_mag_quest'] = 1
                death_list['witch_quest2_2'] = 1
        if death_list['witch_death'] != 1 and death_list['witch_dialogue'] != 2 and death_list['assistant_quest'] == 1:
            for character in fait_character:
                if character.character == 'witch':
                    if pygame.sprite.collide_rect(hero,w):
                        death_list['witch_dialogue'] = 2
        #score_text = font.render(f'Монеты: {hero.score}', True, (240, 215, 0))
        #screen.blit(score_text, (10, 60))
        camera.update(hero) 
        animatedEntities.update() 
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        for e in entities4:
            screen.blit(e.image, camera.apply(e))
        hero.draw(screen, camera.state, circle_surf)
        hero.update(left, right, up, down, screen, platforms, camera.state)
        for e in entities2:
            screen.blit(e.image, camera.apply(e))
        for e in entities3:
            screen.blit(e.image, (camera.apply(e)[0] - e.rect.width * 0.3,camera.apply(e)[1] - (e.rect.height * 0.15)))
        draw_health_bar(hero.health, 10, 10,screen,hero.health_max)
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
            screen.blit(text_surface, (225,175))
            text_surface2 = score_font.render(text[1], False, (230, 230, 230))
            screen.blit(text_surface2, (210,300))
            g = hero.musec
            g2 = hero.effect
            hero.musec = slider.draw(screen,hero.musec)
            hero.effect = slider2.draw(screen,hero.effect)
            if g != hero.musec or g2 != hero.effect:
                pygame.mixer.music.set_volume(hero.musec)
                hero.attack_sound.set_volume(hero.effect)
        if hero.health <= 0:
            hero.winner = True
        if hero.rect.x < 0:
            hero.location = 1
            hero.winner = True
            hero.rect.x = 2300 
            hero.rect.y = 550
        if hero.rect.y > total_level_height:
            hero.location = 3
            hero.winner = True
            hero.rect.x = 250 
            hero.rect.y = 100
        if hero.rect.x >= total_level_width and hero.rect.y <= 700:
            hero.rect.x = 80
            #hero.rect.y = 170
            hero.location = 5
            hero.winner = True
        if hero.rect.x >= total_level_width and hero.rect.y > 700:
            hero.rect.x = 20
            hero.rect.y = 740
            hero.location = 6
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
test1 = 0
#hero = Player(1, 100, 384, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)