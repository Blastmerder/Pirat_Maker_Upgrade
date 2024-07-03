import sys
import pygame


class MainMenu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def event_loop(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self, dt):
        self.event_loop(dt)
