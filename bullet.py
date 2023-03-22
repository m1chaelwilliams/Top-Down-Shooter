import pygame as py
from settings import *

class Bullet(py.sprite.Sprite):
    def __init__(self, groups, inventory, obstacles, pos, movement, target, isPlayer, img = py.Surface((10,10))):
        super().__init__(groups)
        self.movement = movement
        self.target = target
        self.obstacles = obstacles
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 20
        self.isPlayer = isPlayer
        self.inventory = inventory

    def check_wall_collisions(self):
        for sprite in self.obstacles:
            if sprite.rect.colliderect(self.rect):
                self.kill()
    def update(self):
        self.check_wall_collisions()
        self.rect.x += self.movement[0] * self.speed
        self.rect.y += self.movement[1] * self.speed
        if self.isPlayer == False:
            if self.rect.colliderect(self.target.rect):
                self.kill()
                
                self.inventory.subtract_health(1)
                if self.inventory.get_health() < 1:
                    self.target.kill()
        else:
            for sprite in self.target:
                if sprite.rect.colliderect(self.rect):
                    sprite.health -= 1
                    if sprite.health < 1:
                        sprite.kill()
                    self.kill()