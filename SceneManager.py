import pygame as py
from settings import *
from sampleLevel import SampleLevel

# runs current scene as long as exit condition is false

class SceneManager:
    def __init__(self):
        self.scenes = {'sampleScene':SampleLevel(self)}
        self.scene = None
    def set_scene(self, key):
        self.scene = self.scenes[key]
    def get_scene(self):
        return self.scene
    def run(self):
        if self.scene:
            self.scene.run()