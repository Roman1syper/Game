import pygame
#from player import Player
from blocks import *
from random import randint
from text import tree_slaim_2t1,tree_slaim_2t2,tree_slaim_2t3, ninja_2t1,ninja_2t2,ninja_2t3, slaim_2t, slaim_farmer_t
from main import *
from anim import NPS_SLAIM_TREE, NPS_SLAIM_TREE2, NPS_SLAIM_TREE3, NPS_CRYSTAL, NPS_NINJA_1, NPS_NINJA_2_1
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
    levelFile = open('lvl/3.txt')
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
def main3(hero,screen,death_list):
    global level
    #print(3)
    level = []
    entities = pygame.sprite.Group()
    entities2 = pygame.sprite.Group()
    entities3 = pygame.sprite.Group()
    entities4 = pygame.sprite.Group()
    break_object = pygame.sprite.Group()
    animatedEntities = pygame.sprite.Group()
    animatedEntities2 = pygame.sprite.Group()
    fait_character = []
    platforms = [] 
    vegetables = []
    loadLevel()

    left = right = False # по умолчанию - стоим
    up = down = False
    attaka = 0
    bg = Surface(DISPLAY)
    bg.fill((104,159,56))
    
    slaim_icon = 'assets/monsters/Slaim_bro/tree_slaim_icon.png'
    slaim_icon2 = 'assets/monsters/Slaim_bro/tree_slaim_icon3.png'
    slaim_icon3 = 'assets/monsters/Slaim_bro/tree_slaim_icon2.png'

    ninja_icon = 'assets/monsters/Ninja/ninja_icon2.png'
    ninja_icon2 = 'assets/monsters/Ninja/ninja_icon2_2.png'
    
    timer = pygame.time.Clock()
    x=y=0 # координаты
    text = 0
    number = 0
    tree_num = 0
    tree_slaim_2t = [tree_slaim_2t1,tree_slaim_2t2,tree_slaim_2t3]
    random_tree = 9
    random_mushroom = 9
    random_mushroom2 = 9
    random_mushroom3 = 9
    random_grass = 9
    for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
                pf = Img_stat(x,y,32,32,'assets/other/not_in.png')
                platforms.append(pf)
            elif col == "=":
                pf1 = Img_stat(x,y,640,32,'assets/other/not_in.png')
                platforms.append(pf1)
            elif col == "/":
                pf2 = Img_stat(x + 64,y,32,400,'assets/other/not_in.png')
                platforms.append(pf2)
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
            elif col == "+":
                random1 = randint(0,1)
                flip1 = randint(1,2)
                if random1 == 0:
                    t = 'assets/grass/grass_eggplant1.png'
                else:
                    t = 'assets/grass/grass_eggplant2.png'
                if flip1 == 1:
                    flip_x = True
                else:
                    flip_x = False
                pf = Img_break(x,y,32,32,t,1,'assets/grass/grass_eggplant3.png',30,0,0,flip_x)
                entities.add(pf)
                vegetables.append(pf)
                break_object.add(pf)
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
            elif col == "9" and hero.hard >= 3:
                tree = 'assets/tree/tree_min2.png'
                tree_2 = 'assets/tree/tree_min1.png'
                pf = Img_break(x - 22,y - 28,152,178,tree, 60, tree_2,hp,hp_max,0,flip_x)
                platforms.append(pf)
                entities3.add(pf)
                break_object.add(pf)
            elif col == "?":
                tree = 'assets/tree/tree_min5.png'
                tree_2 = 'assets/tree/tree_min1.png'
                pf_ninja = Img_break(x - 22,y - 28,152,178,tree, 60, tree_2,hp,hp_max,0,flip_x)
                platforms.append(pf_ninja)
                entities3.add(pf_ninja)
                break_object.add(pf_ninja)
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
            elif col == "N":
                ninja3 = Dialogue_img(x - 80,y - 52,166,88,NPS_NINJA_1, NPS_NINJA_2_1,0,ninja_icon,ninja_icon2,0,33,28,3,'ninja2_3',ninja_2t3,False,False,True,166,88)
                animatedEntities2.add(ninja3)
                entities2.add(ninja3)
                fait_character.append(ninja3)
            elif col == "n":
                ninja2 = Dialogue_img(x - 80,y - 52,170,90,NPS_NINJA_1, NPS_NINJA_2_1,0,ninja_icon,ninja_icon2,0,33,28,3,'ninja2_2',ninja_2t2,True,False,True,170,90)
                animatedEntities2.add(ninja2)
                entities2.add(ninja2)
                fait_character.append(ninja2)
            elif col == "H":
                ninja1 = Dialogue_img(x - 80,y - 52,174,92,NPS_NINJA_1, NPS_NINJA_2_1,0,ninja_icon,ninja_icon2,0,3,28,3,'ninja2_1',ninja_2t1,True,False,True,174,92)
                animatedEntities2.add(ninja1)
                entities2.add(ninja1)
                fait_character.append(ninja1)
            elif col == "S":
                S = Dialogue_img(x - 5,y - 5,52,55,NPS_SLAIM_TREE,NPS_SLAIM_TREE2,NPS_SLAIM_TREE3,slaim_icon,slaim_icon2,slaim_icon3,12,28,3,'slaim_natural',slaim_2t)
                animatedEntities2.add(S)
                entities2.add(S)
                fait_character.append(S)
            elif col == "F":
                farmer = Dialogue_img(x - 5,y - 5,52,55,NPS_SLAIM_TREE,NPS_SLAIM_TREE2,NPS_SLAIM_TREE2,slaim_icon,slaim_icon2,slaim_icon2,13,28,3,'slaim_farmer',slaim_farmer_t)
                animatedEntities2.add(farmer)
                entities2.add(farmer)
                fait_character.append(farmer)
            elif col == "s":
                flip1 = randint(1,2)
                if flip1 == 1:
                    flip_x = True
                else:
                    flip_x = False
                tree_num += 1
                if tree_num >= len(tree_slaim_2t):
                    tree_num = 0
                s = Dialogue_img(x - randint(-30,30),y - randint(-10,10),52,55,NPS_SLAIM_TREE3,NPS_SLAIM_TREE2,NPS_SLAIM_TREE3,slaim_icon3,slaim_icon2,slaim_icon3,12,28,3,'slaim_rustic',tree_slaim_2t[tree_num],flip_x)
                animatedEntities2.add(s)
                entities2.add(s)
                fait_character.append(s)
                text += 1
            elif col == "^":
                pf = Img_stat(x - 200,y - 160,570,390,'assets/building/house.png')
                entities2.add(pf)
                platforms.append(pf)
            elif col == ">":
                number += 1
                pf = Img_stat(x - 64,y - 90,188,180,f'assets/building/house{number}.png')
                entities4.add(pf)
                platforms.append(pf)
   
            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT    #то же самое и с высотой
        x = 0                   #на каждой новой строчке начинаем с нуля
    slaim_tree_number = 0
    for character in fait_character:
        if character.character != 'slaim_rustic':
            character.death = death_list[f'{character.character}_death']
            character.win = death_list[f'{character.character}_win']
            character.quest = death_list[f'{character.character}_quest']
        else:
            death = death_list[f'{character.character}_death']
            win = death_list[f'{character.character}_win']
            quest = death_list[f'{character.character}_quest']
            character.death = death[slaim_tree_number]
            character.win = win[slaim_tree_number]
            character.quest = quest[slaim_tree_number]
            slaim_tree_number += 1

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
                    break_object.update(g,hero)
                    for eggplant in vegetables:
                        if pygame.sprite.collide_rect(g,eggplant):
                            if death_list['slaim_farmer_death'] != 1:
                                farmer.quest2 += 0.2
                                if farmer.quest2 >= 1 and farmer.quest2 < 3:
                                    farmer.quest = 1
                                    farmer.dialogue = 1
                    for character in fait_character:
                        if pygame.sprite.collide_rect(g,character):
                            if character.death != 1 and character.win != 1:
                                character.dialogue = 1
                                test = fait(screen,hero,character.fait)
                                hero.health = test[0] 
                                character.win = test[1]
                                if character.character == 'slaim_natural' and ninja3.dialogue == 2:
                                    ninja2.quest = 1
                                    ninja2.dialogue = 1
                                    death_list['ninja2_2_quest'] = 1
                                    ninja3.quest = 1
                                    ninja3.dialogue = 1
                                    death_list['ninja2_3_quest'] = 1
                                    pf_ninja.rect.y -= 400
                                if character.character == 'ninja2_2':
                                    ninja3.win = test[1]
                                    if death_list['slaim_natural_death'] != 1:
                                        S.quest = 1
                                        S.dialogue = 1
                                    death_list['ninja2_3_win'] = test[1]
                                    ninja3.dialogue = 1
                                if character.character == 'ninja2_3':
                                    ninja2.win = test[1]
                                    if death_list['slaim_natural_death'] != 1:
                                        S.quest = 1
                                        S.dialogue = 1
                                    death_list['ninja2_2_win'] = test[1]
                                    ninja2.dialogue = 1
                                death_list[f'{character.character}_win'] = test[1]
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
                    hero.attack_type = 1

            if e.type == KEYUP and e.key == K_RIGHT or hero.pause == 1:
                right = False
            if e.type == KEYUP and e.key == K_LEFT or hero.pause == 1:
                left = False
            if e.type == KEYUP and e.key == K_DOWN or hero.pause == 1:
                down = False
            if e.type == KEYUP and e.key == K_UP or hero.pause == 1:
                up = False
        #score_text = font.render(f'Монеты: {hero.score}', True, (240, 215, 0))
        #screen.blit(score_text, (10, 60))
        if death_list['slaim_farmer_win'] != 1:
            if pygame.sprite.collide_rect(farmer,hero) and farmer.quest2 >= 3:
                farmer.dialogue = 1
                test = fait(screen,hero,farmer.fait)
                hero.health = test[0]
                farmer.win = test[1]
                death_list['slaim_farmer_win'] = test[1]
                right = False
                left = False
                down = False
                up = False
                pygame.mixer.music.load("sound/sound_son.mp3")
                pygame.mixer.music.set_volume(hero.musec)
                pygame.mixer.music.play(-1, 0.0, 5000)
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
        if (death_list['ninja2_2_win'] == 1 and death_list['ninja2_3_win'] == 1):
            pf1.rect.y = -370
        if death_list['ninja2_1_win'] == 1:
            pf2.rect.y = -370
        if hero.health <= 0:
            hero.winner = True
        if hero.rect.x < 0:
            hero.location = 2
            hero.winner = True
            hero.rect.x = 3500
            hero.rect.y = 400
        if hero.rect.y >= total_level_height:
            hero.location = 8
            hero.winner = True
            hero.rect.x = 500
            hero.rect.y = 100
        if hero.rect.y < 0:
            hero.location = 4
            hero.winner = True
            hero.rect.x = 830
            hero.rect.y = 1660
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