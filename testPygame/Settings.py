import pygame as py
import os
import random
import math
from os import listdir
from os.path import isfile, join

""" CONSTANT"""
WIDTH, HEIGHT = 800, 600
TITLE = "JEU VACHEMENT COOL"
FPS = 60


"""SET THE VALUES"""
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption(TITLE)


