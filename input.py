import pygame as py
import sys

class Input:
    def __init__(self):
        self.events = None
    def get_events(self):
        return self.events
    def check_quit(self):
        if self.events:
            for e in self.events:
                if e.type == py.QUIT:
                    py.quit()
                    sys.exit()
    def run(self):
        self.events = py.event.get()

