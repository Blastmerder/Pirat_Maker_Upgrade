import pygame
from settings import *

from pygame.math import Vector2 as vector
from pygame.image import load

from pygame.mouse import get_pressed as mouse_button
from pygame.mouse import get_pos as mouse_pos



class SettingMenu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # self.create_data()
        # self.create_button()

        self.display_settings = False

        # import textures

        self.button_settings = load('../graphics/settings_gui/settings.png').convert_alpha()
        self.button_settings = pygame.transform.scale2x(self.button_settings)
        self.button_settings_rect = self.button_settings.get_rect(center=(32, 32))

        self.bg = load('../graphics/settings_gui/bg.png').convert_alpha()
        self.bg_rect = self.bg.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

        self.music_button = load('../graphics/settings_gui/volume_music.png').convert_alpha()
        self.music_button = pygame.transform.scale2x(self.music_button)
        self.music_button_rect = self.music_button.get_rect(topleft=self.bg_rect.topleft+vector(64, 0))

        # rect all menu
        self.rect = pygame.Rect((0, 0), (64, 64))

        # all sounds for changing
        self.sounds_bg = []
        self.sounds_effect = []

        self.music_on = True

    """
    def create_data(self):
        self.menu_surfs = {}
        for key, value in EDITOR_DATA.items():
            if value['settings']:
                if not value['settings'] in self.menu_surfs:
                    self.menu_surfs[value['settings']] = [(key, pygame.transform.scale2x(load(value['menu_surf'])))]
                else:
                    self.menu_surfs[value['settings']].append((key, pygame.transform.scale2x(load(value['menu_surf']))))


     def create_button(self):

        # menu area general
        size = 64
        topleft = (WINDOW_WIDTH-size, WINDOW_HEIGHT-size)
        self.rect = pygame.Rect(topleft, (size, size))

        # button areas
        generic_button_rect = pygame.Rect(self.rect.topleft, (self.rect.width / 4, self.rect.height / 4))
        button_margin = 5
        self.interect_obj_button_rect = generic_button_rect.copy().move(self.rect.height/2, self.rect.width / 4).inflate(-button_margin,
                                                                                                                           -button_margin)
        # create the buttons
        self.buttons = pygame.sprite.Group()
        Button(self.interect_obj_button_rect, self.buttons, self.menu_surfs['checkpoint'], self.menu_surfs['checkpoint'])

    def highlight_indicator(self, index):
        if EDITOR_DATA[index]['menu'] == 'checkpoint':
            pygame.draw.rect(self.display_surface, BUTTON_LINE_COLOR, self.interect_obj_button_rect.inflate(4, 4), 5, 4)"""


    def set_sounds(self, sounds_bg: list, sounds_effect: list):
        self.sounds_bg = sounds_bg
        self.sounds_effect = sounds_effect
        self.sounds_bg_volumes = []
        self.sounds_effect_volumes = []

        for bg in self.sounds_bg:
            self.sounds_bg_volumes.append(bg.get_volume())
        for effect in self.sounds_effect:
            self.sounds_effect_volumes.append(effect.get_volume())

    def click(self, mouse_pos, mouse_button):
        if self.button_settings_rect.collidepoint(mouse_pos) and mouse_button[0]:
            self.display_settings = True
        #elif self.button_volume_rect.collidepoint(mouse_pos) and mouse_button[0]:
        #    ...
        if self.music_button_rect.collidepoint(mouse_pos) and mouse_button[0]:
            if self.music_on:
                for music in self.sounds_bg:
                    music.set_volume(0)
                self.music_on = False
            else:
                for i in range(len(self.sounds_bg)):
                    self.sounds_bg[i].set_volume(self.sounds_bg_volumes[i])
                self.music_on = True

        elif mouse_button[0] and not self.rect.collidepoint(mouse_pos):
            self.display_settings = False


    def display(self):
        # self.buttons.update()
        # self.buttons.draw(self.display_surface)

        self.display_surface.blit(self.button_settings, self.button_settings_rect)

        if self.display_settings:
            self.display_surface.blit(self.bg, self.bg_rect)
            self.display_surface.blit(self.music_button, self.music_button_rect)
            self.rect = self.bg_rect


        else:
            self.rect = self.button_settings_rect

    def update(self, dt):
        self.display()


class Button(pygame.sprite.Sprite):
    def __init__(self, rect, group, items, items_alt=None):
        super().__init__(group)
        self.image = pygame.Surface(rect.size)
        self.rect = rect

        self.items = {'main': items, 'alt': items_alt}
        self.index = 0
        self.main_active = True

    def get_id(self):
        return self.items['main' if self.main_active else 'alt'][self.index][0]

    def switch(self):
        self.index += 1
        self.index = 0 if self.index >= len(self.items['main' if self.main_active else 'alt']) else self.index

    def update(self):
        self.image.fill(BUTTON_BG_COLOR)
        surf = self.items['main' if self.main_active else 'alt'][self.index][1]
        rect = surf.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
        self.image.blit(surf, rect)