import pygame as pg

SCREENSIZE = (800,600)
PADDLESIZE = (60,20)
PLAYERSPEED = 8

BALLRADIUS = 20
DEFAULT_BALLSPEED = 1.5
DIFFICULTY_RATE = 0.00003


POPULATION_SIZE = 100
MUTATION_RATE = 0.1
FPS_CAP = -1


BLACK = (0,0,0)
WHITE = (255,255,255)
pg.font.init()
font = pg.font.SysFont("Courier New", 16)
