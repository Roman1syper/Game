import pygame
from pygame import mixer
from fighter import Fighter

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius, 7) #круги
    surf.set_colorkey((0, 0, 0))
    return surf

def fait(screen,hero,type,type_b=0):
  mixer.init()
  pygame.init()

  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 640

  clock = pygame.time.Clock()
  FPS = 60

  RED = (0, 0, 0)
  YELLOW = (255, 255, 0)
  WHITE = (255, 255, 255)

  intro_count = 3
  last_count_update = pygame.time.get_ticks()
  score = [0, 0]#player scores. [P1, P2]
  round_over = False
  ROUND_OVER_COOLDOWN = 2000

  WARRIOR_SIZE = 162
  WARRIOR_SCALE = 4
  WARRIOR_OFFSET = [72, 56]
  WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET,WARRIOR_SIZE]

  SLAIM_SIZE = 96
  SLAIM_SCALE = 3
  SLAIM_OFFSET = [30, 40]
  SLAIM_DATA = [SLAIM_SIZE,SLAIM_SCALE,SLAIM_OFFSET, SLAIM_SIZE]

  WIZARD_SIZE = 250
  WIZARD_SCALE = 3
  WIZARD_OFFSET = [112, 107]
  WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET, WIZARD_SIZE]

  NINJA_SIZE = 200
  NINJA_SCALE = 3
  NINJA_OFFSET = [89, 68]
  NINJA_DATA = [NINJA_SIZE, NINJA_SCALE, NINJA_OFFSET, NINJA_SIZE]

  NINJA2_SIZE = 200
  NINJA2_SCALE = 4
  NINJA2_OFFSET = [91, 77]
  NINJA2_DATA = [NINJA2_SIZE, NINJA2_SCALE, NINJA2_OFFSET, NINJA2_SIZE]

  WORM_SIZE = 90
  WORM_SCALE = 3
  WORM_OFFSET = [24, 35]
  WORM_DATA = [WORM_SIZE,WORM_SCALE,WORM_OFFSET,WORM_SIZE]

  WITCH_SIZE = 100
  WITCH_SCALE = 4
  WITCH_OFFSET = [40, 26]
  WITCH_DATA = [WITCH_SIZE,WITCH_SCALE,WITCH_OFFSET,WITCH_SIZE]

  MAG_SIZE = 150
  MAG_SCALE = 3.5
  MAG_OFFSET = [62, 50]
  MAG_DATA = [MAG_SIZE,MAG_SCALE,MAG_OFFSET,MAG_SIZE]

  MAG_SIZE = 150
  MAG_SCALE = 3.5
  MAG_OFFSET = [62, 50]
  MAG_DATA = [MAG_SIZE,MAG_SCALE,MAG_OFFSET,MAG_SIZE]

  KNIGHT_SIZE = 100
  KNIGHT_SCALE = 4
  KNIGHT_OFFSET = [41, 32]
  KNIGHT_DATA = [KNIGHT_SIZE,KNIGHT_SCALE,KNIGHT_OFFSET,KNIGHT_SIZE]

  ASSISTANT_SIZE = 32
  ASSISTANT_SCALE = 7
  ASSISTANT_OFFSET = [11, 6]
  ASSISTANT_DATA = [ASSISTANT_SIZE, ASSISTANT_SCALE, ASSISTANT_OFFSET, ASSISTANT_SIZE]

  EYE_SIZE = 60
  EYE_SCALE = 3
  EYE_OFFSET = [20, 11]
  EYE_DATA = [EYE_SIZE, EYE_SCALE, EYE_OFFSET, EYE_SIZE]

  SLAIM_TREE_SIZE = 52
  SLAIM_TREE_SCALE = 2.5
  SLAIM_TREE_OFFSET = [5, 19]
  SLAIM_TREE_DATA = [SLAIM_TREE_SIZE,SLAIM_TREE_SCALE,SLAIM_TREE_OFFSET,SLAIM_TREE_SIZE]

  PEOPLE_SIZE = 184
  PEOPLE_SIZE2 = 137
  PEOPLE_SCALE = 2.5
  PEOPLE_OFFSET = [81, 51]
  PEOPLE_DATA = [PEOPLE_SIZE,PEOPLE_SCALE,PEOPLE_OFFSET,PEOPLE_SIZE2]

  PEOPLE3_SIZE = 150
  PEOPLE3_SCALE = 3.25
  PEOPLE3_OFFSET = [63, 39]
  PEOPLE3_DATA = [PEOPLE3_SIZE,PEOPLE3_SCALE,PEOPLE3_OFFSET,PEOPLE3_SIZE]

  KNIGHT2_SIZE = 135
  KNIGHT2_SCALE = 4
  KNIGHT2_OFFSET = [57, 41]
  KNIGHT2_DATA = [KNIGHT2_SIZE,KNIGHT2_SCALE,KNIGHT2_OFFSET,KNIGHT2_SIZE]


  pygame.mixer.music.load("sound/music.mp3")
  pygame.mixer.music.set_volume(hero.musec)
  pygame.mixer.music.play(-1, 0.0, 5000)

  sword_fx = pygame.mixer.Sound("sound/sword.wav")
  sword_fx.set_volume(hero.effect)

  slaim_fx = pygame.mixer.Sound("sound/slaim.mp3")
  slaim_fx.set_volume(hero.effect)

  worm_fx = pygame.mixer.Sound("sound/worm.mp3")
  worm_fx.set_volume(hero.effect)

  magic_fx = pygame.mixer.Sound("sound/magic.wav")
  magic_fx.set_volume(hero.effect + 0.1)

  magic2_fx = pygame.mixer.Sound("sound/fire.ogg")
  magic2_fx.set_volume(hero.effect)
  if type_b != 1:
      bg_image = pygame.image.load("assets/battle/background2.png").convert_alpha()
  else:
      bg_image = pygame.image.load("assets/battle/background3.png").convert_alpha()

  warrior_sheet = pygame.image.load("assets/battle/warrior.png").convert_alpha()
  slaim_sheet = pygame.image.load("assets/battle/slaim_battle.png").convert_alpha()
  slaim_bro_sheet = pygame.image.load("assets/battle/slaim_battle2.png").convert_alpha()
  wizard_sheet = pygame.image.load("assets/battle/wizard.png").convert_alpha()
  ninja_sheet = pygame.image.load("assets/battle/ninja_sprites.png").convert_alpha()
  ninja_evil_sheet = pygame.image.load("assets/battle/ninja_battle2.png").convert_alpha()
  ninja2_sheet = pygame.image.load("assets/battle/ninja2.png").convert_alpha()
  worm_sheet = pygame.image.load("assets/battle/worm.png").convert_alpha()
  worm2_sheet = pygame.image.load("assets/battle/worm2.png").convert_alpha()
  witch_sheet = pygame.image.load("assets/battle/witch.png").convert_alpha()
  mag_sheet = pygame.image.load("assets/battle/mag.png").convert_alpha()
  mag_sheet2 = pygame.image.load("assets/battle/mag2.png").convert_alpha()
  knight_sheet = pygame.image.load("assets/battle/knight.png").convert_alpha()
  knight2_sheet = pygame.image.load("assets/battle/knight2.png").convert_alpha()
  assistant_sheet = pygame.image.load("assets/battle/assistant.png").convert_alpha()
  eye_sheet = pygame.image.load("assets/battle/eye.png").convert_alpha()
  slaim_tree_sheet = pygame.image.load("assets/battle/slaim_battle3.png").convert_alpha()
  slaim_farmer_sheet = pygame.image.load("assets/battle/slaim_battle4.png").convert_alpha()
  people_sheet = pygame.image.load("assets/battle/people1.png").convert_alpha()
  people2_sheet = pygame.image.load("assets/battle/people2.png").convert_alpha()
  people3_sheet = pygame.image.load("assets/battle/people3.png").convert_alpha()

  victory_img = pygame.image.load("assets/battle/victory.png").convert_alpha()
  if hero.cooldown_1 != -1:
    icon1 = pygame.image.load(f"assets/battle/icon{hero.attack_hero[0]}.png").convert_alpha()
  if hero.cooldown_2 != -1:
    icon2 = pygame.image.load(f"assets/battle/icon{hero.attack_hero[1]}.png").convert_alpha()
  if hero.cooldown_3 != -1:
    icon3 = pygame.image.load(f"assets/battle/icon{hero.attack_hero[2]}.png").convert_alpha()
  if hero.cooldown_4 != -1:
    icon4 = pygame.image.load(f"assets/battle/icon{hero.attack_hero[3]}.png").convert_alpha()
  if hero.cooldown_5 != -1:
    icon5 = pygame.image.load(f"assets/battle/icon{hero.attack_hero[4]}.png").convert_alpha()
  if 7 in hero.attack_hero:
    icon5 = pygame.image.load(f"assets/battle/icon7.png").convert_alpha()
  WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7, 8, 7, 8, 10, 6, 5, 5]

  WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
  NINJA_ANIMATION_STEPS = [4, 8, 1, 4, 4, 2, 7]
  NINJA_EVIL_ANIMATION_STEPS = [4, 8, 1, 4, 4, 2, 7, 4, 4, 8]
  NINJA2_ANIMATION_STEPS = [8, 8, 2, 6, 6, 4, 6]
  SLAIM_ANIMATION_STEPS = [7, 11, 1, 8, 8, 1, 11]
  SLAIM_BRO_ANIMATION_STEPS = [7, 11, 1, 8, 8, 5, 11]
  WORM_ANIMATION_STEPS = [9, 9, 9, 16, 16, 3, 8]
  WITCH_ANIMATION_STEPS = [8, 8, 1, 5, 5, 1, 8]
  MAG_ANIMATION_STEPS = [8, 8, 1, 8, 8, 4, 5]
  KNIGHT_ANIMATION_STEPS = [8, 10, 1, 6, 5, 1, 9, 1, 1, 5]
  KNIGHT2_ANIMATION_STEPS = [10, 6, 1, 4, 4, 3, 9, 5]
  ASSISTANT_ANIMATION_STEPS = [3, 8, 1, 8, 8, 2, 8]
  EYE_ANIMATION_STEPS = [16, 13, 1, 9, 9, 3, 15]
  SLAIM_TREE_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 6]
  PEOPLE_ANIMATION_STEPS = [6, 8, 1, 4, 4, 3, 9]
  PEOPLE3_ANIMATION_STEPS = [8, 8, 2, 4, 4, 3, 6, 4, 4]

  count_font = pygame.font.Font("fonts/turok.ttf", 80)
  score_font = pygame.font.Font("fonts/turok.ttf", 30)

  def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

  def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

  def draw_health_bar(health, x, y, max):
    ratio = health / max
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 254, 34))
    pygame.draw.rect(screen, RED, (x, y, 250, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 250 * ratio, 30))

  #игроки - создание персонажей
  #fighter_1 = Fighter(5, 200, 310, False, NINJA_DATA, ninja_sheet, NINJA_ANIMATION_STEPS, sword_fx, 1)
  rolling_over = 20
  #print(hero.attack_hero)
  if -1 in hero.attack_hero:
    if hero.cooldown_1 == rolling_over:
        fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, hero.health, hero.cooldown_5 ,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,hero.cooldown_1,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
    elif hero.cooldown_2 == rolling_over:
        fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, hero.health,hero.cooldown_1,hero.cooldown_5,hero.health_max,hero.cooldown_3,hero.cooldown_4,hero.cooldown_2,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
    elif hero.cooldown_3 == rolling_over:
        fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, hero.health,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_5,hero.cooldown_4,hero.cooldown_3,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
    elif hero.cooldown_4 == rolling_over:
        fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, hero.health,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_5,hero.cooldown_4,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
    else:
        fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, hero.health,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,-1,90,hero.damage,hero.attack_hero,hero.cooldown_5,hero.amulet_hero)
  else:
    if hero.attack_hero[4] == 7:
        fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, hero.health,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,hero.cooldown_5,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
    else:
        fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, hero.health,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,-1,90,hero.damage,hero.attack_hero,hero.cooldown_5,hero.amulet_hero)
  fighter_1.repulsion = hero.repulsion
  if 5 in hero.amulet_hero:
            fighter_1.rolling_over_speed += 2
  if 6 in hero.amulet_hero:
      fighter_1.attack_anim = 40
      fighter_1.speed_anim = 80
  fighter_1.speed1 = hero.speedx * 2 - (hero.speedx // 15)
  if hero.hard == 1:
      fighter_1.damage = hero.damage * 3
  elif hero.hard == 2:
      fighter_1.damage = hero.damage * 2.5
  else:
     fighter_1.damage = hero.damage * 2

  fighter_5 = False
  fighter_6 = False
  fighter_7 = False
  if 18 in hero.amulet_hero:
      fighter_5 = Fighter(7, 10, 450, True, SLAIM_DATA, slaim_sheet, SLAIM_ANIMATION_STEPS,slaim_fx, 0, 100,20,-1,100,-1,-1,-1,40,4)
      if 17 in hero.amulet_hero:
          fighter_5.damage += 3
  if 19 in hero.amulet_hero:
      fighter_6 = Fighter(252, 100, 450, True, SLAIM_TREE_DATA, slaim_tree_sheet, SLAIM_TREE_ANIMATION_STEPS, magic_fx, 0,90,11,11,100,-1,-1,-1,40,1.5)
      if 17 in hero.amulet_hero:
          fighter_6.damage += 2
  if 20 in hero.amulet_hero:
      fighter_7 = Fighter(23, 20, 320, False, EYE_DATA, eye_sheet, EYE_ANIMATION_STEPS, magic_fx, 0, 100,40,-1,100,-1,-1,-1,90,8)
      if 17 in hero.amulet_hero:
          fighter_7.damage += 2
  #fighter_2 = Fighter(4, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 2)
  fighter_3 = False
  fighter_4 = False
  if type == 1:
      fighter_2 = Fighter(7, 600, 450, True, SLAIM_DATA, slaim_sheet, SLAIM_ANIMATION_STEPS,slaim_fx, 0, 70, 100, 100, 100, -1,-1,-1, 100, 5)
  elif type == 2:
      fighter_2 = Fighter(5, 600, 350, True, NINJA_DATA, ninja_sheet, NINJA_ANIMATION_STEPS, sword_fx, 0, 90, 17, 17, 100, -1, -1, -1, 130, 1.5, [1,-1,-1,-1,-1],-1,[0,0],1)
  elif type == 22:
      fighter_2 = Fighter(55, 600, 350, True, NINJA_DATA, ninja_evil_sheet, NINJA_EVIL_ANIMATION_STEPS, sword_fx,0, 180, 17, 17, 200, -1, -1, -1, 130, 3, [1,-1,-1,-1,-1],-1,[0,0],12)
  elif type == 3:
      fighter_2 = Fighter(9, 600, 350, True, NINJA2_DATA, ninja2_sheet, NINJA2_ANIMATION_STEPS, sword_fx, 0, 140, 50, 70, 150, -1, -1, 50, 180, 2, [1,-1,-1,-1,-1],-1,[0,0],2)
  elif type == 33:
      fighter_2 = Fighter(9, 600, 350, True, NINJA2_DATA, ninja2_sheet, NINJA2_ANIMATION_STEPS, sword_fx, 0, 110, 70, 90, 150, -1, -1, -1, 180, 2, [1,-1,-1,-1,-1],-1,[0,0],2)
      fighter_3 = Fighter(9, 400, 350, True, NINJA2_DATA, ninja2_sheet, NINJA2_ANIMATION_STEPS, sword_fx, 0, 110, 60, 80, 150, -1, -1, -1, 180, 2, [1,-1,-1,-1,-1],-1,[0,0],2)
  elif type == 4:
      fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 280, 30, -1, 300, -1, -1, -1, 450, 25)
  elif type == 44:
      fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
  elif type == 414:
      fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 260, 30, -1, 300, -1, -1, -1, 450, 25)
      fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 60, 60, 80, 150, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 2)
  elif type == 415:
      fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 260, 30, -1, 300, -1, -1, -1, 450, 25)
      fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people2_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 55, 80, 60, 100, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 6)
  elif type == 416:
       fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 260, 30, -1, 300, -1, -1, -1, 450, 25)
       fighter_4 = Fighter(33, 200, 350, False, PEOPLE3_DATA, people3_sheet, PEOPLE3_ANIMATION_STEPS, sword_fx, 0, 50, 30, 50, 100, 60, 40, -1, 100, 4,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 4)
  elif type == 4414:
      fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
      fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 40, 60, 80, 150, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 2)
  elif type == 4415:
      fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
      fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people2_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 45, 80, 60, 100, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 6)
  elif type == 4416:
      fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
      fighter_4 = Fighter(33, 200, 350, False, PEOPLE3_DATA, people3_sheet, PEOPLE3_ANIMATION_STEPS, sword_fx, 0, 50, 30, 50, 100, 60, 40, -1, 100, 4,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 4)
  elif type == 5:
      fighter_2 = Fighter(13, 600, 350, True, WITCH_DATA, witch_sheet, WITCH_ANIMATION_STEPS, magic_fx, 0, 140, 80, 80, 150, -1, -1, -1, 100, 7)
  elif type == 6:
      fighter_2 = Fighter(15, 600, 350, True,  MAG_DATA, mag_sheet, MAG_ANIMATION_STEPS, magic2_fx, 0, 240, 40,50,250,-1,-1,-1,90,3)
  elif type == 66:
      fighter_2 = Fighter(15, 600, 350, True,  MAG_DATA, mag_sheet2, MAG_ANIMATION_STEPS, magic2_fx, 0, 280, 40,50,300,-1,-1,-1,90,4,[1,-1,-1,-1,-1],-1,[0,0],6)
  elif type == 7:
      fighter_2 = Fighter(17, 600, 350, True, KNIGHT_DATA, knight_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, 0, 220, 40, -1, 250, -1, -1, 140, 100, 6,[1,-1,-1,-1,-1],-1,[0,0,0,0,0], 8)
  elif type == 77:
      fighter_2 = Fighter(17, 600, 350, True, KNIGHT_DATA, knight_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, 0, 220, 40, -1, 250, -1, -1, 140, 100, 6,[1,-1,-1,-1,-1],-1,[0,0,0,0,0], 8)
      fighter_4 = Fighter(15, 600, 350, True,  MAG_DATA, mag_sheet, MAG_ANIMATION_STEPS, magic2_fx, 0, 200, 40,50,270,-1,-1,-1,90,3)
  elif type == 8:
     fighter_2 = Fighter(3, 600, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 0, 360,80,100,400,-1,-1,-1,180,6,[1,1,-1,-1,-1],-1,[0,0,0,0,0],1)
  elif type == 85:
     fighter_2 = Fighter(3, 600, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 0, 380,80,100,400,-1,-1,-1,180,6,[1,1,-1,-1,-1],-1,[0,0,0,0,0],3)
     fighter_4 = Fighter(13, 50, 350, False, WITCH_DATA, witch_sheet, WITCH_ANIMATION_STEPS, magic_fx, 0, 90, 80, 80, 150, -1, -1, -1, 100, 7)
  elif type == 810:
     fighter_2 = Fighter(3, 600, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 0, 390,80,100,400,-1,-1,-1,180,6,[1,1,-1,-1,-1],-1,[0,0,0,0,0],2)
     fighter_4 = Fighter(21, 50, 350, False, ASSISTANT_DATA, assistant_sheet, ASSISTANT_ANIMATION_STEPS, magic_fx, 0, 190, 20, -1, 200,-1,-1,-1,180,9,[1,1,-1,-1,-1],-1,[0,0,0,0,0],8)
  elif type == 9:
      fighter_2 = Fighter(19, 600, 450, True, SLAIM_DATA, slaim_bro_sheet, SLAIM_BRO_ANIMATION_STEPS,slaim_fx, 0, 100, 40, 40, 100, -1, -1, -1, 60, 6)
  elif type == 10:
      fighter_2 = Fighter(21, 600, 350, True, ASSISTANT_DATA, assistant_sheet, ASSISTANT_ANIMATION_STEPS, magic_fx, 0, 190, 20, -1, 200,-1,-1,-1,180,9,[1,1,-1,-1,-1],-1,[0,0,0,0,0],10)
  elif type == 11:
      fighter_2 = Fighter(23, 600, 350, True, EYE_DATA, eye_sheet, EYE_ANIMATION_STEPS, magic_fx, 0, 70,30,200,70,-1,-1,-1,200,7,[1,1,-1,-1,-1],-1,[0,0,0,0,0],4)
  elif type == 12:
      fighter_2 = Fighter(25, 600, 450, True, SLAIM_TREE_DATA, slaim_tree_sheet, SLAIM_TREE_ANIMATION_STEPS, magic_fx, 0, 170,10,10,200,-1,-1,-1,110,3)
  elif type == 13:
      fighter_2 = Fighter(27, 600, 450, True, SLAIM_TREE_DATA, slaim_farmer_sheet, SLAIM_TREE_ANIMATION_STEPS, magic_fx, 0, 200,10,10,200,-1,-1,-1,110, 10,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 12)
  elif type == 14:
      fighter_2 = Fighter(29, 600, 350, True, PEOPLE_DATA, people_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 140, 60, 80, 150, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 2)
  elif type == 15:
      fighter_2 = Fighter(29, 600, 350, True, PEOPLE_DATA, people2_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 95, 80, 60, 100, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 5)
  elif type == 16:
      fighter_2 = Fighter(33, 600, 350, True, PEOPLE3_DATA, people3_sheet, PEOPLE3_ANIMATION_STEPS, sword_fx, 0, 90, 30, 50, 100, 60, 40, -1, 100, 4,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 3)
  elif type == 17:
      fighter_2 = Fighter(35, 600, 350, True, KNIGHT2_DATA, knight2_sheet, KNIGHT2_ANIMATION_STEPS, sword_fx, 0, 100, 100, 80, 100,-1,-1,-1,90, 5, [1,-1,-1,-1,-1],-1,[0,0], 12)
  if 16 in hero.amulet_hero:
    fighter_2.not_damage -= 2
    if fighter_3 != False:
        fighter_3.not_damage -= 2
  if 4 in hero.amulet_hero:
      fighter_1.damage += fighter_1.damage * 0.5
      fighter_2.damage += fighter_2.damage * 0.5
      if fighter_3 != False:
          fighter_3.damage += fighter_3.damage * 0.5
  if 10 in hero.amulet_hero and fighter_4 != False:
      fighter_4.damage += fighter_4.damage * 0.5
      fighter_4.health_max += 25
      fighter_4.health += 25
  #основной цикл
  run = True
  win = 0
  while run:

    clock.tick(FPS)

    draw_bg()

    draw_health_bar(fighter_1.health, 20, 20,hero.health_max)
    draw_health_bar(fighter_2.health, 540, 20,fighter_2.health_max)
    if fighter_3 != False:
        draw_health_bar(fighter_3.health, 540, 60,fighter_3.health_max)
    if fighter_4 != False:
        draw_health_bar(fighter_4.health, 20, 60,fighter_4.health_max)

    if fighter_4 == False:
        draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
    else:
        draw_text("P1: " + str(score[0]), score_font, RED, 20, 150)
    if fighter_3 == False:
        draw_text("P2: " + str(score[1]), score_font, RED, 540, 60)
    else:
        draw_text("P2: " + str(score[1]), score_font, RED, 540, 90)

    if intro_count <= 0:
      fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over, fighter_3)
      fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over, fighter_4)
      if fighter_3 != False:
          fighter_3.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over,fighter_4)
      if fighter_4 != False:
          fighter_4.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over,fighter_3)
      if fighter_5 != False:
          fighter_5.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over,fighter_3)
      if fighter_6 != False:
          fighter_6.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over,fighter_1)
      if fighter_7 != False:
          fighter_7.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over,fighter_3)
    else:
      draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()

    fighter_1.update(fighter_2,fighter_3,screen)
    fighter_2.update(fighter_1,fighter_4,screen)
    if fighter_3 != False:
       fighter_3.update(fighter_1,fighter_4,screen)
    if fighter_4 != False:
       fighter_4.update(fighter_2,fighter_3,screen)
    if fighter_5 != False:
       fighter_5.update(fighter_2,fighter_3,screen)
    if fighter_6 != False:
       fighter_6.update(fighter_2,fighter_1,screen)
    if fighter_7 != False:
       fighter_7.update(fighter_2,fighter_3,screen)

    fighter_1.draw(screen)
    fighter_2.draw(screen)
    if fighter_3 != False:
       fighter_3.draw(screen)
    if fighter_4 != False:
       fighter_4.draw(screen)
    if fighter_5 != False:
       fighter_5.draw(screen)
    if fighter_6 != False:
       fighter_6.draw(screen)
    if fighter_7 != False:
       fighter_7.draw(screen)

    if fighter_1.cooldown != -1 or fighter_1.cooldown_5 != -1:
      screen.blit(icon5, (20, 100))
      if fighter_1.cooldown != -1:
        if fighter_1.cooldown_rolling_over > 0:
            screen.blit(circle_surf(23, (150, 0, 0)), (13, 93))
        else:
            screen.blit(circle_surf(23, (0, 150, 0)), (13, 93))
      if fighter_1.cooldown_5 != -1:
        if fighter_1.attack_cooldown5 > 0:
            screen.blit(circle_surf(23, (150, 0, 0)), (13, 93))
        else:
            screen.blit(circle_surf(23, (0, 150, 0)), (13, 93))
    if fighter_1.cooldown_1 != -1:
      screen.blit(icon1, (70, 100))
      if fighter_1.attack_cooldown1 > 0:
          screen.blit(circle_surf(23, (150, 0, 0)), (63, 93))
      else:
          screen.blit(circle_surf(23, (0, 150, 0)), (63, 93))
    if fighter_1.cooldown_2 != -1:
      screen.blit(icon2, (120, 100))
      if fighter_1.attack_cooldown2 > 0:
          screen.blit(circle_surf(23, (150, 0, 0)), (113, 93))
      else:
          screen.blit(circle_surf(23, (0, 150, 0)), (113, 93))
    if fighter_1.cooldown_3 != -1:
      screen.blit(icon3, (170, 100))
      if fighter_1.attack_cooldown3 > 0:
          screen.blit(circle_surf(23, (150, 0, 0)), (163, 93))
      else:
          screen.blit(circle_surf(23, (0, 150, 0)), (163, 93))
    if fighter_1.cooldown_4 != -1:
      screen.blit(icon4, (220, 100))
      if fighter_1.attack_cooldown4 > 0:
          screen.blit(circle_surf(23, (150, 0, 0)), (213, 93))
      else:
          screen.blit(circle_surf(23, (0, 150, 0)), (213, 93))

    if round_over == False:
      if fighter_4 != False:
        if fighter_1.alive == False and fighter_4.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False and fighter_3 == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
      elif fighter_1.alive == False:
        score[1] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
      elif fighter_3 != False:
        if fighter_2.alive == False and fighter_3.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
      elif fighter_2.alive == False and fighter_3 == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
      screen.blit(victory_img, (260, 150))
      if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
        round_over = False
        intro_count = 3
        #fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 10,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,hero.cooldown_5,90,hero.damage,hero.attack_hero)
        rolling_over = 20
        if -1 in hero.attack_hero:
            if hero.cooldown_1 == rolling_over:
                fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 11, hero.cooldown_5 ,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,hero.cooldown_1,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
            elif hero.cooldown_2 == rolling_over:
                fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 11,hero.cooldown_1,hero.cooldown_5,hero.health_max,hero.cooldown_3,hero.cooldown_4,hero.cooldown_2,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
            elif hero.cooldown_3 == rolling_over:
                fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 11,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_5,hero.cooldown_4,hero.cooldown_3,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
            elif hero.cooldown_4 == rolling_over:
                fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 11,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_5,hero.cooldown_4,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
            else:
                fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 11,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,-1,90,hero.damage,hero.attack_hero,hero.cooldown_5,hero.amulet_hero)
        else:
            if hero.cooldown_5 == rolling_over:
                fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 11,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,hero.cooldown_5,90,hero.damage,hero.attack_hero,-1,hero.amulet_hero)
            else:
                fighter_1 = Fighter(2, 100, 350, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, 2, fighter_1.health + 11,hero.cooldown_1,hero.cooldown_2,hero.health_max,hero.cooldown_3,hero.cooldown_4,-1,90,hero.damage,hero.attack_hero,hero.cooldown_5,hero.amulet_hero)
        if 5 in hero.amulet_hero:
            fighter_1.rolling_over_speed += 2
        if 6 in hero.amulet_hero:
            fighter_1.attack_anim = 40
            fighter_1.speed_anim = 80
        if fighter_1.health > hero.health_max:
            fighter_1.health = hero.health_max
        fighter_1.speed1 = hero.speedx * 2 - (hero.speedx // 15)
        if hero.hard == 1:
            fighter_1.damage = hero.damage * 3
        elif hero.hard == 2:
            fighter_1.damage = hero.damage * 2.5
        else:
            fighter_1.damage = hero.damage * 2
        
        fighter_5 = False
        fighter_6 = False
        fighter_7 = False
        if 18 in hero.amulet_hero:
            fighter_5 = Fighter(7, 10, 450, True, SLAIM_DATA, slaim_sheet, SLAIM_ANIMATION_STEPS,slaim_fx, 0, 100,20,-1,100,-1,-1,-1,40,4)
            if 17 in hero.amulet_hero:
                fighter_5.damage += 3
        if 19 in hero.amulet_hero:
            fighter_6 = Fighter(252, 100, 450, True, SLAIM_TREE_DATA, slaim_tree_sheet, SLAIM_TREE_ANIMATION_STEPS, magic_fx, 0,90,11,11,100,-1,-1,-1,40,1.5)
            if 17 in hero.amulet_hero:
                fighter_6.damage += 2
        if 20 in hero.amulet_hero:
            fighter_7 = Fighter(23, 20, 320, False, EYE_DATA, eye_sheet, EYE_ANIMATION_STEPS, magic_fx, 0, 100,40,-1,100,-1,-1,-1,90,8)
            if 17 in hero.amulet_hero:
                fighter_7.damage += 2
        #fighter_2 = Fighter(4, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 2)
        fighter_3 = False
        fighter_4 = False
        if type == 1:
            fighter_2 = Fighter(7, 600, 450, True, SLAIM_DATA, slaim_sheet, SLAIM_ANIMATION_STEPS,slaim_fx, 0, 70, 100, 100, 100, -1,-1,-1, 100, 5)
        elif type == 2:
            fighter_2 = Fighter(5, 600, 350, True, NINJA_DATA, ninja_sheet, NINJA_ANIMATION_STEPS, sword_fx, 0, 90, 17, 17, 100, -1, -1, -1, 130, 1.5, [1,-1,-1,-1,-1],-1,[0,0],1)
        elif type == 22:
            fighter_2 = Fighter(55, 600, 350, True, NINJA_DATA, ninja_evil_sheet, NINJA_EVIL_ANIMATION_STEPS, sword_fx, 180, 17, 17, 200, -1, -1, -1, 130, 3, [1,-1,-1,-1,-1],-1,[0,0],12)
        elif type == 3:
            fighter_2 = Fighter(9, 600, 350, True, NINJA2_DATA, ninja2_sheet, NINJA2_ANIMATION_STEPS, sword_fx, 0, 140, 50, 70, 150, -1, -1, -1, 180, 2, [1,-1,-1,-1,-1],-1,[0,0],2)
        elif type == 33:
            fighter_2 = Fighter(9, 600, 350, True, NINJA2_DATA, ninja2_sheet, NINJA2_ANIMATION_STEPS, sword_fx, 0, 110, 70, 90, 150, -1, -1, -1, 180, 2, [1,-1,-1,-1,-1],-1,[0,0],2)
            fighter_3 = Fighter(9, 400, 350, True, NINJA2_DATA, ninja2_sheet, NINJA2_ANIMATION_STEPS, sword_fx, 0, 110, 60, 80, 150, -1, -1, -1, 180, 2, [1,-1,-1,-1,-1],-1,[0,0],2)
        elif type == 4:
            fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 280, 30, -1, 300, -1, -1, -1, 450, 25)
        elif type == 44:
            fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
        elif type == 414:
            fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 260, 30, -1, 300, -1, -1, -1, 450, 25)
            fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 60, 60, 80, 150, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 2)
        elif type == 415:
            fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 260, 30, -1, 300, -1, -1, -1, 450, 25)
            fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people2_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 55, 80, 60, 100, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 6)
        elif type == 416:
            fighter_2 = Fighter(11, 600, 450, True, WORM_DATA, worm_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 260, 30, -1, 300, -1, -1, -1, 450, 25)
            fighter_4 = Fighter(33, 200, 350, False, PEOPLE3_DATA, people3_sheet, PEOPLE3_ANIMATION_STEPS, sword_fx, 0, 50, 30, 50, 100, 60, 40, -1, 100, 4,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 4)
        elif type == 4414:
            fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
            fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 40, 60, 80, 150, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 2)
        elif type == 4415:
            fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
            fighter_4 = Fighter(29, 200, 350, False, PEOPLE_DATA, people2_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 45, 80, 60, 100, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 6)
        elif type == 4416:
            fighter_2 = Fighter(31, 600, 450, True, WORM_DATA, worm2_sheet, WORM_ANIMATION_STEPS, worm_fx, 0, 300, 30, -1, 300, -1, -1, -1, 450, 35, [1,-1,-1,-1,-1],-1,[0,0,0],2)
            fighter_4 = Fighter(33, 200, 350, False, PEOPLE3_DATA, people3_sheet, PEOPLE3_ANIMATION_STEPS, sword_fx, 0, 50, 30, 50, 100, 60, 40, -1, 100, 4,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 4)
        elif type == 5:
            fighter_2 = Fighter(13, 600, 350, True, WITCH_DATA, witch_sheet, WITCH_ANIMATION_STEPS, magic_fx, 0, 140, 80, 80, 150, -1, -1, -1, 100, 7)
        elif type == 6:
            fighter_2 = Fighter(15, 600, 350, True,  MAG_DATA, mag_sheet, MAG_ANIMATION_STEPS, magic2_fx, 0, 240, 40,50,250,-1,-1,-1,90,3)
        elif type == 66:
            fighter_2 = Fighter(15, 600, 350, True,  MAG_DATA, mag_sheet2, MAG_ANIMATION_STEPS, magic2_fx, 0, 280, 40,50,300,-1,-1,-1,90,4,[1,-1,-1,-1,-1],-1,[0,0],6)
        elif type == 7:
            fighter_2 = Fighter(17, 600, 350, True, KNIGHT_DATA, knight_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, 0, 220, 40, -1, 250, -1, -1, 140, 100, 6,[1,-1,-1,-1,-1],-1,[0,0,0,0,0], 8)
        elif type == 77:
            fighter_2 = Fighter(17, 600, 350, True, KNIGHT_DATA, knight_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, 0, 220, 40, -1, 250, -1, -1, 140, 100, 6,[1,-1,-1,-1,-1],-1,[0,0,0,0,0], 8)
            fighter_4 = Fighter(15, 600, 350, True,  MAG_DATA, mag_sheet, MAG_ANIMATION_STEPS, magic2_fx, 0, 200, 40,50,270,-1,-1,-1,90,3)
        elif type == 8:
            fighter_2 = Fighter(3, 600, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 0, 360,80,100,400,-1,-1,-1,180,6,[1,1,-1,-1,-1],-1,[0,0,0,0,0],1)
        elif type == 85:
            fighter_2 = Fighter(3, 600, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 0, 380,80,100,400,-1,-1,-1,180,6,[1,1,-1,-1,-1],-1,[0,0,0,0,0],3)
            fighter_4 = Fighter(13, 50, 350, False, WITCH_DATA, witch_sheet, WITCH_ANIMATION_STEPS, magic_fx, 0, 90, 80, 80, 150, -1, -1, -1, 100, 7)
        elif type == 810:
            fighter_2 = Fighter(3, 600, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, 0, 390,80,100,400,-1,-1,-1,180,6,[1,1,-1,-1,-1],-1,[0,0,0,0,0],2)
            fighter_4 = Fighter(21, 50, 350, False, ASSISTANT_DATA, assistant_sheet, ASSISTANT_ANIMATION_STEPS, magic_fx, 0, 190, 20, -1, 200,-1,-1,-1,180,9,[1,1,-1,-1,-1],-1,[0,0,0,0,0],8)
        elif type == 9:
            fighter_2 = Fighter(19, 600, 450, True, SLAIM_DATA, slaim_bro_sheet, SLAIM_BRO_ANIMATION_STEPS,slaim_fx, 0, 100, 40, 40, 100, -1, -1, -1, 60, 6)
        elif type == 10:
            fighter_2 = Fighter(21, 600, 350, True, ASSISTANT_DATA, assistant_sheet, ASSISTANT_ANIMATION_STEPS, magic_fx, 0, 190, 20, -1, 200,-1,-1,-1,180,9,[1,1,-1,-1,-1],-1,[0,0,0,0,0],10)
        elif type == 11:
            fighter_2 = Fighter(23, 600, 350, True, EYE_DATA, eye_sheet, EYE_ANIMATION_STEPS, magic_fx, 0, 70,30,200,70,-1,-1,-1,200,7,[1,1,-1,-1,-1],-1,[0,0,0,0,0],4)
        elif type == 12:
            fighter_2 = Fighter(25, 600, 450, True, SLAIM_TREE_DATA, slaim_tree_sheet, SLAIM_TREE_ANIMATION_STEPS, magic_fx, 0, 170,10,10,200,-1,-1,-1,110,3)
        elif type == 13:
            fighter_2 = Fighter(27, 600, 450, True, SLAIM_TREE_DATA, slaim_farmer_sheet, SLAIM_TREE_ANIMATION_STEPS, magic_fx, 0, 200,10,10,200,-1,-1,-1,110, 10,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 12)
        elif type == 14:
            fighter_2 = Fighter(29, 600, 350, True, PEOPLE_DATA, people_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 140, 60, 80, 150, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 2)
        elif type == 15:
            fighter_2 = Fighter(29, 600, 350, True, PEOPLE_DATA, people2_sheet, PEOPLE_ANIMATION_STEPS, sword_fx, 0, 95, 80, 60, 100, -1, -1, -1, 100, 5,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 5)
        elif type == 16:
            fighter_2 = Fighter(33, 600, 350, True, PEOPLE3_DATA, people3_sheet, PEOPLE3_ANIMATION_STEPS, sword_fx, 0, 90, 30, 50, 100, 60, 40, -1, 100, 4,[1,1,-1,-1,-1],-1,[0,0,0,0,0,0], 3)
        elif type == 17:
            fighter_2 = Fighter(35, 600, 350, True, KNIGHT2_DATA, knight2_sheet, KNIGHT2_ANIMATION_STEPS, sword_fx, 0, 100, 100, 80, 100,-1,-1,-1,90, 5, [1,-1,-1,-1,-1],-1,[0,0], 12)        
        fighter_1.repulsion = hero.repulsion
        if 4 in hero.amulet_hero:
            fighter_1.damage += fighter_1.damage * 0.5
            fighter_2.damage += fighter_2.damage * 0.5
            if fighter_3 != False:
                fighter_3.damage += fighter_3.damage * 0.5
        if 16 in hero.amulet_hero:
            fighter_2.not_damage -= 2
            if fighter_3 != False:
                fighter_3.not_damage -= 2
        if 10 in hero.amulet_hero and fighter_4 != False:
            fighter_4.damage += fighter_4.damage * 0.5
            fighter_4.health_max += 25
            fighter_4.health += 25

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
    if score[0] == 3:
      run = False
      win = 1
    elif score[1] == 3 or hero.health <= 0:
      run = False
      win = 0
    pygame.display.update()
    if fighter_1.health > hero.health_max:
       fighter_1.health = hero.health_max 
    if fighter_1.health <= 0 and win == 1:
        fighter_1.health = 10
  return fighter_1.health, win