import pygame

from settings import *

class Game:
    def __init__(self):

        # general setup
        self.surface= pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        # put one surface on another surface
        self.display_surface.blit(self.surface, (PADDING,PADDING))