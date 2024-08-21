import pygame
import time
from random import randint
class Fighter():
  def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound, choice, health,cooldown_1 = 20,cooldown_2 = 30,health_max = 100,cooldown_3 = 50,cooldown_4 = 40, cooldown = 50, speed_anim = 90, damage = 10,attack_hero=[1,-1,-1,-1,-1],cooldown_5=60,amulet=[0,0,0,0,0,0],not_damage=0):
    self.player = player
    self.size = data[0]
    self.image_scale = data[1]
    self.offset = data[2]
    self.size2 = data[3]
    self.flip = flip
    self.animation_list = self.load_images(sprite_sheet, animation_steps)
    self.action = 0 #0:idle #1:run #2:jump #3:attack1 #4: attack2 #5:hit #6:death
    self.frame_index = 0
    self.image = self.animation_list[self.action][self.frame_index]
    self.update_time = pygame.time.get_ticks()
    if self.player == 7 or self.player == 19:
      self.rect = pygame.Rect((x, y, 108, 70))
    elif self.player == 11 or self.player == 31:
      self.rect = pygame.Rect((x, y, 140, 70))
    elif self.player == 23:
      self.rect = pygame.Rect((x, y, 100, 100))
    elif self.player == 25 or self.player == 27 or self.player == 252:
      self.rect = pygame.Rect((x, y, 100, 80))
    else:
      self.rect = pygame.Rect((x, y, 80, 180))
    self.atak = False
    self.vel_y = 0
    self.running = False
    self.jump = False
    self.attacking = False
    self.rolling_over = False
    self.attack_type = 0
    self.amulet = amulet
    self.repulsion = 0
    self.attack_anim = 45
    self.attack_cooldown1 = cooldown_1 // 2
    self.attack_cooldown2 = cooldown_2 // 2
    self.attack_cooldown3 = cooldown_3 // 2
    self.attack_cooldown4 = cooldown_4 // 2
    self.attack_cooldown5 = cooldown_5 // 2
    self.cooldown_rolling_over = cooldown 
    self.rolling_over_speed = 15
    if 15 in amulet:
      self.cooldown_1 = int(cooldown_1 * 0.85)
      self.cooldown_2 = int(cooldown_2 * 0.85)
      self.cooldown_3 = int(cooldown_3 * 0.85)
      self.cooldown_4 = int(cooldown_4 * 0.85)
      self.cooldown_5 = int(cooldown_5 * 0.85)
    else:
      self.cooldown_1 = cooldown_1
      self.cooldown_2 = cooldown_2
      self.cooldown_3 = cooldown_3
      self.cooldown_4 = cooldown_4
      self.cooldown_5 = cooldown_5
    self.cooldown = cooldown
    self.attack_sound = sound
    self.hit = False
    self.health = health
    self.health_max = health_max
    if self.health > self.health_max:
      self.health = self.health_max
    self.alive = True
    #self.cooldown = 500
    self.cooldown_run = 2500
    self.cooldown2 = 1200
    self.last2 = 0
    self.last3 = 0
    self.random = 3
    self.speed1 = 10
    self.not_damage = not_damage
    if 3 in amulet:
      self.not_damage += 2
    if 14 in amulet:
      self.not_damage += 4
    if 12 in amulet:
      self.not_damage += 1
    if 2 in amulet:
      self.speed2 = 1.42
    else:
      self.speed2 = 1.5
    self.yin_and_yang = False
    self.run = 1
    self.choice = choice
    self.jump_random = 2
    self.damage = damage
    self.cooldown_test = 4
    self.heal = 1
    self.speed_anim = speed_anim
    self.attack_hero = attack_hero
    self.hero_cooldown = [cooldown_1,cooldown_2,cooldown_3,cooldown_4]


  def load_images(self, sprite_sheet, animation_steps):
    animation_list = []
    for y, animation in enumerate(animation_steps):
      temp_img_list = []
      for x in range(animation):
        temp_img = sprite_sheet.subsurface(x * self.size, y * self.size2, self.size, self.size2)
        temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size2 * self.image_scale)))
      animation_list.append(temp_img_list)
    return animation_list


  def move(self, screen_width, screen_height, surface, target, round_over, target2 = False):
    if 7 in self.amulet:
      self.health += 0.015
    if self.yin_and_yang:
      self.health += 0.4
      target.health -= 0.4
      if target2 != False:
        target2.health -= 0.5
    if self.player != 5 and self.player != 6:
      SPEED = self.speed1
      SPEED_BOT = 5
      GRAVITY = self.speed2
      if self.player == 9:
        GRAVITY = 1.35
    else:
      SPEED = 10.5
      SPEED_BOT = 5.5
      GRAVITY = 1.25
    
    dx = 0
    dy = 0
    self.running = False
    #if self.attack_type != 0:
    #    self.attack_type = 0
    
    key = pygame.key.get_pressed()

    if self.attacking == False and self.alive == True and round_over == False:
      if self.player == 1: #бот
        attacking_rect = pygame.Rect(self.rect.centerx - (2.5 * self.rect.width), self.rect.y, 5 * self.rect.width, self.rect.height)
        rect_player = pygame.Rect(self.rect.x - (0.8 * self.rect.width), self.rect.y, 2.5 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and not rect_player.colliderect(target.rect):
          self.attack_type = 2
          self.attack(target)
        elif rect_player.colliderect(target.rect):
          self.attack_type = 1
          self.attack(target)
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.cooldown_run = randint(500,1000)
          if self.rect.centerx >= 100 and self.rect.centerx <= 900:
            if self.health <= 50:
                self.random = 2
            if self.health > 0:
                self.run = randint(0,self.random)
          else:
            self.run = 0
        if self.run != self.random:
          if target.rect.centery <= self.rect.y and self.jump == False:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -30
              self.jump = True
          if target.rect.centerx <= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx > self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True
        else:
          if self.jump == False:
            attacking_rect = pygame.Rect(self.rect.centerx - (2.5 * self.rect.width), self.rect.y, 5 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
              self.vel_y = -30
              self.jump = True
          if target.rect.centerx >= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx < self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True

      if self.choice == 1:
        if key[pygame.K_a]:
          dx = -SPEED
          self.flip = True
          self.running = True
        if key[pygame.K_d]:
          dx = SPEED
          self.flip = False
          self.running = True
        if key[pygame.K_w] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        if key[pygame.K_n] or key[pygame.K_m]:
          if key[pygame.K_n]:
            self.attack_type = 1
          if key[pygame.K_m]:
            self.attack_type = 2
          if self.player == 2:
              self.attack(target)

      if self.player == 3: #бот
        attacking_rect = pygame.Rect(self.rect.centerx - (3.5 * self.rect.width), self.rect.y, 2 * self.rect.width, self.rect.height)
        attacking_rect2 = pygame.Rect(self.rect.centerx + self.rect.width, self.rect.y, 2 * self.rect.width, self.rect.height)
        rect_player = pygame.Rect(self.rect.x - (0.8 * self.rect.width), self.rect.y, 2.5 * self.rect.width, 1.5 * self.rect.height)
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.cooldown_run = randint(500,1500)
          if self.health <= 50:
              self.random = 2
          if self.health > 0:
              self.run = randint(0,self.random)
        if target2 != False:
          if (attacking_rect.colliderect(target2.rect) or attacking_rect2.colliderect(target2.rect)) and not rect_player.colliderect(target2.rect):
            if self.run <= 2:
              if target2.rect.centery <= self.rect.y:
                self.attack_type = 1
              else:
                self.attack_type = 2
            else:
              if target2.rect.centery <= self.rect.y:
                self.attack_type = 2
              else:
                self.attack_type = 1
            if target2.rect.centerx > self.rect.centerx:
              self.flip = False
            else:
              self.flip = True
            if (self.attack_cooldown1 == 0 and self.attack_type == 1) or (self.attack_cooldown2 == 0 and self.attack_type == 2):
              self.cooldown_test = 1
              self.attacking = True
              self.attack_sound.play()
          elif rect_player.colliderect(target2.rect):
            if self.rect.centerx >= 50 and self.rect.centerx <= 750:
              if target2.rect.centerx >= self.rect.centerx:
                dx = -SPEED_BOT - 2
                self.flip = True
                self.running = True
              elif target2.rect.centerx < self.rect.centerx:
                dx = SPEED_BOT + 2
                self.flip = False
                self.running = True
            else:
              if target2.rect.centerx + 50 <= self.rect.centerx:
                dx = -SPEED_BOT - 110
                self.flip = True
                self.running = True
              elif target2.rect.centerx - 50 > self.rect.centerx:
                dx = SPEED_BOT + 110
                self.flip = False
                self.running = True
        if (attacking_rect.colliderect(target.rect) or attacking_rect2.colliderect(target.rect)) and not rect_player.colliderect(target.rect):
          if self.run <= 2:
            if target.rect.centery <= self.rect.y:
              self.attack_type = 1
            else:
              self.attack_type = 2
          else:
            if target.rect.centery <= self.rect.y:
              self.attack_type = 2
            else:
              self.attack_type = 1
          if target.rect.centerx > self.rect.centerx:
            self.flip = False
          else:
            self.flip = True
          if (self.attack_cooldown1 == 0 and self.attack_type == 1) or (self.attack_cooldown2 == 0 and self.attack_type == 2):
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
        elif rect_player.colliderect(target.rect):
          if target.rect.centery >= self.rect.y and self.jump == False and self.run <= 1:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -30
              self.jump = True
          if self.rect.centerx >= 50 and self.rect.centerx <= 750:
            if target.rect.centerx >= self.rect.centerx:
              dx = -SPEED_BOT - 2
              self.flip = True
              self.running = True
            elif target.rect.centerx < self.rect.centerx:
              dx = SPEED_BOT + 2
              self.flip = False
              self.running = True
          else:
            if target.rect.centerx + 50 <= self.rect.centerx:
              dx = -SPEED_BOT - 110
              self.flip = True
              self.running = True
            elif target.rect.centerx - 50 > self.rect.centerx:
              dx = SPEED_BOT + 110
              self.flip = False
              self.running = True
        else:
          if target.rect.y <= self.rect.centery and self.jump == False and self.run <= 1:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -30
              self.jump = True
          if target.rect.centerx < self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx >= self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True
        
      
      if self.choice == 2: #игрок 
        if self.rolling_over and 11 in self.amulet:
          if self.rect.colliderect(target.rect):
            target.health -= 0.75
          if target2 != False:
            if self.rect.colliderect(target2.rect):
              target2.health -= 0.75
        if not self.rolling_over:
          if key[pygame.K_LEFT]:
            dx = -SPEED
            self.flip = True
            self.running = True
          elif key[pygame.K_RIGHT]:
            dx = SPEED
            self.flip = False
            self.running = True
          if key[pygame.K_UP] and self.jump == False:
            if 2 in self.amulet:
              self.vel_y = -33
            else:
              self.vel_y = -30
            self.jump = True
          if key[pygame.K_d] and self.attack_cooldown1 == 0:
            self.attack_type = self.attack_hero[0]
          elif key[pygame.K_s] and self.attack_cooldown2 == 0:
            self.attack_type = self.attack_hero[1]
          elif key[pygame.K_w] and self.attack_cooldown3 == 0:
            self.attack_type = self.attack_hero[2]
          elif key[pygame.K_a] and self.attack_cooldown4 == 0:
            self.attack_type = self.attack_hero[3]
          elif key[pygame.K_e] and self.cooldown_rolling_over == -1:
            self.attack_type = self.attack_hero[4]
          if self.player == 2:
            if (self.attack_cooldown1 == 0 and self.attack_type == self.attack_hero[0]) or (self.attack_cooldown2 == 0 and self.attack_type == self.attack_hero[1]) or (self.attack_cooldown3 == 0 and self.attack_type == self.attack_hero[2]) or (self.attack_cooldown4 == 0 and self.attack_type == self.attack_hero[3]) or (self.attack_cooldown5 == 0 and self.attack_type == self.attack_hero[4]):
                self.cooldown_test = 1
                self.attacking = True
                self.attack_sound.play()
        if key[pygame.K_e] and self.cooldown_rolling_over == 0 and self.cooldown_rolling_over != -1:
          self.rolling_over = True
      if self.player == 5 or self.player == 55: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (2.75 * self.rect.width * self.flip), self.rect.y, 2.25 * self.rect.width, self.rect.height)
        attacking_rect2 = pygame.Rect(self.rect.centerx - (2.25 * self.rect.width * self.flip), self.rect.y - (self.rect.height // 1.75), 2.25 * self.rect.width, 1.5 * self.rect.height)
        if self.player == 5:
          if attacking_rect.colliderect(target.rect) and not attacking_rect2.colliderect(target.rect) and self.attack_cooldown1 == 0:
            self.attack_type = 1
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          elif attacking_rect2.colliderect(target.rect) and self.attack_cooldown2 == 0:
            self.attack_type = 2
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
        if self.player == 55:
          if self.rolling_over == False:
            if self.health >= self.health_max // 1.75:
              if attacking_rect.colliderect(target.rect) and not attacking_rect2.colliderect(target.rect) and self.attack_cooldown1 == 0:
                self.attack_type = 1
                self.cooldown_test = 1
                self.attacking = True
                self.attack_sound.play()
              elif attacking_rect2.colliderect(target.rect) and self.attack_cooldown2 == 0:
                self.attack_type = 2
                self.cooldown_test = 1
                self.attacking = True
                self.attack_sound.play()
            else:
              if attacking_rect.colliderect(target.rect) and not attacking_rect2.colliderect(target.rect) and self.attack_cooldown3 == 0:
                self.attack_type = 3
                self.cooldown_test = 1
                self.attacking = True
                self.attack_sound.play()
              elif attacking_rect.colliderect(target.rect) and self.attack_cooldown4 == 0:
                self.attack_type = 4
                self.cooldown_test = 1
                self.attacking = True
                self.attack_sound.play()
          if target.rolling_over and self.cooldown_rolling_over == 0:
            if self.rolling_over == False:
              if target.rect.centerx <= self.rect.centerx + 10:
                self.flip = True
              elif target.rect.centerx > self.rect.centerx - 10:
                self.flip = False
            self.rolling_over = True
        if self.rolling_over == False:
          now2 = pygame.time.get_ticks()
          if now2 - self.last2 >= self.cooldown_run:
            self.last2 = now2
            self.cooldown_run = 600
            if self.rect.centerx >= 100 and self.rect.centerx <= 600:
              if self.health <= 30:
                  self.random = 2
              if self.health > 0:
                  self.run = randint(0,self.random)
            else:
              self.run = 0
          if self.rect.colliderect(target.rect):
                self.run = 2
                self.cooldown_run = 400
          if self.run <= 1:
            if self.jump == False and self.random == 0:
              now3 = pygame.time.get_ticks()
              if now3 - self.last3 >= self.cooldown2:
                self.last3 = now3
                self.vel_y = -30
                self.jump = True
            if target.rect.centerx <= self.rect.centerx + 10:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx > self.rect.centerx - 10:
              dx = SPEED_BOT
              self.flip = False
              self.running = True
          else:
            if self.jump == False:
              self.vel_y = -30
              self.jump = True
            if target.rect.centerx >= self.rect.centerx + 10:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx < self.rect.centerx - 10:
              dx = SPEED_BOT
              self.flip = False
              self.running = True  

      if self.player == 7: #bot
        if self.rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
          self.attack_type = 1
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.cooldown_run = 1000
          if self.rect.centerx >= 100 and self.rect.centerx <= 550:
            if self.health <= 90:
                self.random = 10
            if self.health > 0:
                self.run = randint(0,self.random)
          else:
            self.run = 0
        if self.run <= 1:
          if self.jump == False and self.random == 0:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -30
              self.jump = True
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True
          else:
              dx = 0
              if target.rect.centerx <= self.rect.centerx:
                self.flip = False
              else:
                self.flip = True
        else:
          if self.jump == False:
            self.vel_y = -30
            self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True   
          else:
              dx = 0
              if target.rect.centerx <= self.rect.centerx:
                self.flip = False
              else:
                self.flip = True  
      if self.player == 9: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (4.25 * self.rect.width * self.flip), self.rect.y, 4.25 * self.rect.width, self.rect.height)
        attacking_rect2 = pygame.Rect(self.rect.centerx - (3.75 * self.rect.width * self.flip), self.rect.y - (self.rect.height // 1.75), 3.75 * self.rect.width, 1.5 * self.rect.height)
        #pygame.draw.rect(surface,(0,250,0),attacking_rect)
        if attacking_rect.colliderect(target.rect) and not attacking_rect2.colliderect(target.rect) and self.attack_cooldown1 == 0:
          self.attack_type = 1
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        elif attacking_rect2.colliderect(target.rect) and self.attack_cooldown2 == 0:
          self.attack_type = 2
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.cooldown_run = 500
          if self.rect.centerx >= 100 and self.rect.centerx <= 600:
            if self.health <= 60:
                self.random = 3
            if self.health > 0:
                self.run = randint(0,self.random)
          else:
            self.run = 0
        if self.rect.colliderect(target.rect):
              self.run = 2
              self.cooldown_run = 400
        if self.run <= 1:
          if self.jump == False and self.random == 0:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -35
              self.jump = True
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT * 1.25
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT * 1.25
            self.flip = False
            self.running = True
          else:
              dx = 0
              if target.rect.centerx <= self.rect.centerx:
                self.flip = False
              else:
                self.flip = True
        else:
          if self.jump == False:
            self.vel_y = -35
            self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT * 1.25
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT * 1.25
            self.flip = False
            self.running = True  
          else:
              dx = 0
              if target.rect.centerx <= self.rect.centerx:
                self.flip = False
              else:
                self.flip = True
      
      if self.player == 11 or self.player == 31: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (1.25 * self.rect.width * self.flip), self.rect.y, 1.25 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
          self.attack_type = 1
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and self.attack_cooldown1 == 0:
             self.attack_type = 1
             self.cooldown_test = 1
             self.attacking = True
             self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= 4000:
          self.last2 = now2  
          self.run = -self.run
          self.random = randint(0,7)
        if self.run == 1:
          if self.jump == False and self.random == 0:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -20
              self.jump = True
          dx = -SPEED_BOT
          self.flip = True
          self.running = True
        else:
          if self.jump == False and self.random == 0:
            self.vel_y = -20
            self.jump = True
          dx = SPEED_BOT 
          self.flip = False
          self.running = True

      if self.player == 13: #bot
        attacking_rect = pygame.Rect(self.rect.x - (self.rect.width * 0.25), self.rect.y, 1.5 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
          self.attack_type = 1
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        elif self.rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
          self.attack_type = 1
          dx = 0
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2 
          self.run = randint(0,2)
          self.cooldown_run = 650
          self.random = randint(0,5)
          if self.rect.colliderect(target.rect):
            self.run = 0
            self.cooldown_run = 450
            self.random = 2
        if self.run <= 1:
          if self.jump == False and self.random == 0:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -32
              self.jump = True
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True
        else:
          if self.jump == False:
            self.vel_y = -32
            self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True  

      if self.player == 15: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (3 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
        attacking_rect2 = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y + (self.rect.height // 5),2 * self.rect.width, self.rect.height // 2)
        #pygame.draw.rect(surface,(0,250,0),attacking_rect)
        if attacking_rect2.colliderect(target.rect) and not attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
          self.attack_type = 1
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        elif attacking_rect.colliderect(target.rect) and self.attack_cooldown2 == 0:
          self.attack_type = 2
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.cooldown_run = 700
          if self.rect.centerx >= 100 and self.rect.centerx <= 600:
            if self.health <= 55:
                self.random = 2
            if self.health > 0:
                self.run = randint(0,self.random)
          else:
            self.run = 0
        if self.rect.colliderect(target.rect):
              self.run = 2
              self.cooldown_run = 500
        if self.run <= 1:
          if self.jump == False and self.random == 0:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -25
              self.random += 1
              self.jump = True
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True
        else:
          if self.jump == False:
            self.vel_y = -25
            self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True  

      if self.player == 17: #bot
        attacking_rect = pygame.Rect(self.rect.x - self.rect.width, self.rect.y, 2.75 * self.rect.width, self.rect.height)
        if target.attack_type != 0 and self.cooldown_rolling_over == 0:
          self.rolling_over = True
          self.cooldown_test = 1
        if target2 != False and self.rolling_over == False:
          if target2.attack_type != 0 and self.cooldown_rolling_over == 0:
            self.rolling_over = True
            self.cooldown_test = 1
          if attacking_rect.colliderect(target2.rect) and self.attack_cooldown1 == 0:
            self.attack_type = 1
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
        if self.rolling_over == False:
          if attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
            self.attack_type = 1
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          elif self.rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
            self.attack_type = 1
            dx = 0
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          now2 = pygame.time.get_ticks()
          if now2 - self.last2 >= self.cooldown_run:
            self.last2 = now2
            self.random1 = randint(1,2)
            self.cooldown_run = 800
            if self.rect.centerx >= 100 and self.rect.centerx <= 600:
              if self.health > 0:
                  self.run = randint(0,self.random)
            else:
              self.run = 0
          if self.run <= 1:
            if self.jump == False and self.random == 0:
              now3 = pygame.time.get_ticks()
              if now3 - self.last3 >= self.cooldown2:
                self.last3 = now3
                self.vel_y = -25
                self.random += 0.5
                self.jump = True
            if target.rect.centerx + 10 <= self.rect.centerx:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 > self.rect.centerx:
              dx = SPEED_BOT
              self.flip = False
              self.running = True
          else:
            if self.jump == False:
              self.vel_y = -25
              self.jump = True
            if target.rect.centerx - 10 >= self.rect.centerx:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx + 10 < self.rect.centerx:
              dx = SPEED_BOT
              self.flip = False
              self.running = True  
      
      if self.player == 19: #bot
        attacking_rect = pygame.Rect(self.rect.x , self.rect.y, self.rect.width, self.rect.height)
        #pygame.draw.rect(surface,(0,250,0),attacking_rect)
        if attacking_rect.colliderect(target.rect) and self.attack_cooldown2 == 0 and self.attack_cooldown1 == 0:
          self.attack_type = randint(1,2)
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        elif self.action != 5:
          if not self.jump:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.random = randint(0,4)
              if self.random == 0:
                self.vel_y = -30
                self.jump = True
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True
        else:
          if not self.jump:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.random = randint(0,4)
              if self.random == 0:
                self.vel_y = -30
                self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True
      
      if self.player == 21: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (1.25 * self.rect.width * self.flip), self.rect.y, 1.25 * self.rect.width, self.rect.height)
        #pygame.draw.rect(surface,(0,200,0),attacking_rect)
        if attacking_rect.colliderect(target.rect):
          if self.health >= self.health_max // 1.75:
            if self.attack_cooldown1 == 0:
              self.attack_type = 1
              self.cooldown_test = 1
              self.attacking = True
              self.attack_sound.play()
          else:
            if self.attack_cooldown2 == 0:
              self.attack_type = 2
              self.cooldown_test = 1
              self.attacking = True
              self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.random1 = randint(-1,3)
          self.run = -self.run
          if self.run == -1:
              self.cooldown_run = randint(400,800)
          else:
              self.cooldown_run = randint(3000,3600)
        if (self.rect.centerx >= 60 and self.rect.centerx <= 640):
          if self.rect.colliderect(target.rect):
            self.run = 1
        else:
          self.run = -1
        if self.run == -1:
          if self.jump == False and self.random1 == 1:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -32
              self.jump = True
          if self.rect.colliderect(target.rect):
            dx = 0
            if target.rect.centerx <= self.rect.centerx:
              self.flip = True
            else:
              self.flip = False
          elif target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT * 1.2
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT * 1.2
            self.flip = False
            self.running = True
        else:
          if self.jump == False and self.random1 == -1:
            self.vel_y = -32
            self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True  

      if self.player == 23: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y, 0.5 * self.rect.width, self.rect.height)
        #pygame.draw.rect(surface,(0,200,0),attacking_rect)
        if attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
          dx = 0
          self.attack_type = 1
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        if self.health <= self.health_max - 30 and not attacking_rect.colliderect(target.rect) and self.attack_cooldown2 == 0:
          dx = 0
          self.attack_type = 2
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.random1 = randint(1,3)
          self.run = randint(1,4)
          self.cooldown_run = randint(700,1700)
        if self.rect.centerx <= 80 and self.rect.centerx >= 620:
          self.cooldown_run = 150

        if self.rect.centery >= 200 and self.rect.centery <= 600 and self.random1 == 1:
          dy = 4
        elif self.rect.centery >= 200 and self.rect.centery <= 600 and self.random1 == 2:
          dy = -4
        else:
          dy = 0

        if self.run == 1:
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True
          else:
            dx = 0
            if target.rect.centerx <= self.rect.centerx:
              self.flip = False
            else:
              self.flip = True
        elif self.run == 2:
          if target.rect.centerx > self.rect.centerx:
            self.flip = False
          else:
            self.flip = True
          dx = 0
        elif self.run == 3:
          if self.rect.centerx < 400 and self.rect.centerx >= 390:
            dx = 0
            if target.rect.centerx > self.rect.centerx:
              self.flip = False
            else:
              self.flip = True
          elif self.rect.centerx >= 400:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif self.rect.centerx < 390:
            dx = SPEED_BOT
            self.flip = False
            self.running = True 
        else:
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True  

      if self.player == 25 or self.player == 27 or self.player == 252: #bot
        attacking_rect = pygame.Rect(self.rect.x , self.rect.y, self.rect.width, self.rect.height)
        if self.player == 25:
            attacking_rect2 = pygame.Rect(self.rect.x - self.rect.width * 2, self.rect.y, self.rect.width * 5, self.rect.height)
        if self.player == 27:
            attacking_rect2 = pygame.Rect(self.rect.x - self.rect.width * 3, self.rect.y - self.rect.height, self.rect.width * 7, self.rect.height * 2)
        #pygame.draw.rect(surface,(0,200,0),attacking_rect2)
        if attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
          if self.player == 252:
            if target2.health > target2.health_max // 2:
              self.attack_type = 1
              self.cooldown_test = 1
              self.attacking = True
              self.attack_sound.play()
              self.heal = 1
          else:
            self.attack_type = 1
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
            self.heal = 1
        elif self.health <= self.health_max - 20 and not attacking_rect2.colliderect(target.rect) and self.attack_cooldown2 == 0:
          dx = 0
          self.attack_type = 2
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
          if self.player == 25:
              self.heal += 0.5
          if self.player == 27:
              self.heal += 1.3
        elif self.player == 252 and target2.health <= target2.health_max // 2:
          dx = 0
          self.attack_type = 2
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        else:
          if self.player == 27:
            if self.health <= self.health_max - self.health_max // 2:
                self.health += 0.025
            elif self.health < self.health_max:
                self.health += 0.015
            else:
              self.health = self.health_max
          now2 = pygame.time.get_ticks()
          if now2 - self.last2 >= self.cooldown_run:
            self.last2 = now2
            self.run = randint(1,3)
            if self.run == 1:
                self.cooldown_run = randint(700,1700)
          if self.hit and attacking_rect2.colliderect(target.rect):
            self.run = 2
          if self.run >= 2:
            if target.rect.centerx + 10 <= self.rect.centerx:
              dx = -SPEED_BOT 
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 > self.rect.centerx:
              dx = SPEED_BOT 
              self.flip = False
              self.running = True
            else:
              dx = 0
              if target.rect.centerx <= self.rect.centerx:
                self.flip = False
              else:
                self.flip = True
          
          else:
            if target.rect.centerx - 10 >= self.rect.centerx:
              dx = -SPEED_BOT 
              self.flip = True
              self.running = True
            elif target.rect.centerx + 10 < self.rect.centerx:
              dx = SPEED_BOT 
              self.flip = False
              self.running = True      
      
      if self.player == 29: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y - self.rect.height * 0.5, 2 * self.rect.width, self.rect.height * 1.5)
        attacking_rect2 = pygame.Rect(self.rect.centerx - (2 * self.rect.width), self.rect.y, 4 * self.rect.width, self.rect.height)
        if self.attack_cooldown1 == 0 and self.attack_cooldown2 == 0:
          if attacking_rect2.colliderect(target.rect) and self.random == 3 and self.attack_cooldown2 == 0:
            self.attack_type = 2
            self.random = -self.random
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          elif attacking_rect.colliderect(target.rect) and self.random == -3 and self.attack_cooldown1 == 0:
            self.attack_type = 1
            self.random = -self.random
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          if target.rect.centerx - 10 <= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 > self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True
        elif (self.attack_cooldown1 == 0 and self.attack_cooldown2 != 0) or (self.attack_cooldown1 != 0 and self.attack_cooldown2 == 0) or (self.rect.x <= 50 or self.rect.x >= 750):
          dx = 0
        else:
          if self.jump == False and target.rect.centery <= self.rect.y:
            self.vel_y = -30
            self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True  
      
      if self.player == 33: #bot
        attacking_rect2 = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y + self.rect.height // 3, self.rect.width, self.rect.height // 1.5)
        attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width), self.rect.y + self.rect.height // 2, 3 * self.rect.width, self.rect.height // 4)
        attacking_rect3 = pygame.Rect(self.rect.centerx - (1.25 * self.rect.width * self.flip), self.rect.y, 1.25 * self.rect.width, self.rect.height)
        attacking_rect4 = pygame.Rect(self.rect.centerx - (1.75 * self.rect.width * self.flip), self.rect.y, 1.75 * self.rect.width, self.rect.height)
        if self.health / self.health_max >= 0.75:
          if attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0:
            self.attack_type = 1
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
            #self.attack13(target)
          if self.attack_cooldown1 == 0:
            if target.rect.centerx + 10 <= self.rect.centerx:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 > self.rect.centerx:
              dx = SPEED_BOT
              self.flip = False
              self.running = True
          else:
            if target.rect.centerx + 10 >= self.rect.centerx:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 < self.rect.centerx:
              dx = SPEED_BOT
              self.flip = False
              self.running = True  
        elif self.health / self.health_max >= 0.5:
          if attacking_rect.colliderect(target.rect) and self.attack_cooldown2 == 0:
            self.attack_type = 2
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          if self.action != 5:
            if not self.jump:
              now3 = pygame.time.get_ticks()
              if now3 - self.last3 >= self.cooldown2:
                self.last3 = now3
                self.random = randint(0,4)
                if self.random == 0:
                  self.vel_y = -30
                  self.jump = True
            if target.rect.centerx + 10 <= self.rect.centerx:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 > self.rect.centerx:
              dx = SPEED_BOT 
              self.flip = False
              self.running = True
          else:
            if not self.jump:
              now3 = pygame.time.get_ticks()
              if now3 - self.last3 >= self.cooldown2:
                self.last3 = now3
                self.random = randint(0,4)
                if self.random == 0:
                  self.vel_y = -30
                  self.jump = True
            if target.rect.centerx + 10 >= self.rect.centerx:
              dx = -SPEED_BOT 
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 < self.rect.centerx:
              dx = SPEED_BOT 
              self.flip = False
              self.running = True
        elif self.health / self.health_max >= 0.25:
          if attacking_rect3.colliderect(target.rect) and self.attack_cooldown3 == 0:
            self.attack_type = 3
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          now3 = pygame.time.get_ticks()
          if now3 - self.last3 >= self.cooldown2:
            self.last3 = now3
            self.cooldown2 = 1800
            self.random = randint(0,4)
          if self.rect.x <= 100 or self.rect.x >= 640:
            self.random = 3
          if self.random >= 3:
            if target.rect.centerx + 10 <= self.rect.centerx:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 > self.rect.centerx:
              dx = SPEED_BOT
              self.flip = False
              self.running = True
          elif self.random == 2:
            if target.rect.centerx > self.rect.centerx:
              self.flip = False
            else:
              self.flip = True
            dx = 0
          else:
            if target.rect.centerx + 10 >= self.rect.centerx:
              dx = -SPEED_BOT
              self.flip = True
              self.running = True
            elif target.rect.centerx - 10 < self.rect.centerx:
              dx = SPEED_BOT
              self.flip = False
              self.running = True  
        elif self.health / self.health_max >= 0.01:
          if attacking_rect4.colliderect(target.rect) and self.attack_cooldown4 == 0:
            self.attack_type = 4
            self.cooldown_test = 1
            self.attacking = True
            self.attack_sound.play()
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT
            self.flip = False
            self.running = True
      
      if self.player == 35: #bot
        attacking_rect = pygame.Rect(self.rect.centerx - (2.25 * self.rect.width * self.flip), self.rect.y, 2.25 * self.rect.width, self.rect.height)
        attacking_rect2 = pygame.Rect(self.rect.centerx - (2.25 * self.rect.width * (not self.flip)), self.rect.y, 2.25 * self.rect.width, self.rect.height)
        #pygame.draw.rect(surface,(0,250,0),attacking_rect2)
        if attacking_rect.colliderect(target.rect) and self.attack_cooldown1 == 0 and self.run <= 1:
          self.attack_type = 1
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        elif attacking_rect2.colliderect(target.rect) and self.attack_cooldown2 == 0 and self.rect.colliderect(target.rect):
          self.attack_type = 2
          self.cooldown_test = 1
          self.attacking = True
          self.attack_sound.play()
        now2 = pygame.time.get_ticks()
        if now2 - self.last2 >= self.cooldown_run:
          self.last2 = now2
          self.cooldown_run = 1000
          if self.rect.centerx <= 100 and self.rect.centerx >= 700:
            if self.health >= 60:
                self.random = 3
                self.run = 3
          else:
            self.run = randint(0,4)
        if self.rect.colliderect(target.rect):
              dx = 0
        elif self.run <= 1:
          if self.jump == False and self.random == 0:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -35
              self.jump = True
          if target.rect.centerx + 10 <= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx - 10 > self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True
          else:
              dx = 0
              if target.rect.centerx <= self.rect.centerx:
                self.flip = False
              else:
                self.flip = True
        elif self.run == 3:
          if self.jump == False and self.random == 0:
            now3 = pygame.time.get_ticks()
            if now3 - self.last3 >= self.cooldown2:
              self.last3 = now3
              self.vel_y = -35
              self.jump = True
          if 360 <= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif 340 > self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True
        elif self.run == 2:
          dx = 0
          if target.rect.centerx <= self.rect.centerx:
            self.flip = False
          else:
            self.flip = True
        else:
          if self.jump == False:
            self.vel_y = -35
            self.jump = True
          if target.rect.centerx - 10 >= self.rect.centerx:
            dx = -SPEED_BOT 
            self.flip = True
            self.running = True
          elif target.rect.centerx + 10 < self.rect.centerx:
            dx = SPEED_BOT 
            self.flip = False
            self.running = True  
          else:
              dx = 0
              if target.rect.centerx <= self.rect.centerx:
                self.flip = False
              else:
                self.flip = True
    #гравитация
    if not 13 in self.amulet:
      if not self.rolling_over and self.player != 23 and self.attack_type != 9:
        self.vel_y += GRAVITY
        dy += self.vel_y
      if self.player == 23 and self.rect.y <= 50:
        self.vel_y += GRAVITY
        dy += self.vel_y
    else:
      if not self.rolling_over and self.player != 23 and self.attack_type == 0:
        self.vel_y += GRAVITY
        dy += self.vel_y

    if self.rect.left + dx < 0:
      dx = -self.rect.left
    if self.rect.right + dx > screen_width:
      dx = screen_width - self.rect.right
    if self.rect.bottom + dy > screen_height - 110:
      self.vel_y = 0
      self.jump = False
      dy = screen_height - 110 - self.rect.bottom

    #автоповорот персонажей
    #if target.rect.centerx > self.rect.centerx:
    #  self.flip = False
    #else:
    #  self.flip = True

    if self.attack_cooldown1 > 0:
      self.attack_cooldown1 -= 1
    if self.attack_cooldown2 > 0:
      self.attack_cooldown2 -= 1
    if self.attack_cooldown3 > 0:
      self.attack_cooldown3 -= 1
    if self.attack_cooldown4 > 0:
      self.attack_cooldown4 -= 1
    if self.attack_cooldown5 > 0:
      self.attack_cooldown5 -= 1
    if self.cooldown_rolling_over > 0:
      self.cooldown_rolling_over -= 1
    if self.rolling_over and self.player != 17:
      if self.rect.centerx > 10 and self.rect.centerx < 790:
        if self.flip:
            dx = -30
        if not self.flip:
            dx = 30
      else:
        dx = 0
    self.rect.x += dx
    self.rect.y += dy


  def update(self, target, target2, surface):
    if self.cooldown_test >= 1:
      now3 = pygame.time.get_ticks()
      if now3 - self.last3 >= self.speed_anim:
        self.last3 = now3
        self.cooldown_test += 1
        if self.cooldown_test == 3:
          if self.player == 2 or self.player == 1:
            self.attack(target,target2,surface)
          elif self.player == 3:
            self.attack2(target,target2)
          elif self.player == 5 or self.player == 55:
            self.attack3(target)
          elif self.player == 7:
            self.attack4(target,1,target2)
          elif self.player == 9:
            self.attack5(target)
          elif self.player == 11 or self.player == 31:
            self.attack6(target, target2)
          elif self.player == 13:
            self.attack7(target)
          elif self.player == 15:
            self.attack8(target)
          elif self.player == 17:
            self.attack9(target,target2)
          elif self.player == 19:
            self.attack4(target,2,target2)
          elif self.player == 21:
            self.attack10(target)
          elif self.player == 23:
            self.attack11(target)
          elif self.player == 25:
            self.attack4(target,3,target2)
          elif self.player == 252:
            self.attack4(target,5,target2)
          elif self.player == 27:
            self.attack4(target,4,target2)
          elif self.player == 29:
            self.attack12(target)
          elif self.player == 33:
            self.attack13(target)
          elif self.player == 35:
            self.attack14(target)
          self.cooldown_test = 0
          self.attack_type = 0
    if self.health <= 0:
      self.health = 0
      self.alive = False
      self.update_action(6)#6:death
    elif self.attacking == True:
      if self.player != 2:
        if self.attack_type == 1:
          self.update_action(3)# attack1
        elif self.attack_type == 2:
          self.update_action(4)# attack2
        elif self.attack_type == 3:
          self.update_action(7)# attack3
        elif self.attack_type == 4:
          self.update_action(8)# attack4
        elif self.attack_type == 6:
          self.update_action(10)# attack6
        elif self.attack_type == 7:
          self.update_action(11)# attack7
        elif self.attack_type == 8:
          self.update_action(12)# attack8
        elif self.attack_type == 9:
          self.update_action(13)# attack9
      else:
        if self.attack_type == 1:
          self.update_action(3)# attack1
        elif self.attack_type == 2:
          self.update_action(4)# attack2
        elif self.attack_type == 5:
          self.update_action(7)# attack3
        elif self.attack_type == 6:
          self.update_action(8)# attack4
        elif self.attack_type == 8:
          self.update_action(10)# attack6
        elif self.attack_type == 9:
          self.update_action(11)# attack7
        elif self.attack_type == 10:
          self.yin_and_yang = True
          self.update_action(12)# attack8
        elif self.attack_type == 11:
          self.update_action(13)# attack9
    elif self.hit == True:
      self.update_action(5)#5:hit
    elif self.rolling_over == True:
      self.update_action(9)
    elif self.jump == True:
      self.update_action(2)#2:jump
    elif self.running == True:
      self.update_action(1)#1:run
    else:
      self.update_action(0)#0:idle
    if self.player == 11:
      animation_cooldown = 40
    elif self.attacking:
      animation_cooldown = self.attack_anim
    elif self.hit and self.player == 19:
      animation_cooldown = 21
    elif self.rolling_over and self.player == 2:
      animation_cooldown = self.rolling_over_speed
    elif self.rolling_over and self.player != 2:
      animation_cooldown = 20
    else:
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
        if self.player != 2:
          if self.action == 3:
              self.attacking = False
              self.attack_cooldown1 = self.cooldown_1  
          if self.action == 4:
              self.attacking = False
              self.attack_cooldown2 = self.cooldown_2 
          if self.action == 7:
              self.attacking = False
              self.attack_cooldown3 = self.cooldown_3 
          if self.action == 8:
              self.attacking = False
              self.attack_cooldown4 = self.cooldown_4
        else:
          self.yin_and_yang = False
          if self.action == self.attack_hero[0] + 2 and self.action != 9:
            self.attacking = False
            self.attack_cooldown1 = self.cooldown_1
          elif self.action == self.attack_hero[1] + 2 and self.action != 9:
            self.attacking = False
            self.attack_cooldown2 = self.cooldown_2
          elif self.action == self.attack_hero[2] + 2 and self.action != 9:
            self.attacking = False
            self.attack_cooldown3 = self.cooldown_3
          elif self.action == self.attack_hero[3] + 2 and self.action != 9:
            self.attacking = False
            self.attack_cooldown4 = self.cooldown_4
          elif self.action == self.attack_hero[4] + 2 and self.action != 9:
            self.attacking = False
            self.attack_cooldown5 = self.cooldown_5
              
        #if self.action == 8:
        #    self.attacking = False
        #    self.attack_cooldown4 = self.cooldown_4
        if self.action == 5:
          self.hit = False
          self.cooldown_run = 100
          self.attacking = False
        if self.action == 9:
          self.rolling_over = False
          self.cooldown_rolling_over = self.cooldown
          self.attacking = False
  def attack(self, target, target2,surface):
    if self.rolling_over == False:
      if self.attack_type == 1:
        attacking_rect = pygame.Rect(self.rect.centerx - (2.5 * self.rect.width * self.flip), self.rect.y, 2.25 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage:
            target.health -= 1
          else:
            target.health -= self.damage - target.not_damage
          target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage:
               target2.health -= 1
            else:
               target2.health -= self.damage - target2.not_damage
            target2.hit = True
      elif self.attack_type == 2:
        if self.flip:
          self.dop = -1#0.65
        else:
          self.dop = 1
        attacking_rect = pygame.Rect(self.rect.centerx - (2.5 * self.rect.width), self.rect.y, 5 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage * 3:
            target.health -= 1
          else:
            target.health -= self.damage * 3 - target.not_damage
          target.rect.x -= self.rect.width * self.dop * self.repulsion
          target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage * 3:
               target2.health -= 1
            else:
               target2.health -= self.damage * 3 - target2.not_damage
            target2.rect.x -= self.rect.width * self.dop * self.repulsion
            target2.hit = True
      elif self.attack_type == 5:
        attacking_rect = pygame.Rect(self.rect.centerx - (3.25 * self.rect.width * self.flip), self.rect.y - self.rect.height, 3.25 * self.rect.width, self.rect.height * 2)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage * 5:
            target.health -= 1
          else:
            target.health -= self.damage * 5 - target.not_damage
          target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage * 5:
              target2.health -= 1
            else:
              target2.health -= self.damage * 5 - target2.not_damage
            target2.hit = True
      elif self.attack_type == 6:
        attacking_rect = pygame.Rect(self.rect.centerx - (2.5 * self.rect.width * self.flip), self.rect.y, 2.25 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
            if target.not_damage >= self.damage * 2:
              target.health -= 1
            else:
              target.health -= self.damage * 2 - target.not_damage
            if target.not_damage >= self.damage * 2:
                self.health += 1
            else:
                self.health += self.damage * 2 - target.not_damage
            target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage * 2:
              target2.health -= 1
            else:
              target2.health -= self.damage * 2 - target2.not_damage

            if target2.not_damage >= self.damage * 2:
                self.health += 1
            else:
                self.health += self.damage * 2 - target2.not_damage
            target2.hit = True
        if self.health >= self.health_max:
            self.health = self.health_max
      elif self.attack_type == 8:
        self.health += self.damage * 2
        if self.health > self.health_max:
          self.health = self.health_max
      elif self.attack_type == 9:
        if not self.flip:
          attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width), self.rect.y - self.rect.height * 1.5, self.rect.width, self.rect.height * 4)
          attacking_rect2 = pygame.Rect(self.rect.centerx - (self.rect.width * 2), self.rect.y - self.rect.height * 1.5, self.rect.width * 3, self.rect.height * 4)
          attacking_rect3 = pygame.Rect(self.rect.centerx - (self.rect.width * 3), self.rect.y - self.rect.height * 1.5, self.rect.width * 5, self.rect.height * 4)
        else:
          attacking_rect = pygame.Rect(self.rect.centerx , self.rect.y - self.rect.height * 1.5, self.rect.width, self.rect.height * 4)
          attacking_rect2 = pygame.Rect(self.rect.centerx - self.rect.width, self.rect.y - self.rect.height * 1.5, self.rect.width * 3, self.rect.height * 4)
          attacking_rect3 = pygame.Rect(self.rect.centerx - self.rect.width * 2, self.rect.y - self.rect.height * 1.5, self.rect.width * 5, self.rect.height * 4)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage * 4:
            target.health -= 1
          else:
            target.health -= self.damage * 4 - target.not_damage
        if attacking_rect2.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage * 3:
            target.health -= 1
          else:
            target.health -= self.damage * 3 - target.not_damage
          target.rect.y -= 100 * self.repulsion
        if attacking_rect3.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage:
            target.health -= 1
          else:
            target.health -= self.damage - target.not_damage
          if target.rect.x > self.rect.x:
            target.rect.x += 50 * self.repulsion
          else:
            target.rect.x -= 50 * self.repulsion
          target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage * 4:
               target2.health -= 1
            else:
               target2.health -= self.damage * 4 - target2.not_damage
            if attacking_rect2.colliderect(target2.rect) and target2.rolling_over == False:
              if target2.not_damage >= self.damage * 3:
                target2.health -= 1
              else:
                target2.health -= self.damage * 3 - target.not_damage
              target2.rect.y -= 100 * self.repulsion
            if attacking_rect3.colliderect(target2.rect) and target2.rolling_over == False:
              if target2.not_damage >= self.damage:
                target2.health -= 1
              else:
                target2.health -= self.damage - target2.not_damage
              if target2.rect.x > self.rect.x:
                target2.rect.x += 50 * self.repulsion
              else:
                target2.rect.x -= 50 * self.repulsion
              target2.hit = True
      elif self.attack_type == 10:
        attacking_rect = pygame.Rect(self.rect.x - self.rect.width * 2, self.rect.y, 5 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.rect.x > self.rect.x:
            target.rect.x += 150 * self.repulsion
          else:
            target.rect.x -= 150 * self.repulsion
          target.rect.y -= 150 * self.repulsion
          target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.rect.x > self.rect.x:
              target2.rect.x += 150 * self.repulsion
            else:
              target2.rect.x -= 150 * self.repulsion
            target2.rect.y -= 150 * self.repulsion
            target2.hit = True
      if self.attack_type == 11 and self.rect.y > 350:
        attacking_rect = pygame.Rect(self.rect.x - self.rect.width * 1.75, self.rect.y + self.rect.height // 2, 4.5 * self.rect.width, self.rect.height * 1.5)        
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage * 4:
            target.health -= 1
          else:
            target.health -= self.damage * 4 - target.not_damage
          target.hit = True
          self.rect.y -= 80 * self.repulsion
          if not self.flip:
            self.rect.x += 80 * self.repulsion
          else:
            self.rect.x -= 80 * self.repulsion
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage * 4:
               target2.health -= 1
            else:
               target2.health -= self.damage * 4 - target2.not_damage
            target2.hit = True
            if not attacking_rect.colliderect(target.rect):
              self.rect.y -= 80 * self.repulsion
              if not self.flip:
                self.rect.x += 80 * self.repulsion
              else:
                self.rect.x -= 80 * self.repulsion
            else:
              self.rect.y -= 30 * self.repulsion
              if not self.flip:
                self.rect.x += 30 * self.repulsion
              else:
                self.rect.x -= 30 * self.repulsion

      #self.attack_type = 0
  def attack2(self, target,target2):
    if self.attack_cooldown1 == 0 and self.attack_type == 2:
      if self.flip == False:
        self.dop = -0.35
      else:
        self.dop = 1
      attacking_rect = pygame.Rect(self.rect.centerx - (4 * self.rect.width * self.dop), self.rect.y, 2.5 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.rect.x -= self.rect.width * self.dop  * 3
        target.hit = True
      if target2 != False:
        if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
          if target2.not_damage >= self.damage:
             target2.health -= 1
          else:
             target2.health -= self.damage - target2.not_damage
          target2.rect.x -= self.rect.width * self.dop * 3
          target2.hit = True

      attacking_rect = pygame.Rect(self.rect.centerx - (4 * self.rect.width * self.dop), self.rect.y - self.rect.height, 2.5 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage #// 2
        target.rect.x -= self.rect.width * self.dop * 1.5
        target.hit = True
      if target2 != False:
        if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
          if target2.not_damage >= self.damage:
             target2.health -= 1
          else:
            target2.health -= self.damage - target2.not_damage #// 2
          target2.rect.x -= self.rect.width * self.dop * 1.5
          target2.hit = True
    elif self.attack_cooldown2 == 0 and self.attack_type == 1 and self.action != 3:
      if self.flip == False:
        self.dop = -0.35
      else:
        self.dop = 1
      attacking_rect = pygame.Rect(self.rect.centerx - (4 * self.rect.width * self.dop), self.rect.y - self.rect.height, 2.5 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.rect.y -= self.rect.width * 3.25
        target.hit = True
      if target2 != False:
        if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
          if target2.not_damage >= self.damage:
            target2.health -= 1
          else:
            target2.health -= self.damage - target2.not_damage
          target2.rect.y -= self.rect.width * 3.25
          target2.hit = True

      attacking_rect = pygame.Rect(self.rect.centerx - (4 * self.rect.width * self.dop), self.rect.y, 2.5 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage #// 2
        target.rect.y -= self.rect.width * 1.75
        target.hit = True
      if target2 != False:
        if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
          if target2.not_damage >= self.damage:
            target2.health -= 1
          else:
            target2.health -= self.damage - target2.not_damage #// 2
          target2.rect.y -= self.rect.width * 1.75
          target2.hit = True
  def attack3(self, target):
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      attacking_rect = pygame.Rect(self.rect.centerx - (2.75 * self.rect.width * self.flip), self.rect.y, 2.75 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown2 == 0 and self.attack_type == 2:
      attacking_rect = pygame.Rect(self.rect.centerx - (2.75 * self.rect.width * self.flip), self.rect.y - (self.rect.height // 2), 2.75 * self.rect.width, 1.5 * self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown3 == 0 and self.attack_type == 3:
      if self.flip:
          attacking_rect = pygame.Rect(self.rect.centerx - (2.75 * self.rect.width), self.rect.y, 3 * self.rect.width, self.rect.height)
      else:
          attacking_rect = pygame.Rect(self.rect.centerx + (0.25 * self.rect.width), self.rect.y, 3 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown4 == 0 and self.attack_type == 4:
      attacking_rect = pygame.Rect(self.rect.centerx - (2.75 * self.rect.width * self.flip), self.rect.y - (self.rect.height // 1.5), 2.75 * self.rect.width, 1.75 * self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
  def attack4(self, target, type, target2):
    if self.attack_cooldown1 == 0 and (self.attack_type == 1 or self.attack_type == 2):
      if type == 1:
        attacking_rect = pygame.Rect(self.rect.x , self.rect.y, self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage:
             target.health -= 1
          else:
             target.health -= self.damage - target.not_damage
          target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage:
              target2.health -= 1
            else:
              target2.health -= self.damage - target2.not_damage
            target2.hit = True
      elif type == 2:
        attacking_rect = pygame.Rect(self.rect.x , self.rect.y, self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if self.attack_type == 1:
            if target.not_damage >= self.damage * 2:
               target.health -= 1
            else:
               target.health -= self.damage * 2 - target.not_damage
            target.hit = True
          elif self.attack_type == 2:
            if target.not_damage >= self.damage:
               target.health -= 1
            else:
               target.health -= self.damage - target.not_damage
            target.hit = True
      elif type == 3 or type == 4:
        attacking_rect = pygame.Rect(self.rect.x , self.rect.y, self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if self.attack_type == 1:
            if target.not_damage >= self.damage:
              target.health -= 1
            else:
              target.health -= self.damage - target.not_damage
            if type == 3:
                target.rect.y -= 150
            if type == 4:
                target.rect.y -= 100
                target.rect.y -= 200
                target.rect.y -= 300
            target.hit = True
        if self.attack_type == 2:
          self.health += self.heal
          if self.health == self.health_max:
            self.health = self.health_max
      elif type == 5:
        attacking_rect = pygame.Rect(self.rect.x , self.rect.y, self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if self.attack_type == 1:
            target.rect.y -= 150
            if target.not_damage >= self.damage:
              target.health -= 1
            else:
              target.health -= self.damage - target.not_damage
            target.hit = True
        if self.attack_type == 2:
          target2.health += 0.4
  def attack5(self, target):
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      attacking_rect = pygame.Rect(self.rect.centerx - (4.25 * self.rect.width * self.flip), self.rect.y, 4.25 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown2 == 0 and self.attack_type == 2 and self.action != 3:
      attacking_rect = pygame.Rect(self.rect.centerx - (4 * self.rect.width * self.flip), self.rect.y - (self.rect.height // 2), 4 * self.rect.width, 1.5 * self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
  def attack6(self, target, target2):
    if self.attack_cooldown1 == 0 and (self.attack_type == 1 or self.attack_type == 2):
      attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y, self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
      if target2 != False:
        if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
          if target2.not_damage >= self.damage:
            target2.health -= 1
          else:
            target2.health -= self.damage - target2.not_damage
          target2.hit = True
  def attack7(self, target):
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      attacking_rect = pygame.Rect(self.rect.x - self.rect.width, self.rect.y - (self.rect.height * 0.75), 3 * self.rect.width, 1.75 * self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.rect.y -= 400
        target.hit = True
  def attack8(self, target):
    if self.attack_cooldown1 == 0 and (self.attack_type == 1 or self.attack_type == 2):
      attacking_rect = pygame.Rect(self.rect.centerx - (3 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
      attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width * self.flip), self.rect.y + (self.rect.height // 5),1.5 * self.rect.width, self.rect.height // 2)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage * 4:
            target.health -= 1
        else:
            target.health -= self.damage * 4 - target.not_damage
        target.hit = True
  def attack9(self, target,target2): 
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      if self.attack_type == 1:
        attacking_rect = pygame.Rect(self.rect.x - self.rect.width, self.rect.y, 3 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
          if target.not_damage >= self.damage:
            target.health -= 1
          else:
            target.health -= self.damage - target.not_damage
          target.hit = True
        if target2 != False:
          if attacking_rect.colliderect(target2.rect) and target2.rolling_over == False:
            if target2.not_damage >= self.damage:
              target2.health -= 1
            else:
              target2.health -= self.damage - target2.not_damage
            target2.hit = True
  def attack10(self, target):
    if self.attack_cooldown1 == 0 and (self.attack_type == 1 or self.attack_type == 2):
      attacking_rect = pygame.Rect(self.rect.centerx - (1.25 * self.rect.width * self.flip), self.rect.y, 1.25 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if self.attack_type == 1:
          if target.not_damage >= self.damage:
             target.health -= 1
          else:
            target.health -= self.damage - target.not_damage
        if self.attack_type == 2:
          if target.not_damage >= self.damage * 2:
            target.health -= 1
          else:
            target.health -= self.damage * 2 - target.not_damage
        target.hit = True
  def attack11(self, target):
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y, 0.5 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown2 == 0 and self.attack_type == 2:
      self.attacking = True
      self.attack_sound.play()
      self.health += self.damage * 2
  def attack12(self, target):
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y - self.rect.height * 0.5, 2 * self.rect.width, self.rect.height * 1.5)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown2 == 0 and self.attack_type == 2:
      attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width), self.rect.y, 4 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
  def attack13(self, target):
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width), self.rect.y + self.rect.height // 2, 4 * self.rect.width, self.rect.height // 4)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown2 == 0 and self.attack_type == 2:
      attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width * self.flip), self.rect.y + self.rect.height // 3, 1.5 * self.rect.width, self.rect.height // 1.5)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage * 1.5:
            target.health -= 1
        else:
            target.health -= self.damage * 1.5 - target.not_damage
        target.hit = True
    elif self.attack_cooldown3 == 0 and self.attack_type == 3:
      attacking_rect = pygame.Rect(self.rect.centerx - (1.75 * self.rect.width * self.flip), self.rect.y, 1.75 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage * 2:
            target.health -= 1
        else:
            target.health -= self.damage * 2 - target.not_damage
        target.hit = True
    elif self.attack_cooldown4 == 0 and self.attack_type == 4:
      attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)  
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage * 2.5:
            target.health -= 1
        else:
            target.health -= self.damage * 2.5 - target.not_damage
        target.hit = True
  def attack14(self, target):
    if self.attack_cooldown1 == 0 and self.attack_type == 1:
      attacking_rect = pygame.Rect(self.rect.centerx - (2.75 * self.rect.width * self.flip), self.rect.y, 2.75 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True
    elif self.attack_cooldown2 == 0 and self.attack_type == 2:
      attacking_rect = pygame.Rect(self.rect.centerx - (2.75 * self.rect.width * (not self.flip)), self.rect.y, 2.75 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect) and target.rolling_over == False:
        if target.not_damage >= self.damage:
            target.health -= 1
        else:
            target.health -= self.damage - target.not_damage
        target.hit = True

  def update_action(self, new_action):
    if new_action != self.action:
      self.action = new_action
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks()

  def draw(self, surface):
    img = pygame.transform.flip(self.image, self.flip, False)
    #pygame.draw.rect(surface,(0,200,0),self.rect)
    surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))