import pygame
#from player import Player
from blocks import *
from random import randint
from text import king_t
from main import *
from anim import NPS_KING,NPS_KING2, NPS_CRYSTAL, king_icon,king_icon2
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
    levelFile = open('lvl/7.txt')
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

def main7(hero,screen,death_list):
    global level
    #print(7)
    level = []
    entities = pygame.sprite.Group()
    entities2 = pygame.sprite.Group()
    break_object = pygame.sprite.Group()
    animatedEntities = pygame.sprite.Group()
    animatedEntities2 = pygame.sprite.Group()
    platforms = [] 
    fait_character = []
    #list_knight = []
    loadLevel()

    left = right = False # по умолчанию - стоим
    up = down = False
    bg = Surface(DISPLAY)
    bg.fill((100,100,100))
    
    timer = pygame.time.Clock()
    x=y=0 # координаты
    random_tree = 0
    random_mushroom = 0
    random_mushroom2 = 0
    random_mushroom3 = 0
    random_grass = 0
    random_stone = 0
    for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
                pf = Img_stat(x,y,32,32,'assets/other/not_in.png')
                platforms.append(pf)
            elif col == "*":
                pf = Anim_img(x, y, 32, 32, NPS_CRYSTAL)
                animatedEntities.add(pf)
                entities.add(pf)
            elif col == "0":
                colunm = Img_break(x - 50,y - 150,150,450,'assets/building/column.png',80,'assets/building/column2.png',9,0)
                break_object.add(colunm)
                entities2.add(colunm)
            elif col == " ":
                random_grass += 1
                number_grass = 0
                if random_grass % death_list['random'][2][3] == 0:
                    number_grass = 1
                elif random_grass % death_list['random'][2][4] == 0:
                    number_grass = 2
                elif random_grass % death_list['random'][2][5] == 0:
                    number_grass = 3
                elif random_grass % death_list['random'][2][6] == 0:
                    number_grass = 4
                elif random_grass % death_list['random'][2][7] == 0:
                    number_grass = 5
                if random_grass % death_list['random'][2][10] == 0:
                    flip_x = True
                else:
                    flip_x = False
                if number_grass != 0:
                    t = f'assets/grass/grass3_{number_grass}.png'
                    pf = Img_stat(x,y,32,32,t,flip_x)
                    entities.add(pf)
            elif col == "<":
                pf = Img_stat(x,y,32,32,'assets/building/road1.png')
                entities.add(pf)
            elif col == ">":
                pf = Img_stat(x,y,32,32,'assets/building/road2.png')
                entities.add(pf)
            elif col == "=":
                pf = Img_stat(x,y,32,32,'assets/building/road3.png')
                entities.add(pf)
            elif col == "{":
                pf = Img_stat(x,y,32,32,'assets/building/road1.png')
                platforms.append(pf)
                entities.add(pf)
            elif col == "}":
                pf = Img_stat(x,y,32,32,'assets/building/road2.png')
                platforms.append(pf)
                entities.add(pf)
            elif col == "+":
                pf = Img_stat(x,y,32,32,'assets/building/road3.png')
                platforms.append(pf)
                entities.add(pf)
            elif col == "2":
                random_stone += 1
                if random_stone % death_list['random'][4] == 0:
                    if random_stone % 4 == 0:
                        stone = 'assets/tree/stone.png'
                    else:
                        stone = 'assets/tree/stone2.png'
                    pf = Img_stat(x,y,27,22,stone)
                    entities.add(pf)
                    platforms.append(pf)
            elif col == "K":
                king = Dialogue_img(x - 290,y + 50,150,105,NPS_KING,NPS_KING2,0,king_icon,king_icon2,0,-1,28,3,'king',king_t,False,False,True,150,105)
                animatedEntities2.add(king)
                entities2.add(king)
                fait_character.append(king)
   
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
                                character.win = 1
                                death_list[f'{character.character}_win'] = 1
                                right = False
                                left = False
                                down = False
                                up = False
                                pygame.mixer.music.load("sound/sound_son.mp3")
                                pygame.mixer.music.set_volume(hero.musec)
                                pygame.mixer.music.play(-1, 0.0, 5000)
                            elif character.win == 1:
                                death_list[f'{character.character}_death'] = 1
                                hero.end = 0
                                hero.health -= 1000
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
        #score_text = font.render(f'Монеты: {hero.score}', True, (240, 215, 0))
        #screen.blit(score_text, (10, 60))
        camera.update(hero) 
        animatedEntities.update() 
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        hero.draw(screen, camera.state, circle_surf)
        hero.update(left, right, up, down, screen, platforms, camera.state)
        for e in entities2:
            screen.blit(e.image, camera.apply(e))
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
        if hero.boom == 6:
            hero.end = 3
            hero.health = -1
        if hero.health <= 0:
            hero.winner = True
        if hero.rect.x > total_level_width:
            hero.health -= 1000
            hero.end = 0
            hero.winner = True
        if hero.rect.x <= 0:
            hero.rect.x = 600
            hero.rect.y = 350
            hero.location = 9
            hero.winner = True
        pygame.display.update()
    return hero
level = []
entities = pygame.sprite.Group()
animatedEntities = pygame.sprite.Group() # все анимированные объекты, за исключением героя
platforms = [] # то, во что мы будем врезаться или опираться
PLATFORM_COLOR = "#000000"
test1 = 0
#hero = Player(1, 100, 384, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)