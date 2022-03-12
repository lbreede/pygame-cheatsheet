from csv import reader
from os import walk
import pygame
from settings import *


def import_csv_layout(path):
    lst = []
    with open(path) as f:
        layout = reader(f, delimiter=",")
        for row in layout:
            lst.append(list(row))
    return lst


def import_folder(path, force_tilesize=False):
    surface_list = []
    for _, __, images in walk(path):
        for img in images:
            fullpath = path + "/" + img
            image_surf = pygame.image.load(fullpath).convert_alpha()
            if force_tilesize:
                image_surf = pygame.transform.scale(image_surf, (TILESIZE, TILESIZE))
            surface_list.append(image_surf)
    return surface_list
