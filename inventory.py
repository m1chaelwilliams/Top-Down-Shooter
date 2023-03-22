import pygame as py
from settings import *

class Inventory:
    def __init__(self, health, items):
        self.health = health
        self.items = items
    def subtract_health(self, amount):
        self.health -= 1
        if self.health < 1:
            self.health = 0
        print(self.health)
    def get_health(self):
        return self.health
    