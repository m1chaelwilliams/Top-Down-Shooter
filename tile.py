import pygame as py
from settings import *

class Tile(py.sprite.Sprite):
    def __init__(self, groups, pos, img = py.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)