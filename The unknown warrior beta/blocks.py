
from random import randint
from pygame import *
import pygame
import pyganim
pygame.init()
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR2 = "#000000"
PLATFORM_COLOR = "#555500"

sword_fx = pygame.mixer.Sound("sound/sword.wav")
sword_fx.set_volume(0.1)
WARRIOR_SIZE = 162
WARRIOR_SCALE = 1.5
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
#warrior_sheet = pygame.image.load("assets/battle/warrior.png").convert_alpha()

class Img_stat(sprite.Sprite):
    def __init__(self, x, y, w, h, img, xbool = False, ybool = False, big=False,bigw=100,bigh=100,type=1,save=1):
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image = image.load(img).convert_alpha()
        self.type = type
        self.save = save
        self.image = pygame.transform.flip(self.image, xbool, ybool)
        if big:
            self.image =  pygame.transform.scale(self.image, (bigw,bigh))
        self.rect = Rect(x, y, w, h)

class Img_stat2(sprite.Sprite):
    def __init__(self, x, y, w, h, img, xbool = False, ybool = False):
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image = image.load(img).convert_alpha()
        self.rect = Rect(x, y, w, h)
    def draw(self,surface):
        surface.blit(self.image, self.rect)


class Img_t(sprite.Sprite):
    def __init__(self, x, y, img, img2, xbool = False, ybool = False):
        sprite.Sprite.__init__(self)
        #self.image1 = Surface((w, h))
        self.image1 = image.load(img).convert_alpha()
        self.image2 = image.load(img2).convert_alpha()
        self.rect = Rect(x, y, 300,50)
        self.rect2 = Rect(x + 100, y, 50,50)
        self.clicked = False
    def draw(self, surface, test):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.rect2.centerx = pos[0]
                    if self.rect2.centerx >= self.rect.x + 20:
                        test = (self.rect2.centerx - self.rect.x) / 600 #500
                    else:
                        test = 0

        surface.blit(self.image1, self.rect)
        surface.blit(self.image2, self.rect2)
        return test

class Img_button(sprite.Sprite):
    def __init__(self, x, y, w, h, img, img2):
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image = image.load(img).convert_alpha()
        self.image1 = image.load(img).convert_alpha()
        self.image2 = image.load(img2).convert_alpha()
        self.rect = Rect(x, y, w, h)
        self.clicked = False
    def draw(self, surface, hero,type):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.image = self.image2 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if type == -1:
                    hero.location = -1
                    hero.winner = True
                if type == 1:
                    hero.pause = -hero.pause
                if type == 2:
                    hero.location = -1
                    hero.winner = True
                if type == 3:
                    hero = 1
                if type == 4:
                    hero = 2
                if type == 5:
                    hero = 3
                if type < -1:
                    hero = -type // 2
                self.clicked = True
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked =  False
            self.image = self.image1

        surface.blit(self.image, self.rect)
        return hero

class Anim_img(sprite.Sprite):
    def __init__(self, x, y, w, h, img, xbool = False, ybool = False):
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image.fill(Color(PLATFORM_COLOR2))
        self.image.set_colorkey(Color(PLATFORM_COLOR2))
        self.rect = Rect(x, y, w, h)
        boltAnim = []
        for anim in img:
            boltAnim.append((anim, 0.1))
        self.boltAnim = pyganim.PygAnimation(boltAnim, xbool, ybool)
        self.boltAnim.play()
        
    def update(self):
        self.image.fill(Color(PLATFORM_COLOR2))
        self.boltAnim.blit(self.image, (0, 0))

class Anim_img2(sprite.Sprite):
    def __init__(self, x, y, w, h, img,img2,type, xbool = False, ybool = False, big=False,bigw=100,bigh=100,character='people'):
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image.fill(Color(PLATFORM_COLOR2))
        self.image.set_colorkey(Color(PLATFORM_COLOR2))
        self.rect = Rect(x, y, w, h)
        boltAnim = []
        for anim in img:
            boltAnim.append((anim, 0.1))
        self.boltAnim = pyganim.PygAnimation(boltAnim,xbool,ybool,big,bigw,bigh)
        self.boltAnim.play()
        boltAnim2 = []
        for anim in img2:
            boltAnim2.append((anim, 0.1))
        self.boltAnim2 = pyganim.PygAnimation(boltAnim2,xbool,ybool,big,bigw,bigh)
        self.boltAnim2.play()
        self.win = 0
        self.character = character
        self.type = type
        
    def update(self,hero,screen):
        if self.win <= 0:
            self.image.fill(Color(PLATFORM_COLOR2))
            self.boltAnim.blit(self.image, (0, 0))
        else:
            self.image.fill(Color(PLATFORM_COLOR2))
            self.boltAnim2.blit(self.image, (0, 0))

