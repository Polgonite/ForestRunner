# Example file showing a circle moving on screen
import pygame
from pygame.locals import *
import random

import math

from components.player import playerClass
from components.obstacle import obstacleClass
from components.gargoyle import gargoyleClass
from components.environment import gameEnvironment

def main():
    global a
    global b
    global c
    global scrolls
    global gameStarted
    global obstacles
    global timer_event_id
    global obstacle_tracker

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((320, 240),HWSURFACE|DOUBLEBUF|RESIZABLE)
    fake_screen = screen.copy()
    clock = pygame.time.Clock()
    running = True

    size = width, height = 320*4, 240*4
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    player = playerClass()

    a = 0
    b = 0
    c = 0

    obstacle_tracker = 0

    gameStarted = False
    
    timer_event_id = pygame.USEREVENT + 1

    obstacles = []


    environment = gameEnvironment()

    scrolls = []
    for i in range(0, len(environment.layers)):
        scrolls.append(0)
    
    tiles = math.ceil(width / environment.layers[1].get_width()) + 1

    def spawn_obstacles():
        global obstacle_tracker
        
        obstacle_tracker += 1

        if obstacle_tracker > 6:
            if random.randint(0,10) + obstacle_tracker > 15:
                obstacle_tracker = 0
                if random.randint(0, 10) > 8:
                    obstacles.append(gargoyleClass())
                else:
                    obstacles.append(obstacleClass())
    
    def drawForeground():
        global scrolls
        global gameStarted

        if gameStarted:
            layers = [environment.layers[i] for i in range(9)]
            scroll_speeds = [1, 1.1, 0, 0, 0, 0.75, 0.7, 0.65, 0.6]

            for i in range(tiles):
                for j, (layer, speed) in enumerate(zip(layers, scroll_speeds)):
                    fake_screen.blit(layer, (layer.get_width() * i + scrolls[j], -550))
                    scrolls[j] -= speed

                    # RESET THE SCROLL FRAME 
                    if abs(scrolls[j]) > layer.get_width(): 
                        scrolls[j] = 0
        else:
            layers = [environment.layers[i] for i in range(9)]
            scroll_speeds = [1, 1.1, 0, 0, 0, 0.75, 0.7, 0.65, 0.6]

            for i in range(tiles):
                for j, (layer, speed) in enumerate(zip(layers, scroll_speeds)):
                    fake_screen.blit(layer, (layer.get_width() * i + scrolls[j], -550))
                    scrolls[j] -= speed

                    # RESET THE SCROLL FRAME 
                    if abs(scrolls[j]) > layer.get_width(): 
                        scrolls[j] = 0    

    def drawBackground():
        global scrolls
        global gameStarted

        if gameStarted:
            layers = [environment.layers[i] for i in range(11)]
            scroll_speeds = [1.1, 1, 1, 1, 1, 0.75, 0.7, 0.65, 0.6, 0.65, 0.6]

            for i in range(tiles):
                for j, (layer, speed) in reversed(list(enumerate(zip(layers, scroll_speeds)))):
                    fake_screen.blit(layer, (layer.get_width() * i + scrolls[j], -550))
                    scrolls[j] -= speed

                    # RESET THE SCROLL FRAME 
                    if abs(scrolls[j]) > layer.get_width(): 
                        scrolls[j] = 0
        else:
            layers = [environment.layers[i] for i in range(11)]
            scroll_speeds = [1.1, 1, 1, 1, 1, 0.75, 0.7, 0.65, 0.6, 0.65, 0.6]

            for i in range(tiles):
                for j, (layer, speed) in reversed(list(enumerate(zip(layers, scroll_speeds)))):
                    fake_screen.blit(layer, (layer.get_width() * i + scrolls[j], -550))

                    # RESET THE SCROLL FRAME 
                    if abs(scrolls[j]) > layer.get_width(): 
                        scrolls[j] = 0
    
    def redrawGameWindow():
        global a
        global b
        global c
        global gameStarted
        global obstacles
        global timer_event_id

        b += 1
        if b == 15:
            a += 1
            b = 0
            if c >= 4:
                c = 0
            else:
                c += 1
        fake_screen.fill(black)
        drawBackground()
        if gameStarted:

            # Draw player
            if player.isJumping:
                if player.speed[1] <= -1:
                    if a >= 2:
                        a = 0
                    player.sprite = player.jump[a + 2]
                elif -1 < player.speed[0] < 0.1:
                    if a >= 4:
                        a = 0
                    player.sprite = player.jump[a + 4]
                else:
                    if a >= 2:
                        a = 0
                    player.sprite = player.jump[a + 8]
            elif player.isSliding and keys[pygame.K_DOWN]:
                if a > 5:
                    a = 3
                player.sprite = player.slide[a]
            elif player.isSliding:
                print(a)
                if a > 7:
                    a = 0
                    player.sprite = player.right[a]
                    player.isSliding = False
                player.sprite = player.slide[a]


            else:
                if a >= 6:
                    a = 0
                player.sprite = player.right[a]


            fake_screen.blit(player.sprite, player.rect)

            # Draw obstacles
            obstacles[:] = [x for x in obstacles if not (x.rect[0] < -150)]
            for i, obstacle in enumerate(obstacles):
                obstacle.rect = obstacle.rect.move(obstacle.speed)
                if type(obstacle) == gargoyleClass:
                    obstacle.sprite = obstacle.sprites[c]
                    fake_screen.blit(obstacle.sprite, obstacle.rect)
                else:
                    fake_screen.blit(obstacle.sprite, obstacle.rect)

            

            

            
            
        else:
            if player.isDead:
                if a >= 30:
                    a = 20
                player.sprite = player.die[int(a/5)]
            else:
                if a >= 4:
                    a = 0
                player.sprite = player.idle[a]
            
            # Draw obstacles
            obstacles[:] = [x for x in obstacles if not (x.rect[0] < -66)]
            for i, obstacle in enumerate(obstacles):
                fake_screen.blit(obstacle.sprite, obstacle.rect)
            
            fake_screen.blit(player.sprite, player.rect)

        screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
        pygame.display.flip()
    
    while running:
        clock.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
            elif event.type == timer_event_id:
                spawn_obstacles()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and gameStarted == False: 
            obstacles = []
            player.reset_position()
            gameStarted = True
            pygame.time.set_timer(timer_event_id, 100)
        
        if gameStarted:
            if keys[pygame.K_SPACE] and player.isJumping == False:
                player.isSliding = False
                player.speed[1] -= 3
                a = 1
            if keys[pygame.K_DOWN] and player.isJumping == False and player.isSliding == False:
                player.isSliding = True
                a = 0
            player.rect = player.rect.move(player.speed)
            player.do_state_magic()
            for obstacle in obstacles:
                if player.mask.overlap(pygame.mask.from_surface(obstacle.sprite), (obstacle.rect[0] - player.rect[0], obstacle.rect[1] - player.rect[1])):
                    gameStarted = False
                    player.isDead = True
                    pygame.time.set_timer(timer_event_id, 0)

        redrawGameWindow()

    pygame.quit()

main()   