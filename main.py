import pygame as py
from settings import *
from input import Input
from gamestate import Gamestate
from SceneManager import SceneManager
from level import level
from inventory import Inventory

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = py.time.Clock()

        self.events = None

        
        self.input = Input()
        self.level = level(self.input, Inventory(3, {}))


    def update_display(self):
        py.display.update()
        self.clock.tick(FPS)

    def run(self):
        while True:
            self.input.check_quit()
            self.input.run()
            self.level.run()
            self.update_display()

if __name__ == '__main__':
    game = Game()
    game.run()

