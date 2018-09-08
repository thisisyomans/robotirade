import pygame, sys, time, math, random
from pygame.locals import *

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [300, 240]
pi = math.pi
acc = [0, 0]
arrows = []
badtimer = 100
badtimer1 = 0
badguys = [[-35, 100]]
healthvalue = 194
dead = False

player = pygame.image.load('resources/PNG/Soldier1/soldier1_gun.png')
grass = pygame.image.load('resources/PNG/Tiles/tile_01.png')
castle1 = pygame.image.load('resources/PNG/towerDefense_tile205.png')
castle = pygame.transform.rotate(castle1, -90)
arrow1 = pygame.image.load('resources/PNG/Tiles/tile_533.png')
arrow = pygame.transform.scale(arrow1, (32, 32))
badguyimg1 = pygame.image.load('resources/PNG/Robot1/robot1_hold.png')
badguyimg = badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

class SceneBase:
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    def Update(self):
        pass

    def Render(self, screen):
        while 1:
            #exitcode = 1
            badtimer -= 1

            screen.fill(0)
            for x in range(width//grass.get_width() + 1):
                for y in range(height//grass.get_height() + 1):
                    screen.blit(grass,(x * 60, y * 60))
            screen.blit(pygame.transform.flip(castle, True, False), (531, 30))
            screen.blit(pygame.transform.flip(castle, True, False), (531, 135))
            screen.blit(pygame.transform.flip(castle, True, False), (531, 240))
            screen.blit(pygame.transform.flip(castle, True, False), (531, 345))

            position = pygame.mouse.get_pos()
            angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
            playerrot = pygame.transform.rotate(player, 360-angle * (360 / (2 * pi)))
            playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
            screen.blit(playerrot, playerpos1)

            for bullet in arrows:
                index = 0
                velx = math.cos(bullet[0]) * 10
                vely = math.sin(bullet[0]) * 10
                bullet[1] += velx
                bullet[2] += vely
                if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
                    arrows.pop(index)
                index += 1
                for projectile in arrows:
                    arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
                    screen.blit(arrow1, (projectile[1], projectile[2]))

            if badtimer == 0:
                badguys.append([-35, random.randint(50, 430)])
                badtimer = 100 - (badtimer1 * 2)
                if badtimer1 >= 35:
                    badtimer1 = 35
                else:
                    badtimer1 += 5
            index = 0
            for badguy in badguys:
                if badguy[0] > 640:
                    badguys.pop(index)
                badguy[0] += 7
                badrect = pygame.Rect(badguyimg.get_rect())
                badrect.top = badguy[1]
                badrect.right = badguy[0]
                if badrect.right > 531:
                    healthvalue -= random.randint(5, 20)
                    print(healthvalue)
                    badguys.pop(index)
                index1 = 0
                for bullet in arrows:
                    bullrect = pygame.Rect(arrow.get_rect())
                    bullrect.left = bullet[1]
                    bullrect.top = bullet[2]
                    if badrect.colliderect(bullrect):
                        acc[0] += 1
                        badguys.pop(index)
                        arrows.pop(index1)
                    index1 += 1
                index += 1
            for badguy in badguys:
                screen.blit(badguyimg, badguy)

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))

run_game(width, height, 60, TitleScene())
