import pygame
from player import Player
from blocks import Img_button, image, Img_t, QUIT, Img_stat
from platformerhabrahabr1 import play
from time import sleep
from random import randint 
import json
pygame.init()

attack_hero = []
amulet_hero = []
next_game = -1

ability_list = {
    'attack_1':1,
    'attack_2':-1,
    'attack_5':-1,
    'attack_6':-1,
    'attack_7':-1,
    'attack_8':-1,
    'attack_9':-1,
    'attack_10':-1,
    'attack_11':-1,
    'amulet_1':-1,
    'amulet_2':0,
    'amulet_3':0,
    'amulet_4':0,
    'amulet_5':0,
    'amulet_6':0,
    'amulet_7':0,
    'amulet_8':0,
    'amulet_9':0,
    'amulet_10':0,
    'amulet_11':0,
    'amulet_12':0,
    'amulet_13':0,
    'amulet_14':0,
    'amulet_15':0,
    'amulet_16':0,
    'amulet_17':0,
    'amulet_18':0,
    'amulet_19':0,
    'amulet_20':0
}

try:
   with open('ability.txt') as load_file:
       ability_list = json.load(load_file)
except:
  with open('ability.txt','w') as store_file:
      json.dump(ability_list,store_file)

WIN_WIDTH = 800 
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("The Unknown Warrior")

