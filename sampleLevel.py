import pygame as py
from settings import *
from level import level


class SampleLevel(level):
    def __init__(self, sceneManager):
        super().__init__()
        self.sceneManager = sceneManager
        self.input = input()
    def check_exit_condition(self):
        pass
    def run(self):
        
        super().run()