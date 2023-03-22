import pygame as py
from settings import *
from bullet import Bullet
from inventory import Inventory

class Enemy(py.sprite.Sprite):
    def __init__(self, groups, inventory, obstacles, pos, player, bullet_group, img=py.Surface((TILESIZE, TILESIZE))):
        self.groups = groups
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)
        self.radius = py.transform.scale(self.image, (TILESIZE*5, TILESIZE*5))
        self.inventory = inventory

        # target variables
        self.player = player
        self.target_rect = None
        self.bullet_group = bullet_group
        self.obstacles = obstacles
        self.health = 3


        self.image.fill('red')

        # movement variables
        self.movement = py.math.Vector2()
        self.speed = 3

        # timer variable

        self.shoot_interval = 20
        self.timer = 0
        self.moving = True

    def check_relative_pos(self, target):
        position_offset = {'up': False, 'down': False, 'left':False, 'right':False}

        if self.rect.x > target.x:
            position_offset['left'] = True
        if self.rect.x < target.x:
            position_offset['right'] = True
        if self.rect.y > target.y:
            position_offset['up'] = True
        if self.rect.y < target.y:
            position_offset['down'] = True

        return position_offset

    def move_towards(self, target):
        position_offset = self.check_relative_pos(target)
        if position_offset['up']:
            self.movement.y = -1
        elif position_offset['down']:
            self.movement.y = 1
        else:
            self.movement.y = 0

        if position_offset['left']:
            self.movement.x = -1
        elif position_offset['right']:
            self.movement.x = 1
        else:
            self.movement.x = 0

        if self.moving:
            self.rect.x += self.movement.x
            self.rect.y += self.movement.y


    def shoot(self):
        Bullet([self.bullet_group], self.inventory, self.obstacles, (self.rect.centerx, self.rect.centery), self.get_distance(self.player), self.player, False)

    def get_distance(self, target):
        distance = py.math.Vector2()
        distance.x = target.rect.x - self.rect.x
        distance.y = target.rect.y - self.rect.y
        if distance.magnitude() != 0:
            distance = distance.normalize()

        print(distance)
        return distance
    
    def check_wall(self, target):
        
        for sprite in self.obstacles:
            if sprite.rect.clipline((self.rect.centerx, self.rect.centery), (target.rect.centerx, target.rect.centery)):
                return False
        return True
    
    def draw_health(self):
        if self.inventory.get_health() > 0:
            health_rect = py.Rect(self.rect.x, self.rect.y-(TILESIZE//2), self.health*(TILESIZE/3), 20)
            health_rect.left = self.rect.left
            py.draw.rect(py.display.get_surface(), (255,0,0), (health_rect.x, health_rect.y, TILESIZE, 20))
            py.draw.rect(py.display.get_surface(), (0,255,0), health_rect)
            

    def update(self):

        self.check_wall(self.player)
        self.target_rect = self.player.get_rect_pos()
        if self.check_wall(self.player):
            self.move_towards(self.target_rect)

        self.timer += 1
        if self.timer > self.shoot_interval:
            if self.timer == self.shoot_interval+1:
                if self.check_wall(self.player):
                    self.shoot()
            self.moving = False
        if self.timer > self.shoot_interval * 4:
            self.timer = 0
            self.moving = True

        self.draw_health()
