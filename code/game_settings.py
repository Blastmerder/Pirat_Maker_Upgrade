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

        self.group_settings = pygame.sprite.Group()

        # import textures

        self.button_settings = load('../graphics/settings_gui/settings.png').convert_alpha()
        self.button_settings = pygame.transform.scale2x(self.button_settings)
        self.button_settings_rect = self.button_settings.get_rect(center=(32, 32))

        self.bg = load('../graphics/settings_gui/bg.png').convert_alpha()
        self.bg_rect = self.bg.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

        # change volume music
        limit_changer_music_surf = pygame.surface.Surface((500, 25))
        self.limit_walker_music = Element(
            surf=limit_changer_music_surf,
            pos=self.bg_rect.topleft+vector(450, 57),
            group=self.group_settings
        )

        limit_changer_sounds_surf = pygame.surface.Surface((500, 25))
        self.limit_walker_sounds = Element(
            surf=limit_changer_sounds_surf,
            pos=self.bg_rect.topleft+vector(450, 157),
            group=self.group_settings
        )

        self.music_button_surf_on = pygame.transform.scale(load('../graphics/settings_gui/volume_music.png').convert_alpha(), (68, 60))
        self.music_button_surf_off = pygame.transform.scale(load('../graphics/settings_gui/volume_music_off.png').convert_alpha(), (68, 60))
        self.music_button = Element(
            surf=self.music_button_surf_on,
            pos=self.bg_rect.topleft+vector(130, 55),
            group=self.group_settings
        )

        # changer volume sound effects
        self.sounds_button_surf_on = pygame.transform.scale(
            load('../graphics/settings_gui/volume_sounds.png').convert_alpha(), (88, 60))
        self.sounds_button_surf_off = pygame.transform.scale(
            load('../graphics/settings_gui/volume_sounds_off.png').convert_alpha(), (88, 60))
        self.sounds_button = Element(
            surf=self.sounds_button_surf_on,
            pos=self.bg_rect.topleft + vector(130, 150),
            group=self.group_settings
        )

        changer_surf = pygame.surface.Surface((20, 50))
        self.walker_music = Element(
            surf=changer_surf,
            pos=self.bg_rect.topleft+vector(500, 57),
            group=self.group_settings
        )
        self.walker_music.image.fill('gray')

        walker_surf = pygame.surface.Surface((20, 50))
        self.walker_sound = Element(
            surf=walker_surf,
            pos=self.bg_rect.topleft+vector(500, 157),
            group=self.group_settings
        )
        self.walker_sound.image.fill('gray')

        # rect all menu
        self.rect = pygame.Rect((0, 0), (64, 64))

        # all sounds for changing
        self.sounds_bg = []
        self.sounds_effect = []

        self.hold_music = False
        self.hold_sound = False

        self.music_on = True
        self.sounds_on = True

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

        self.sounds_bg_volume = 0.4
        self.sounds_effect_volume = 0.4

    def click(self):
        if mouse_button()[0]:
            if self.button_settings_rect.collidepoint(mouse_pos()):
                self.display_settings = True

            if self.music_button.rect.collidepoint(mouse_pos()):
                for sound in self.sounds_bg:
                    sound.set_volume(self.sounds_bg_volume) if not self.music_on else sound.set_volume(0)
                self.music_on = not self.music_on
                self.music_button.image = self.music_button_surf_on if self.music_on else self.music_button_surf_off

            if self.sounds_button.rect.collidepoint(mouse_pos()):
                for sound in self.sounds_effect:
                    sound.set_volume(self.sounds_effect_volume) if not self.sounds_on else sound.set_volume(0)
                self.sounds_on = not self.sounds_on
                self.sounds_button.image = self.sounds_button_surf_on if self.sounds_on else self.sounds_button_surf_off


            if not self.rect.collidepoint(mouse_pos()):
                self.display_settings = False


    def change_walker_music(self):
        if mouse_button()[0] and self.display_settings and not self.hold_sound:
            if self.walker_music.rect.collidepoint(mouse_pos()) or self.hold_music:
                self.walker_music.rect.centerx = mouse_pos()[0]
                self.hold_music = True
        else:
            self.hold_music = False

        self.walker_music.rect.centerx = self.limit_walker_music.rect.x if self.walker_music.rect.centerx < self.limit_walker_music.rect.x else self.walker_music.rect.centerx
        self.walker_music.rect.centerx = self.limit_walker_music.rect.right if self.walker_music.rect.centerx > self.limit_walker_music.rect.right else self.walker_music.rect.centerx

        if int((self.walker_music.rect.x - self.limit_walker_music.rect.x) / 49 * 10) != self.sounds_bg_volume/100 and self.music_on:
            self.sounds_bg_volume = int((self.walker_music.rect.x - self.limit_walker_music.rect.x) / 49 * 10) / 100
            for sound in self.sounds_bg:
                sound.set_volume(self.sounds_bg_volume)


    def change_walker_sounds(self):
        if mouse_button()[0] and self.display_settings and not self.hold_music:
            if self.walker_sound.rect.collidepoint(mouse_pos()) or self.hold_sound:
                self.walker_sound.rect.centerx = mouse_pos()[0]
                self.hold_sound = True
        else:
            self.hold_sound = False

        self.walker_sound.rect.centerx = self.limit_walker_sounds.rect.x if self.walker_sound.rect.centerx < self.limit_walker_sounds.rect.x else self.walker_sound.rect.centerx
        self.walker_sound.rect.centerx = self.limit_walker_sounds.rect.right if self.walker_sound.rect.centerx > self.limit_walker_sounds.rect.right else self.walker_sound.rect.centerx

        if int((self.walker_sound.rect.x - self.limit_walker_sounds.rect.x) / 49 * 10) != self.sounds_effect_volume/100 and self.sounds_on:
            self.sounds_effect_volume = int((self.walker_sound.rect.x - self.limit_walker_sounds.rect.x) / 49 * 10) / 100
            for sound in self.sounds_effect:
                sound.set_volume(self.sounds_effect_volume)


    def draw_volume(self, rect_walker, rect_limit):
        line_rect = pygame.Rect(rect_limit.rect.topleft, (rect_walker.rect.x - rect_limit.rect.x, 25))
        line_rect2 = pygame.Rect(rect_limit.rect.bottomleft-vector(0, 5), (rect_walker.rect.x - rect_limit.rect.x, 5))
        line_rect3 = pygame.Rect(rect_limit.rect.topleft+vector(5, 0), (rect_walker.rect.x - rect_limit.rect.x - 5, 5))
        line_rect4 = pygame.Rect(rect_limit.rect.bottomleft-vector(0, 15), (5, 15))

        pygame.draw.rect(self.display_surface, '#FF0000', line_rect)
        pygame.draw.rect(self.display_surface, '#AD0000', line_rect2)
        pygame.draw.rect(self.display_surface, '#E46D6D', line_rect3)
        pygame.draw.rect(self.display_surface, '#AD0000', line_rect4)


    def display(self):
        # self.buttons.update()
        # self.buttons.draw(self.display_surface)

        self.display_surface.blit(self.button_settings, self.button_settings_rect)

        if self.display_settings:
            self.display_surface.blit(self.bg, self.bg_rect)
            self.group_settings.draw(self.display_surface)
            self.draw_volume(self.walker_music, self.limit_walker_music)
            self.draw_volume(self.walker_sound, self.limit_walker_sounds)
            self.display_surface.blit(self.walker_music.image, self.walker_music.rect)
            self.display_surface.blit(self.walker_sound.image, self.walker_sound.rect)

            self.rect = self.bg_rect
        else:
            self.rect = self.button_settings_rect

    def update(self, dt):
        self.display()
        self.change_walker_music()
        self.change_walker_sounds()
        # self.update_images()


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



class Element(pygame.sprite.Sprite):
    def __init__(self, surf, pos, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(center=pos)

