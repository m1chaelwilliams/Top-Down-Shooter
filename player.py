import pygame as py
from settings import *
from bullet import Bullet

import math

class Player(py.sprite.Sprite):
    def __init__(self, groups, inventory, obstacles, pos, input, bullet_group, enemy_group, img = py.Surface((TILESIZE, TILESIZE)), items = None):
        super().__init__(groups)
        self.image = img
        self.base_img = self.image
        self.rect = self.image.get_rect(topleft = pos)
        self.kInput = input
        self.bullet_group = bullet_group
        self.enemy_group = enemy_group
        self.obstacles = obstacles

        self.inventory = inventory

        # movement vars
        self.movement = py.math.Vector2()

        # bullet vars


        # weapon vars
        #self.weapon = Weapon([groups], (self.rect.centerx, self.rect.centery), self, py.transform.scale(py.image.load('weapon.png').convert_alpha(), (TILESIZE*2,TILESIZE*2)))
    def input(self):
        keys = py.key.get_pressed()

        if keys[py.K_a]:
            self.movement.x = -1
        elif keys[py.K_d]:
            self.movement.x = 1
        else:
            self.movement.x = 0

        if keys[py.K_w]:
            self.movement.y = -1
        elif keys[py.K_s]:
            self.movement.y = 1
        else:
            self.movement.y = 0
    def get_rect_pos(self):
        return self.rect

    def move(self):
        self.rect.x += self.movement.x * SPEED
        self.collisions('horizontal')
        self.rect.y += self.movement.y * SPEED
        self.collisions('vertical')
    def collisions(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.movement.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.movement.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.movement.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.movement.y < 0:
                        self.rect.top = sprite.rect.bottom
    def click(self):
        events = self.kInput.get_events()
        for e in events:
            if e.type == py.MOUSEBUTTONDOWN:
                return True
        return False

    def get_mouse_pos(self):
        return py.mouse.get_pos()

    def shoot(self):
        print('created!')
        Bullet([self.bullet_group], self.inventory, self.obstacles, (self.rect.centerx, self.rect.centery), self.get_distance(self.get_mouse_pos()), self.enemy_group, True)

    def get_distance(self, target):
        distance = py.math.Vector2()
        distance.x = target[0] - self.rect.x
        distance.y = target[1] - self.rect.y
        distance = distance.normalize()

        print(distance)
        return distance
    
    def draw_health(self):
        if self.inventory.get_health() > 0:
            health_rect = py.Rect(self.rect.x, self.rect.y-(TILESIZE//2), self.inventory.get_health()*(TILESIZE/3), 20)
            health_rect.left = self.rect.left
            py.draw.rect(py.display.get_surface(), (255,0,0), (health_rect.x, health_rect.y, TILESIZE, 20))
            py.draw.rect(py.display.get_surface(), (0,255,0), health_rect)
            

    def update(self):
        if self.click():
            self.shoot()
        self.input()
        self.move()
        self.draw_health()



