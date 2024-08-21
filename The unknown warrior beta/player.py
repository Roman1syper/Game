from pygame import *
#import pyganim
import blocks
import pygame
from random import randint
from copy import deepcopy

particles = []

class Player(sprite.Sprite):
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps,hard,sound,attack_hero=[1,0,0,0,0],amulet_hero=[0,0,0,0,0,0],cooldown=[-1,-1,-1,-1,-1]):
        self.location = 1
        self.player = player
        self.hard = hard 
        self.winner = False
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:idle #1:run #2:jump #3:attack1 #4: attack2 #5:hit #6:death location
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 33, 68))
        self.yvel = 0
        self.xvel = 0
        self.repulsion = 1.75
        if hard <= 2:
            self.speedx = 5.5
            self.speedy = 5
        else:
            self.speedx = 5
            self.speedy = 4.5
        if 1 in amulet_hero:
            self.speedx += self.speedx / 100 * 15
            self.speedy += self.speedy / 100 * 15
        self.attacking = False
        self.attack_hero = attack_hero
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack_sound = sound
        self.hit = False
        self.health = 100 // hard
        self.alive = True
        self.particles = False
        self.attack1 = 0
        self.damage = 4
        self.health_max = 140 - (20 * hard)
        self.end = -1
        self.pause = -1
        self.reset = -1
        self.musec = 0.2
        self.effect = 0.2
        self.attack_hero = attack_hero
        self.amulet_hero = amulet_hero
        self.boom = 0
        self.cooldown_1 = cooldown[0]
        self.cooldown_2 = cooldown[1]
        self.cooldown_3 = cooldown[2]
        self.cooldown_4 = cooldown[3]
        self.cooldown_5 = cooldown[4]

    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
    

    def update(self, left, right, up, down, screen, platforms, camera):

        if up and self.attack_type == 0:
            self.yvel = -self.speedy
        
        if down and self.attack_type == 0:
            self.yvel = self.speedy
                       
        if left and self.attack_type == 0:
            self.flip = True
            self.xvel = -self.speedx # Лево = x- n
 
        if right and self.attack_type == 0:
            self.flip = False
            self.xvel = self.speedx # Право = x + n
        
        if self.attack_type == 1:
            if self.attacking == False:
                self.particles = False
                self.update_action(3)
                self.attacking = True
                self.attack_sound.play()
                self.attack(screen, camera)
        elif right or left or up or down:
            self.particles = True
            self.update_action(1)
        elif not (left or right) and not (up or down): # стоим, когда нет указаний идти
            self.particles = False
            self.update_action(0)
        elif self.hit == True:
            self.particles = False
            self.update_action(5)

        if not (left or right):
            self.xvel = 0
        if not (up or down):
            self.yvel = 0
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        animation_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = self.cooldown_1
                    self.attack_type = 0
                if self.action == 5:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 20 
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)
   
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком
                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    def attack(self, surface, camera):
        if self.attack_cooldown == 0:
            if self.flip:
                self.dop = -0.65
            else:
                self.dop = 1
            if self.attack_type == 1:
                attacking_rect = Attaka(self.rect.centerx - (2.5 * self.rect.width * self.flip), self.rect.y, 2.25 * self.rect.width, self.rect.height)
                rect1 = deepcopy(attacking_rect)
                rect1.rect.top += camera.top
                rect1.rect.left += camera.left
            if self.attack_type == 2:
                attacking_rect = pygame.Rect(self.rect.centerx - (2.5 * self.rect.width), self.rect.y, 5 * self.rect.width, self.rect.height)
            return attacking_rect
    def test(self, surface, camera):
        attacking_rect = Attaka(self.rect.centerx - (2.5 * self.rect.width * self.flip), self.rect.y, 2.25 * self.rect.width, self.rect.height)
        return attacking_rect

    def draw(self, surface, camera, circle_surf):
        rect = deepcopy(self.rect)
        rect.top += camera.top
        rect.left += camera.left

        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (rect.x - (self.offset[0] * self.image_scale), rect.y - (self.offset[1] * self.image_scale)))
        if self.particles:
            if not self.flip:
                my = rect.y - (self.offset[1] * self.image_scale) + 150
                mx = rect.x - (self.offset[0] * self.image_scale) + 100
                particles.append([[mx, my], [randint(-8, -1) , randint(-2, -1)], randint(1, 3)])
            else:
                my = rect.y - (self.offset[1] * self.image_scale) + 150
                mx = rect.x - (self.offset[0] * self.image_scale) + 146
                particles.append([[mx, my], [randint(1, 8) , randint(-2, -1)], randint(1, 3)])

            for particle in particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.15
                particle[1][1] += 0.1

                radius = particle[2] 
                surface.blit(circle_surf(radius, (70, 80, 60)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)

                if particle[2] <= 0.05:
                    particles.remove(particle)

class Attaka(sprite.Sprite):
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)