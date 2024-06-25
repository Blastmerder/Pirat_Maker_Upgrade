import pygame
from os import walk
from settings import *


def import_folder(path):
    surface_list = []

    for folder_name, sub_folder, img_files in walk(path):
        for image_name in img_files:
            full_path = path + '/' + image_name
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.rotozoom(image_surf, 0, TILE_SIZE/64)
            surface_list.append(image_surf)

    return surface_list


def import_folder_dict(path):
    surface_dict = {}

    for folder_name, sub_folder, img_files in walk(path):
        for image_name in img_files:
            full_path = path + '/' + image_name
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.rotozoom(image_surf, 0, TILE_SIZE/64)
            surface_dict[image_name.split('.')[0]] = image_surf

    return surface_dict
