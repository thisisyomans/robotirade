import pygame, math, time, random, os, sys
from pygame.locals import *

##QUICK NOTE: some of the code contains features that haven't been fully implemented,
##so you will find code that currently might have no affect on the game whatsoever

#initialize game, base vars + values needed for setup
pygame.init()
pygame.display.set_caption('RoboTirade')
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [300, 240]
pi = math.pi
acc = [0, 0]
missiles = []
timerevil = 100
timerevil1 = 0
evildudes = [[-35, 100]]
healthvalue = 194
pygame.mixer.init()

#this is just alternative way for referencing filepaths, makes packaging w/ PyInstaller easier
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)

#NOTE: original resources
#player = pygame.image.load(resource_path(os.path.join('resources', 'PNG/Soldier1/soldier1_gun.png')))
#grass = pygame.image.load(resource_path(os.path.join('resources', 'PNG/Tiles/tile_01.png')))
#tower1 = pygame.image.load(resource_path(os.path.join('resources', 'PNG/towerDefense_tile205.png')))
#tower = pygame.transform.rotate(tower1, -90)
#missile1 = pygame.image.load(resource_path(os.path.join('resources', 'PNG/Tiles/tile_533.png')))
#missile = pygame.transform.scale(missile1, (32, 32))
#enemyimage1 = pygame.image.load(resource_path(os.path.join('resources', 'PNG/Robot1/robot1_hold.png')))
#enemyimage = enemyimage1
#healthbar = pygame.image.load(resource_path(os.path.join('resources', 'images/healthbar.png')))
#health = pygame.image.load(resource_path(os.path.join('resources', 'images/health.png')))
#gameover = pygame.image.load(resource_path(os.path.join('resources', 'images/gameover.png')))
#youwin = pygame.image.load(resource_path(os.path.join('resources', 'images/youwin.png')))

#towerhit = pygame.mixer.Sound(resource_path(os.path.join('resources', 'audio/explode.wav')))
#enemy = pygame.mixer.Sound(resource_path(os.path.join('resources', 'audio/enemy.wav')))
#shoot = pygame.mixer.Sound(resource_path(os.path.join('resources', 'audio/shoot.wav')))
#towerhit.set_volume(0.05)
#enemy.set_volume(0.05)
#shoot.set_volume(0.05)
#pygame.mixer.music.load(resource_path(os.path.join('resources', 'audio/moonlight.wav'))) ###NOTE: needs to be changed
#pygame.mixer.music.play(-1, 0.0)
#pygame.mixer.music.set_volume(0.25)

#NOTE: new resources
#image resources + small manipulations
player = pygame.image.load(resource_path(os.path.join('resources2', 'soldier1_gun.png')))
grass = pygame.image.load(resource_path(os.path.join('resources2', 'tile_01.png')))
tower1 = pygame.image.load(resource_path(os.path.join('resources2', 'towerDefense_tile205.png')))
tower = pygame.transform.rotate(tower1, -90)
missile1 = pygame.image.load(resource_path(os.path.join('resources2', 'tile_533.png')))
missile = pygame.transform.scale(missile1, (32, 32))
enemyimage1 = pygame.image.load(resource_path(os.path.join('resources2', 'robot1_hold.png')))
enemyimage = enemyimage1
healthbar = pygame.image.load(resource_path(os.path.join('resources2', 'healthbar.png')))
health = pygame.image.load(resource_path(os.path.join('resources2', 'health.png')))
gameover = pygame.image.load(resource_path(os.path.join('resources2', 'gameover.png')))
youwin = pygame.image.load(resource_path(os.path.join('resources2', 'youwin.png')))

#audio resources + small manipulations
towerhit = pygame.mixer.Sound(resource_path(os.path.join('resources2', 'explode.wav')))
enemy = pygame.mixer.Sound(resource_path(os.path.join('resources2', 'enemy.wav')))
shoot = pygame.mixer.Sound(resource_path(os.path.join('resources2', 'shoot.wav')))
towerhit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load(resource_path(os.path.join('resources2', 'moonlight.wav'))) ###NOTE: needs to be changed
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

#running var is used for switching from infinite loop gamescreen to end screen
#exitcode is used for deciding if the player won or lost, winning is currently not possible 
running = 1
exitcode = 0
while running:
    timerevil -= 1
    screen.fill(0)
    for x in range(width//grass.get_width() + 1):
            for y in range(height//grass.get_height() + 1):
                screen.blit(grass,(x * 60, y * 60))
    screen.blit(pygame.transform.flip(tower, True, False), (531, 30))
    screen.blit(pygame.transform.flip(tower, True, False), (531, 135))
    screen.blit(pygame.transform.flip(tower, True, False), (531, 240))
    screen.blit(pygame.transform.flip(tower, True, False), (531, 345))

    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360-angle * (360 / (2 * pi)))
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)

    for bullet in missiles:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            missiles.pop(index)
        index += 1
        for projectile in missiles:
            missile1 = pygame.transform.rotate(missile, 360 - projectile[0] * 57.29)
            screen.blit(missile1, (projectile[1], projectile[2]))

    if timerevil == 0:
        evildudes.append([-35, random.randint(50, 430)])
        timerevil = 100 - (timerevil1 * 2)
        if timerevil1 >= 35:
            timerevil1 = 35
        else:
            timerevil1 += 5
    index = 0
    for badguy in evildudes:
        if badguy[0] > 640:
            evildudes.pop(index)
        badguy[0] += 7
        badrect = pygame.Rect(enemyimage.get_rect())
        badrect.top = badguy[1]
        badrect.right = badguy[0]
        if badrect.right > 531:
            towerhit.play()
            healthvalue -= random.randint(5, 20)
            #print(healthvalue)
            evildudes.pop(index)
        index1 = 0
        for bullet in missiles:
            bullrect = pygame.Rect(missile.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                acc[0] += 1
                evildudes.pop(index)
                missiles.pop(index1)
            index1 += 1
        index += 1
    for badguy in evildudes:
        screen.blit(enemyimage, badguy)

#Originally you could actually win the game, so this commented out timer applies to that
#Game mechanic/purpose of timer: if you live long enough, you win!
    #font = pygame.font.Font(None, 24)
    #survivedtext = font.render(str((90000 - pygame.time.get_ticks())/60000) + ':' + str((90000 - pygame.time.get_ticks())/1000%60).zfill(2), True, (0, 0, 0))
    #textRect = survivedtext.get_rect()
    #textRect.topright = [635, 5]
    #screen.blit(survivedtext, textRect)

    screen.blit(healthbar, (5, 5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1 + 8, 8))

    pygame.display.flip()

    #event handling: key downs and up
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit(0)

            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True

            if event.key == K_SPACE:
                shoot.play()
                position = pygame.mouse.get_pos()
                acc[1] += 1
                missiles.append([math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32, playerpos1[1] + 32])

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False

    #movement system based on event handling of keys + keys array + current player position
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

    if healthvalue <= 0:
        gamestatus = False
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0

if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(resource_path(os.path.join('resources2', 'freesansbold.ttf')), 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(gameover, (0, 0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(resource_path(os.path.join('resources2', 'freesansbold.ttf')), 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(youwin, (0, 0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit(0)
            if event.key == K_r:
                running = 1
    pygame.display.flip()
