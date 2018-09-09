import pygame, math, time, random
from pygame.locals import *

class EndingScreen():
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit(0)
    #screen.fill(0)
    #pygame.font.init()
    #font = pygame.font.Font(None, 24)
    #text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
    #textRect = text.get_rect()
    #textRect.centerx = screen.get_rect().centerx
    #textRect.centery = screen.get_rect().centery + 24
    #screen.blit(gameover, (0, 0))
    #screen.blit(text, textRect)