pygame.mixer.music.load("sound/sound_son.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("sound/sword.wav")
sword_fx.set_volume(0.2)
WARRIOR_SIZE = 162
WARRIOR_SCALE = 1.5
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
warrior_sheet = pygame.image.load("assets/battle/warrior.png").convert_alpha()

hero = Player(1, 100, 300, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, 2,sword_fx) #100 300

def option(hero,screen):
    bg = image.load('assets/background_end/background0.png').convert_alpha()
    timer = pygame.time.Clock()

    size_t = 27
    score_font = pygame.font.Font("fonts/game.ttf", size_t)
    button1 = Img_button(250,5,300,130,'assets/button/back.png','assets/button/back2.png')
    button2 = Img_button(30,150,300,130,'assets/button/easy.png','assets/button/easy2.png')
    button3 = Img_button(30,265,300,130,'assets/button/norm.png','assets/button/norm2.png')
    button4 = Img_button(30,380,300,130,'assets/button/hard.png','assets/button/hard2.png')
    button5 = Img_button(30,495,300,130,'assets/button/impossable.png','assets/button/impossable2.png')
    slider = Img_t(400,250,'assets/button/test1.png','assets/button/test2.png')
    slider2 = Img_t(400,450,'assets/button/test1.png','assets/button/test2.png')
    text = ['уровень сложности:','громкость музыки:','громкость эффектов:']
    menu1 = 0
    play_game = -1
    y = 210
    while play_game != 1:
        timer.tick(60)
        screen.blit(bg,(0,0))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
        play_game = button1.draw(screen,play_game,3)
        hero.hard = button2.draw(screen,hero.hard,-2)
        hero.hard = button3.draw(screen,hero.hard,-4)
        hero.hard = button4.draw(screen,hero.hard,-6)
        hero.hard = button5.draw(screen,hero.hard,-8)
        hero.musec = slider.draw(screen,hero.musec)
        hero.effect = slider2.draw(screen,hero.effect)
        text_surface = score_font.render(text[0], False, (230, 230, 230))
        text_surface2 = score_font.render(text[1], False, (230, 230, 230))
        text_surface3 = score_font.render(text[2], False, (230, 230, 230))
        pygame.mixer.music.set_volume(hero.musec)
        screen.blit(text_surface, (10,125))
        screen.blit(text_surface2, (380,200))
        screen.blit(text_surface3, (370,400))
        pygame.display.update()

def play_game_save(hero,screen,attack_hero,next_game):
    bg = image.load('assets/background_end/background0.png').convert_alpha()
    timer = pygame.time.Clock()

    size_t = 27
    score_font = pygame.font.Font("fonts/game.ttf", size_t)
    button1 = Img_button(30,550,140,70,'assets/button/back_1.png','assets/button/back_1.png')
    button2 = Img_button(620,550,140,70,'assets/button/next.png','assets/button/next.png')
    text = 'экипировка персонажа'

    entities = pygame.sprite.Group()
    list_icon = []
    list_icon_save = []
    list_icon_save2 = []
    x = 250
    type = 12
    icond = Img_stat(270,240,90,90,'assets/other/keys_d.png',False,False,True,48,48,0)
    icons = Img_stat(370,240,90,90,'assets/other/keys_s.png',False,False,True,48,48,0)
    iconw = Img_stat(470,240,90,90,'assets/other/keys_w.png',False,False,True,48,48,0)
    icona = Img_stat(570,240,90,90,'assets/other/keys_a.png',False,False,True,48,48,0)
    icone = Img_stat(670,240,90,90,'assets/other/keys_e.png',False,False,True,48,48,0)
    icon_list_k = []
    icon_list_k.append(icond)
    icon_list_k.append(icons)
    icon_list_k.append(iconw)
    icon_list_k.append(icona)
    icon_list_k.append(icone)
    for i in icon_list_k:
        entities.add(i)
    for i in range(5):
        icon1 = Img_stat(x,150,90,90,'assets/other/icon2.png',False,False,True,90,90,type)
        entities.add(icon1)
        list_icon_save.append(icon1)
        type += 1
        if type == 3:
            type = 5
        x += 100
    x = 5
    type = 1
    for i in range(9):
        if ability_list[f'attack_{type}'] == 1:
            icon = 'assets/other/icon4.png'
        else:
            icon = 'assets/other/icon5.png'
        icon1 = Img_stat(x,300,80,80,icon,False,False,True,80,80,type)
        entities.add(icon1)
        list_icon_save2.append(icon1)
        type += 1
        if type == 3:
            type = 5
        x += 88
    type = -1
    icon = 1
    x = 13
    for i in range(9):
        icon1 = Img_stat(x,307,64,64,f'assets/battle/icon{-type}.png',False,False,True,64,64,type)
        entities.add(icon1)
        list_icon.append(icon1)
        type -= 1
        if type == -3:
            type = -5
        x += 88
    hero_icon = Img_stat(80,100,138,168,'assets/other/icon1.png',False,False,True,138,168,0)
    entities.add(hero_icon)
    list_attack_icon = []
    for i in list_icon:
        attack_icon = Img_stat(80,100,138,168,f'assets/other/Attack/attack_{-i.type}.png',False,False,True,138,168,i.type)
        list_attack_icon.append(attack_icon)
    icon_t = Img_stat(0,300,46,56,'assets/other/icon3.png',False,False,True,90,90)
    icon_t2 = Img_stat(0,300,46,56,'assets/other/icon3.png',False,False,True,80,80)
    text_weapon = ['начальное оружие','победите жителя деревни','','',
                   'убей короля',
                   'предайте предателя у замка','победите обычного ниндзя',
                   'победите фермера слизня','спасите деревню слизней',
                   'победи ведьму','победи мага огня']
    text_weapon2 = ['идиальный баланс','отолкнёт или притянет врага, хороший урон','','',
                   'убийственный урон, долгая перезарядка','отхилься нанеся урон',
                   'рывок и неуязвимость к урону','восполни здоровье',
                   'чем ближе к противнику, тем больше урона','безконтактный бой и отталкивание',
                   'огненый пинок с неба, удар в прыжке']
    text_weapon_name = ['клинок молний','клинок двух душ','','',
                        'молниеносная кара','вампирский удар',
                        'мгновенный шаг','перчатка садовода',
                        'небесная кара','сила инь и янь',
                        'прыжок феникса']
    #menu1 = 0
    number = 0
    number2 = 0
    play_game = -1
    y = 210
    clicked = False
    while play_game != 1:
        timer.tick(60)
        screen.blit(bg,(0,0))
        pos = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
        play_game = button1.draw(screen,play_game,3)
        next_game = button2.draw(screen,next_game,3)
        if next_game == 1:
            play_game = 1
            next_game = 1
        for e in entities:
            screen.blit(e.image, (e.rect.x,e.rect.y))
            if e.rect.collidepoint(pos):
                if e.type > 11:
                    icon_t.rect = e.rect
                    screen.blit(icon_t.image, (icon_t.rect.x,icon_t.rect.y))
                if e.type <= 11 and e.type > 0:
                    icon_t2.rect = e.rect
                    screen.blit(icon_t2.image, (icon_t2.rect.x,icon_t2.rect.y))
                    text_surface = score_font.render(text_weapon[e.type - 1], False, (180, 180, 180))
                    screen.blit(text_surface, (30,510))
                    text_surface2 = score_font.render(text_weapon2[e.type - 1], False, (230, 230, 230))
                    screen.blit(text_surface2, (30,450))
                    text_surface3 = score_font.render(text_weapon_name[e.type - 1], False, (250, 230, 0))
                    screen.blit(text_surface3, (30,400))
                    if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                        for i in list_icon:
                            if i.type == -e.type and number < 5 and e.save == 1 and ability_list[f'attack_{-i.type}'] == 1:
                                i.rect.x = list_icon_save[number].rect.x + 12
                                i.rect.y = list_icon_save[number].rect.y + 12
                                list_icon_save[number].save = 1
                                attack_hero.append(-i.type)
                                number += 1
                                if -i.type == 7 and number != 5:
                                    if number == 4:
                                        icon_list_k[4].rect.x = 570
                                        icon_list_k[3].rect.x = 670
                                    if number == 3:
                                        icon_list_k[4].rect.x = 470
                                        icon_list_k[2].rect.x = 670
                                    if number == 2:
                                        icon_list_k[4].rect.x = 370
                                        icon_list_k[1].rect.x = 670
                                    if number == 1:
                                        icon_list_k[4].rect.x = 270
                                        icon_list_k[0].rect.x = 670
                                for g in list_attack_icon:
                                    if g.type == i.type:
                                        entities.add(g)
                                e.save = 0
                        clicked = True
                    if pygame.mouse.get_pressed()[1] == 0:
                        clicked = False
        text_surface = score_font.render(text, False, (230, 230, 230))
        screen.blit(text_surface, (300,70))
        pygame.display.update()
    return next_game

def play_game_save2(hero,screen,amulet_hero,next_game):
    bg = image.load('assets/background_end/background0.png').convert_alpha()
    timer = pygame.time.Clock()

    size_t = 25
    score_font = pygame.font.Font("fonts/game.ttf", size_t)
    button1 = Img_button(30,560,140,70,'assets/button/back_1.png','assets/button/back_1.png')
    button2 = Img_button(620,560,140,70,'assets/button/next.png','assets/button/next.png')
    text = 'экипировка персонажа'

    entities = pygame.sprite.Group()
    
    hero_icon = Img_stat(80,100,138,168,'assets/other/icon1.png',False,False,True,138,168,0)
    entities.add(hero_icon)
    icon_t = Img_stat(0,300,46,56,'assets/other/icon3.png',False,False,True,80,80)
    icon_t2 = Img_stat(0,300,46,56,'assets/other/icon3.png',False,False,True,70,70)
    
    list_icon = []
    list_icon_save = []
    list_icon_save2 = []
    play_game = -1
    #y = 210
    number = 0
    clicked = False
    x = 240
    type = 21
    for i in range(6):
        icon1 = Img_stat(x,150,90,90,'assets/other/icon2.png',False,False,True,80,80,type)
        entities.add(icon1)
        list_icon_save.append(icon1)
        type += 1
        x += 90
    x = 8
    y = 280
    type = 1
    for i in range(20):
        if ability_list[f'amulet_{type}'] == 1:
            icon = 'assets/other/icon4.png'
        else:
            icon = 'assets/other/icon5.png'
        icon1 = Img_stat(x,y,80,80,icon,False,False,True,70,70,type)
        entities.add(icon1)
        list_icon_save2.append(icon1)
        type += 1
        x += 79
        if type == 11:
            y = 360
            x = 8
    x = 18
    y = 290
    type = -1
    for i in range(20):
        icon1 = Img_stat(x,y,50,50,f'assets/other/Transperent/icon{-type}.png',False,False,True,50,50,type)
        entities.add(icon1)
        list_icon.append(icon1)
        type -= 1
        x += 79
        if type == -11:
            y = 370
            x = 18
    list_attack_icon = []
    for i in list_icon:
        if -i.type == 18:
            attack_icon = Img_stat(20,160,92,112,f'assets/other/Amulet/amulet_{-i.type}.png',False,False,True,92,112,i.type)
        elif -i.type == 19:
            attack_icon = Img_stat(10,130,69,84,f'assets/other/Amulet/amulet_{-i.type}.png',False,False,True,69,84,i.type)
        elif -i.type == 20:
            attack_icon = Img_stat(60,100,69,84,f'assets/other/Amulet/amulet_{-i.type}.png',False,False,True,69,84,i.type)
        else:
            attack_icon = Img_stat(80,100,138,168,f'assets/other/Amulet/amulet_{-i.type}.png',False,False,True,138,168,i.type)
        list_attack_icon.append(attack_icon)
    text_amulet_name = ['скоростная шерcть','перо лёгкости',
            'твёрдые наплечники','ожерелье берсерка',
            'амулет ягуара','амулет быстрейшего ягуара',
            'липкое растение','блестящая кольчуга',
            'магнитное перо','листья фиола',
            'заостренная ткань','кольчуга джунглей',
            'перо феникса','наплечник воина',
            'наплечник силы','молнииностный клюв',
            'ожерелье питомцев','ожерелье слайма',
            'ожерелье лестного слайма','ожерелье монстра']
    text_amulet = ['увеличивает скорость персонажа','увеличивает высоту и долгость прыжка',
            'урон по вам уменьшен на 2 хп','урон врагов и ваш увеличен',
            'рывок длиться дольше','скорость атаки всех оружий увеличена',
            'потихоньку востанавливает вам здоровье','хп персонажа увеличенно на 50',
            'ваши притягивание и отталкивание увеличены','хп и урон союзников увеличены',
            'рывок наносит урон','не много увеличивает защиту, хп и урон',
            'атаки в прыжке дают зависать в воздухе','урон по вам уменьшен на 4 хп',
            'скорость перезарядки атак уменьшена','броня противника уменьшена на 2 хп',
            'улучшает урон питомцев','призывает слайма помошника',
            'призывает древестного слайма помошнка','призывает глаза помошника']
    text_amulet_info = ['получите любую концовку','обруште колонны в замке',
        'победите друга рыцаря','победите крутого слайма',
        'победите отряд метасуса','победите усиленного ниндзя',
        'победите фермера слайма','победите червя без помощи',
        'сохранитесь 1 раз','победите червя с крестьянином',
        'победите всех рыцарей короля','победите королевского мага',
        'сбегите с финального поля боя','победите усиленного мага огня',
        'победите ассистентку','победите ведьму',
        'получи концовку ассестентки','победи слайма физара',
        'победи древестного слайма','победите 2 глазиков'
    ]
    while play_game != 1:
        timer.tick(60)
        screen.blit(bg,(0,0))
        pos = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
        play_game = button1.draw(screen,play_game,3)
        next_game = button2.draw(screen,next_game,3)
        if next_game == 1:
            play_game = 1
            next_game = 1
        for e in entities:
            screen.blit(e.image, (e.rect.x,e.rect.y))
            if e.rect.collidepoint(pos):
                if e.type != 0:
                    if e.type >= 21:
                        icon_t.rect = e.rect
                        screen.blit(icon_t.image, (icon_t.rect.x,icon_t.rect.y))
                    if e.type < 21 and e.type > 0:
                        icon_t2.rect = e.rect
                        screen.blit(icon_t2.image, (icon_t2.rect.x,icon_t2.rect.y))
                        text_surface = score_font.render(text_amulet_name[e.type - 1], False, (250, 230, 0))
                        screen.blit(text_surface, (20,440))
                        text_surface = score_font.render(text_amulet[e.type - 1], False, (230, 230, 230))
                        screen.blit(text_surface, (20,480))
                        text_surface = score_font.render(text_amulet_info[e.type - 1], False, (180, 180, 180))
                        screen.blit(text_surface, (20,520))
                        if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                            for i in list_icon:
                                if i.type == -e.type and number < 6 and e.save == 1 and ability_list[f'amulet_{-i.type}'] == 1:
                                    i.rect.x = list_icon_save[number].rect.x + 12
                                    i.rect.y = list_icon_save[number].rect.y + 12
                                    list_icon_save[number].save = 1
                                    amulet_hero.append(-i.type)
                                    number += 1
                                    for g in list_attack_icon:
                                        if g.type == i.type:
                                            entities.add(g)
                                    e.save = 0
                            clicked = True
                        if pygame.mouse.get_pressed()[1] == 0:
                            clicked = False
        text_surface = score_font.render(text, False, (230, 230, 230))
        screen.blit(text_surface, (300,70))
        pygame.display.update()
    return next_game

def info(hero,screen):
    bg = image.load('assets/background_end/background0.png').convert_alpha()
    timer = pygame.time.Clock()

    size_t = 27
    score_font = pygame.font.Font("fonts/game.ttf", size_t)
    button3 = Img_button(250,10,300,130,'assets/button/back.png','assets/button/back2.png')
    text = ['Приветствую тебя игрок','даннаю игру можно поделить на 2 части:',
            'путешествие по миру и файтинги','управление похоже и там и там',
            'ходьба - стрелки','атаки - в, ы, ф, у, ц (русские)',
            'одна из фишек игры - крушить, со всем','окружением можно взаимодействовать',
            'после победы ты можешь убить врага','в случаи проигрыша произойти может всё',
            'для начала боя ударь противника','ты должен победить 3 раунда']
    menu1 = 0
    play_game = -1
    y = 170
    while play_game != 1:
        timer.tick(60)
        screen.blit(bg,(0,0))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
        play_game = button3.draw(screen,play_game,3)
        for i in text:
            text_surface = score_font.render(i, False, (230, 230, 230))
            screen.blit(text_surface, (10,y))
            y += 38
            if y >= 616:
                y = 170
        pygame.display.update()

def main_menu(hero,screen,attack_hero,next_game,amulet_hero):
    bg = image.load('assets/background_end/background.png').convert_alpha()
    timer = pygame.time.Clock()

    size_t = 28
    score_font = pygame.font.Font("fonts/game.ttf", size_t)
    button1 = Img_button(250,100,300,130,'assets/button/play.png','assets/button/play2.png')
    button4 = Img_button(250,220,300,130,'assets/button/option.png','assets/button/option2.png')
    button3 = Img_button(250,460,300,130,'assets/button/back.png','assets/button/back2.png')
    button2 = Img_button(250,340,300,130,'assets/button/info.png','assets/button/info2.png')
    text = 'кем ты станешь?'
    menu1 = 0
    play_game = -1
    while play_game != 1:
        timer.tick(60)
        screen.blit(bg,(0,0))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
        menu1 = button1.draw(screen,menu1,3)
        menu1 = button2.draw(screen,menu1,4)
        play_game = button3.draw(screen,play_game,3)
        if menu1 == 1:
            hard = hero.hard 
            musec = hero.musec
            effect = hero.effect
            #hero = Player(1, 100, 300, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, hard,sword_fx) #100 300
            #hero.musec = musec
            #hero.effect = effect
            #hero.attack_sound.set_volume(hero.effect)
            #pygame.mixer.music.set_volume(hero.musec)
            #play(hero,screen,death_list)
            attack_hero = []
            amulet_hero = []
            cooldown = []
            sleep(0.2)
            next_game = -1
            next_game = play_game_save(hero,screen,attack_hero,next_game)
            sleep(0.2)
            if next_game == 1:
                next_game = -1
                next_game = play_game_save2(hero,screen,amulet_hero,next_game)
                if next_game == 1:
                    if attack_hero == []:
                        attack_hero = [1]
                    for i in range(5-len(attack_hero)):
                        attack_hero.append(-1)
                    for i in attack_hero:
                        if i == 7 and len(attack_hero) == 5 and not -1 in attack_hero:
                            attack_hero.remove(i)
                            attack_hero.append(7)
                    for i in attack_hero:
                        if i == 1:
                            cooldown.append(17)
                        elif i == 2:
                            cooldown.append(150)
                        elif i == 5:
                            cooldown.append(600)
                        elif i == 6:
                            cooldown.append(300)
                        elif i == 7:
                            cooldown.append(20)
                        elif i == 8:
                            cooldown.append(400)
                        elif i == 9:
                            cooldown.append(1000)
                        elif i == 10:
                            cooldown.append(250)
                        elif i == 11:
                            cooldown.append(350)
                        else:
                            cooldown.append(-1)
                    #print(attack_hero)
                    death_list = {'random':[[randint(3,6),randint(7,11),randint(12,15),randint(2,3)],[randint(2,3),randint(4,6),randint(2,4)],[randint(300,500),randint(250,500),randint(275,500),randint(250,450),randint(250,500),randint(200,400),randint(150,400),randint(200,400),randint(150,400),randint(200,400),randint(2,4)],[randint(5,6),randint(2,4),randint(2,4)],randint(3,6)],
                    'location':0,
                    'moon':1,
                    'slaim_death':-1,
                    'slaim_quest':-1,
                    'slaim_win':-1,
                    'witch_dialogue':-1,
                    'witch_death':-1,
                    'witch_quest':-1,
                    'witch_quest2':-1,
                    'witch_quest2_2':-1,
                    'witch_quest3':-1,
                    'witch_quest4':-1,
                    'witch_win':-1,
                    'assistant_death':-1,
                    'assistant_quest':-1,
                    'assistant_quest2':-1,
                    'assistant_quest3':-1,
                    'assistant_win':-1,
                    'slaim_bro_death':-1,
                    'slaim_bro_quest':-1,
                    'slaim_bro_win':-1,
                    'eye1_death':-1,
                    'eye1_quest':-1,
                    'eye1_quest2':-1,
                    'eye1_win':-1,
                    'eye2_death':-1,
                    'eye2_quest':-1,
                    'eye2_quest2':-1,
                    'eye2_win':-1,
                    'ninja_death':-1,
                    'ninja_quest':-1,
                    'ninja_win':-1,
                    'ninja_evil_death':-1,
                    'ninja_evil_quest':-1,
                    'ninja_evil_win':-1,
                    'ninja2_1_death':-1,
                    'ninja2_1_quest':-1,
                    'ninja2_1_win':-1,
                    'ninja2_3_death':-1,
                    'ninja2_3_quest':-1,
                    'ninja2_3_win':-1,
                    'ninja2_2_death':-1,
                    'ninja2_2_quest':-1,
                    'ninja2_2_win':-1,
                    'slaim_natural_death':-1,
                    'slaim_natural_quest':-1,
                    'slaim_natural_win':-1,
                    'slaim_rustic_death':[-1,-1,-1,-1,-1,-1],
                    'slaim_rustic_quest':[-1,-1,-1,-1,-1,-1],
                    'slaim_rustic_win':[-1,-1,-1,-1,-1,-1],
                    'slaim_farmer_death':-1,
                    'slaim_farmer_quest':-1,
                    'slaim_farmer_win':-1,
                    'fire_mag_death':-1,
                    'fire_mag_quest':-1,
                    'fire_mag_quest2':-1,
                    'fire_mag_quest3':-1,
                    'fire_mag_quest4':-1,
                    'fire_mag_win':-1,
                    'fire_mag_win2':-1,
                    'people1_death':-1,
                    'people1_quest':-1,
                    'people1_win':-1,
                    'people1-2_death':-1,
                    'people1-2_quest':-1,
                    'people1-2_win':-1,
                    'people2_death':-1,
                    'people2_quest':-1,
                    'people2_win':-1,
                    'people2-2_death':-1,
                    'people2-2_quest':-1,
                    'people2-2_win':-1,
                    'people3_death':-1,
                    'people3_quest':-1,
                    'people3_win':-1,
                    'people3-2_death':-1,
                    'people3-2_quest':-1,
                    'people3-2_win':-1,
                    'worm1_death':-1,
                    'worm1_win':-1,
                    'worm1_quest':-1,
                    'worm2_death':-1,
                    'worm2_win':-1,
                    'worm2_quest':-1,
                    'worm3_death':-1,
                    'worm3_win':-1,
                    'worm3_quest':-1,
                    'knight_death':-1,
                    'knight_win':-1,
                    'knight_quest':-1,
                    'knight2_death':-1,
                    'knight2_win':-1,
                    'knight2_quest':-1,
                    'knight3_death':-1,
                    'knight3_win':-1,
                    'knight3_quest':-1,
                    'knight4_death':-1,
                    'knight4_win':-1,
                    'knight4_quest':-1,
                    'knight5_death':-1,
                    'knight5_win':-1,
                    'knight5_quest':-1,
                    'mag_death':-1,
                    'mag_win':-1,
                    'mag_quest':-1,
                    'king_death':-1,
                    'king_win':-1,
                    'king_quest':-1
                    }
                    with open('save.txt','w') as store_file:
                        json.dump(death_list,store_file)
                    #print(attack_hero)
                    hero = Player(1, 100, 300, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, hard,sword_fx,attack_hero,amulet_hero,cooldown) #100 300
                    if 8 in hero.amulet_hero:
                        hero.health_max += 50
                    if 9 in hero.amulet_hero:
                        hero.repulsion += 1
                    if 12 in hero.amulet_hero:
                        hero.health_max += 15
                        hero.damage += 0.5
                    hero.musec = musec
                    hero.effect = effect
                    hero.attack_sound.set_volume(hero.effect)
                    pygame.mixer.music.set_volume(hero.musec)
                    play(hero,screen,death_list)
                    if death_list['people1_win'] == 1 or death_list['people2_win'] == 1 or death_list['people3_win'] == 1:
                        ability_list['attack_2'] = 1
                    if death_list['king_death'] == 1:
                        ability_list['attack_5'] = 1
                    if death_list['assistant_win'] == 1 and death_list['assistant_quest3'] == 1 and death_list['mag_quest'] == 1:
                        ability_list['attack_6'] = 1
                    if death_list['ninja_win'] == 1:
                        ability_list['attack_7'] = 1
                    if death_list['slaim_farmer_win'] == 1:
                        ability_list['attack_8'] = 1
                    if death_list['ninja2_1_win'] == 1 and death_list['ninja2_2_win'] == 1 and death_list['ninja2_3_win'] == 1:
                        ability_list['attack_9'] = 1
                    if death_list['witch_win'] == 1:
                        ability_list['attack_10'] = 1
                    if death_list['fire_mag_win'] == 1:
                        ability_list['attack_11'] = 1

                    if hero.end != -1:
                        ability_list['amulet_1'] = 1
                    if hero.end == 3:
                        ability_list['amulet_2'] = 1
                    if death_list['knight_win'] == 1:
                        ability_list['amulet_3'] = 1
                    if death_list['slaim_bro_win'] == 1:
                        ability_list['amulet_4'] = 1
                    if death_list['ninja2_1_win'] == 1 and death_list['ninja2_2_win'] == 1 and death_list['ninja2_3_win'] == 1:
                        ability_list['amulet_5'] = 1
                    if death_list['ninja_evil_win'] == 1:
                        ability_list['amulet_6'] = 1
                    if death_list['slaim_farmer_win'] == 1: 
                        ability_list['amulet_7'] = 1
                    if death_list['worm1_win'] == 1 or death_list['worm2_win'] == 1 or death_list['worm3_win'] == 1:
                        ability_list['amulet_8'] = 1
                    if death_list['moon'] != 1:
                        ability_list['amulet_9'] = 1
                    if death_list['people1-2_win'] == 1 or death_list['people2-2_win'] == 1 or death_list['people3-2_win'] == 1:
                        ability_list['amulet_10'] = 1
                    if death_list['knight2_win'] == 1 and death_list['knight3_win'] == 1 and death_list['knight4_win'] == 1 and death_list['knight5_win'] == 1:
                        ability_list['amulet_11'] = 1
                    if death_list['mag_win'] == 1:
                        ability_list['amulet_12'] = 1
                    if hero.end == 4:
                        ability_list['amulet_13'] = 1
                    if death_list['fire_mag_win2'] == 1:
                        ability_list['amulet_14'] = 1
                    if death_list['assistant_win'] == 1:
                        ability_list['amulet_15'] = 1
                    if death_list['witch_win'] == 1:
                        ability_list['amulet_16'] = 1
                    if death_list['king_death'] == 1 and death_list['assistant_quest3'] == 1 and death_list['assistant_win'] != 1:
                        ability_list['amulet_17'] = 1
                    if death_list['slaim_win'] == 1:
                        ability_list['amulet_18'] = 1
                    if 1 in death_list['slaim_rustic_win']:
                        ability_list['amulet_19'] = 1
                    if death_list['eye1_win'] == 1 and death_list['eye2_win'] == 1:
                        ability_list['amulet_20'] = 1
                    sleep(0.2)
            menu1 = 0
        elif menu1 == 2:
            sleep(0.2)
            info(hero,screen)
            sleep(0.2)
            menu1 = 0
        elif menu1 == 3:
            sleep(0.2)
            option(hero,screen)
            sleep(0.2)
            menu1 = 0
        menu1 = button4.draw(screen,menu1,5)
        text_surface = score_font.render(text, False, (230, 230, 230))
        screen.blit(text_surface, (250,590))
        pygame.display.update()
main_menu(hero,screen,attack_hero,next_game,amulet_hero)
with open('ability.txt','w') as store_file:
    json.dump(ability_list,store_file)
#print(ability_list)