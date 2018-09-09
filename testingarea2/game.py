import pygame, math, time, random
import gameplay, endingscene
from pygame.locals import *

while True:
    if gamestatus == 0:
        GamePlay()
    elif gamestatus == 1:
        EndingScreen()