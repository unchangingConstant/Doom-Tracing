import pygame
from actors import *
from engine import Engine
import map
import time
import os
import sys

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)

height = 900
width = 1600
rays = 1600

columnWidth = width / rays

windowDim = (width, height)
win = pygame.display.set_mode(windowDim)

if __name__ == "__main__":
    run = True
    david = Camera()

    while run:

        fps_start = time.time()
        start = time.time()
    
        win.fill((0, 0, 0))

        pixelColumns = Engine().render(map.map_1, david, (width, height), rays)

        currentCol = 0
        for col in pixelColumns:
            rectTop = (height - col) / 2
            wallRect = pygame.Rect(currentCol, rectTop, columnWidth, col)
            pygame.draw.rect(win, (127, 127, 127), wallRect)
            currentCol += columnWidth

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()

        if userInput[pygame.K_a]:
            david.turn(Camera.LEFT)
        if userInput[pygame.K_d]:
            david.turn(Camera.RIGHT)
        if userInput[pygame.K_w]:
            david.move(Camera.FORWARD)
        if userInput[pygame.K_s]:
            david.move(Camera.BACKWARD)

        stop = time.time()
        pygame.time.delay(25 - (int(1000 * (stop - start))))
        fps_stop = time.time()

        win.blit(font.render(f"{int(1 / (fps_stop-fps_start))} VIEW FPS - {int(1 / (stop-start))} REAL FPS", False, (0, 255, 0)), (0, 0))
        pygame.display.update()