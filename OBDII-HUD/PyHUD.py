from obd2 import OBD2

import pygame
from pygame.locals import *
from pygame.color import THECOLORS

if not pygame.font: print "No fonts!"
if not pygame.mixer: print "No mixer!"

from math import pi

def toRad(x):
    return pi * x / 180

class PyHUD(object):
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        red = THECOLORS['red']
        white = THECOLORS['white']
        self.screen.fill(white)
        pygame.draw.circle(self.screen, red, [100, 100], 50)
        pygame.draw.circle(self.screen, white, [100, 100], 48)
        pygame.draw.circle(self.screen, red, [250, 100], 50)
        pygame.draw.circle(self.screen, white, [250, 100], 48)
        pygame.draw.arc(self.screen, red, [50, 200, 250, 100], toRad(180), toRad(360))
        pygame.draw.arc(self.screen, red, [50, 202, 250, 100], toRad(178), toRad(362))

        pygame.display.flip()
    def MainLoop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

if __name__ == '__main__':
    app = PyHUD()
    app.MainLoop()