class Img_break(sprite.Sprite):
    def __init__(self, x, y, w, h, imag, life, die, hp, hp_max, type = 2, xbool = False, ybool = False):
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image = image.load(imag).convert_alpha()
        self.image = pygame.transform.flip(self.image, xbool, ybool)
        if type == 0:
            self.rect = Rect(x, y, w // 1.5, h // 1.2)
        else:
            self.rect = Rect(x, y, w, h)
        self.life = life
        self.die = image.load(die).convert_alpha()
        self.die = pygame.transform.flip(self.die, xbool, ybool)
        self.hp = hp
        self.hp_max = hp_max
        self.test = 1
        self.type = type
    def update(self,attaka,hero):
        if pygame.sprite.collide_rect(attaka, self):
            self.life -= hero.damage
        if self.life <= 0 and self.test == 1:
            hero.health += self.hp
            if hero.health_max >= 10:
                hero.health_max += self.hp_max
            if self.hp == 9:
                hero.boom += 1
            if hero.health > hero.health_max:
                hero.health = hero.health_max
            if hero.health <= 0:
                hero.end = self.type
            self.image = self.die
            self.test = -1
        if self.life <= -20 and self.type != 0:
            hero.health += -self.hp
            if hero.health > hero.health_max:
                hero.health = hero.health_max
            if hero.health <= 0:
                hero.end = self.type
            self.kill()
        #pygame.draw.rect(screen,(0,200,0),self.rect)

class Dialogue_img(sprite.Sprite):
    def __init__(self, x, y, w, h, img, img2, img3, icon, icon2, icon3, fait, size_t, type, character, text = [], xbool = False, ybool = False,big=False,bigw=100,bigh=100,play_anim=0.1):
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, w, h)
        boltAnim = []
        for anim in img:
            boltAnim.append((anim, play_anim))
        self.boltAnim = pyganim.PygAnimation(boltAnim,xbool,ybool,big,bigw,bigh)
        self.boltAnim.play()
        boltAnim2 = []
        for anim in img2:
            boltAnim2.append((anim, play_anim))
        self.boltAnim2 = pyganim.PygAnimation(boltAnim2,xbool,ybool,big,bigw,bigh)
        self.boltAnim2.play()
        if img3 != 0:
            boltAnim3 = []
            for anim in img3:
                boltAnim3.append((anim, play_anim))
            self.boltAnim3 = pyganim.PygAnimation(boltAnim3,xbool,ybool,big,bigw,bigh)
        else:
            boltAnim3 = []
            for anim in img:
                boltAnim3.append((anim, play_anim))
            self.boltAnim3 = pyganim.PygAnimation(boltAnim3,xbool,ybool,big,bigw,bigh)
        self.boltAnim3.play()
        self.image1 = image.load('assets/other/window.png').convert_alpha()
        self.icon = image.load(icon).convert_alpha()
        self.icon2 = image.load(icon2).convert_alpha()
        if icon3 != 0:
            self.icon3 = image.load(icon3).convert_alpha()
        else:
            self.icon3 = image.load(icon).convert_alpha()
        self.last = 0
        self.cooldown_run = 40
        for i in range(16 - len(text)):
            text.append('')
        self.text = text[0]
        self.text2 = text[1]
        self.text3 = text[2]
        self.text4 = text[3]
        self.text5 = text[4]
        self.text6 = text[5]
        self.text7 = text[6]
        self.text8 = text[7]
        self.text9 = text[8]
        self.text10 = text[9]
        self.text11 = text[10]
        self.text12 = text[11]
        self.text13 = text[12]
        self.text14 = text[13]
        self.text15 = text[14]
        self.text16 = text[15]
        self.fait = fait
        self.quest = -1
        self.quest2 = -1
        self.win = -1
        self.death = -1
        self.character = character
        self.test = -1
        self.test2 = -1
        self.test3 = -1
        self.test4 = -1
        self.list_t = str()
        self.list_t2 = str()
        self.list_t3 = str()
        self.list_t4 = str()
        self.score_font = pygame.font.Font("fonts/game.ttf", size_t)
        self.size_t = size_t
        self.type = type
        self.dialogue = 1
        
    def update(self,hero,screen):
        if self.type == 1:
            if self.win != 1 and self.quest != 1:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim.blit(self.image, (0, 0))
            elif self.win == 1:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim2.blit(self.image, (0, 0))
            elif self.win <= 0 and self.quest == 1:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim3.blit(self.image, (0, 0))
        if self.type == 2:
            if self.win != 1 and self.quest != 1:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim.blit(self.image, (0, 0))
            else:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim2.blit(self.image, (0, 0))
        if self.type == 3:
            if self.win != 1 and self.quest != 1:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim.blit(self.image, (0, 0))
            elif self.win != 1 and self.quest == 1:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim3.blit(self.image, (0, 0))
            else:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim2.blit(self.image, (0, 0))
        if self.type == 4:
            if self.win != 1:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim.blit(self.image, (0, 0))
            else:
                self.image.fill(Color(PLATFORM_COLOR))
                self.boltAnim2.blit(self.image, (0, 0))
        if pygame.sprite.collide_rect(hero, self):
            if self.type == 1:
                if self.win == 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text5
                    self.text2 = self.text6
                    self.text3 = self.text7
                    self.text4 = self.text8
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                elif self.quest == 1 and self.win <= 0 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text13
                    self.text2 = self.text14
                    self.text3 = self.text15
                    self.text4 = self.text16
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                elif self.win == 0 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text9
                    self.text2 = self.text10
                    self.text3 = self.text11
                    self.text4 = self.text12
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
            if self.type == 2:
                if self.win == 1 and self.quest != 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text5
                    self.text2 = self.text6
                    self.text3 = self.text7
                    self.text4 = self.text8
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                elif self.quest == 1 and self.quest2 != 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text9
                    self.text2 = self.text10
                    self.text3 = self.text11
                    self.text4 = self.text12
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                elif self.quest2 == 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text13
                    self.text2 = self.text14
                    self.text3 = self.text15
                    self.text4 = self.text16
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
            if self.type == 3:
                if self.win == 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text5
                    self.text2 = self.text6
                    self.text3 = self.text7
                    self.text4 = self.text8
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                elif self.quest == 1 and self.win != 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text9
                    self.text2 = self.text10
                    self.text3 = self.text11
                    self.text4 = self.text12
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                else:
                    self.dialogue = 2
            if self.type == 4:
                if self.win == 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text5
                    self.text2 = self.text6
                    self.text3 = self.text7
                    self.text4 = self.text8
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                elif self.quest == 1 and self.win != 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text9
                    self.text2 = self.text10
                    self.text3 = self.text11
                    self.text4 = self.text12
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
                elif self.quest2 == 1 and self.win != 1 and self.dialogue == 1:
                    self.dialogue = 2
                    self.text = self.text13
                    self.text2 = self.text14
                    self.text3 = self.text15
                    self.text4 = self.text16
                    self.test = -1
                    self.test2 = -1
                    self.test3 = -1
                    self.test4 = -1
                    self.list_t = str()
                    self.list_t2 = str()
                    self.list_t3 = str()
                    self.list_t4 = str()
        if pygame.sprite.collide_rect(hero, self):
            screen.blit(self.image1, (0,0))
            if self.win != 1 and self.quest != 1:
                screen.blit(self.icon, (0,0))
            elif self.win >= 0:
                screen.blit(self.icon2, (0,0))
            elif self.win <= 0 and self.quest == 1:
                screen.blit(self.icon3, (0,0))
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown_run:
                self.last = now
                if len(self.text) != self.test:
                    self.test += 1
                if len(self.text) > self.test:
                    self.list_t += self.text[self.test]
                if len(self.text) == self.test:
                    if len(self.text2) != self.test2:
                        self.test2 += 1
                    if len(self.text2) > self.test2:
                        self.list_t2 += self.text2[self.test2]
                    if len(self.text2) == self.test2:
                        if len(self.text3) != self.test3:
                            self.test3 += 1
                        if len(self.text3) > self.test3:
                            self.list_t3 += self.text3[self.test3]
                        if len(self.text3) == self.test3:
                            self.test4 += 1
                            if len(self.text4) > self.test4:
                                self.list_t4 += self.text4[self.test4]
            text_surface = self.score_font.render(self.list_t, False, (0, 0, 0))
            text_surface2 = self.score_font.render(self.list_t2, False, (0, 0, 0))
            text_surface3 = self.score_font.render(self.list_t3, False, (0, 0, 0))
            text_surface4 = self.score_font.render(self.list_t4, False, (0, 0, 0))
            screen.blit(text_surface, (210,self.size_t - 10))
            screen.blit(text_surface2, (210,self.size_t * 2))
            screen.blit(text_surface3, (210,self.size_t * 3 + 10))
            screen.blit(text_surface4, (210,self.size_t * 4 + 20))
            #draw_text(self.list_t, score_font, (0,0,0), 0, 0)
        if self.death == 1:
            self.kill()
