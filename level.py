import pygame as py
from settings import *
from tile import Tile
from player import Player
from enemy import Enemy

class level:
    def __init__(self, input, inventory):
        self.input = input
        self.display = py.display.get_surface()

        self.visible_sprites = py.sprite.Group()
        self.obstacles = py.sprite.Group()
        self.bullet_group = py.sprite.Group()
        self.enemy_group = py.sprite.Group()

        self.inventory = inventory

        self.world_list = [WORLD, WORLD2]
        self.world_index = 0

        self.create_map(self.world_list[self.world_index])
    def create_map(self, map):
        for i, row in enumerate(map):
            for j, column in enumerate(row):
                    if column == 2:
                        x = j*TILESIZE
                        y = i*TILESIZE
                        self.player = Player([self.visible_sprites], self.inventory, self.obstacles, (x,y), self.input, self.bullet_group, self.enemy_group)
                        
        for i, row in enumerate(map):
            for j, column in enumerate(row):
                if column != 0:
                    x = j*TILESIZE
                    y = i*TILESIZE
                    if column == 1:
                        Tile([self.visible_sprites, self.obstacles], (x,y))

                    if column == 3:
                        self.enemy = Enemy([self.visible_sprites, self.enemy_group], self.inventory, self.obstacles, (x,y), self.player, self.bullet_group)
    def clear_sprites(self):
        if self.visible_sprites:
            for sprite in self.visible_sprites:
                sprite.kill()
        if self.obstacles:
            for sprite in self.obstacles:
                sprite.kill()
        if self.bullet_group:
            for sprite in self.bullet_group:
                sprite.kill()

    def draw(self):
        self.bullet_group.draw(self.display)
        self.visible_sprites.draw(self.display)
    def update(self):
        self.bullet_group.update()
        self.visible_sprites.update()
        if not self.enemy_group:
            if self.world_index < len(self.world_list)-1:
                self.world_index += 1
            self.clear_sprites()
            self.inventory.health = 3
            self.create_map(self.world_list[self.world_index])

    def run(self):
        self.display.fill(py.Color('#FFFDD0'))
        self.draw()
        self.update()