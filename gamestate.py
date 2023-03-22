import pygame as py

class Gamestate:
    def __init__(self):
        self.currentState = None
    def set_state(self, newState):
        self.currentState = newState
    def get_state(self):
        return self.currentState
    def run(self):
        self.currentState.run()