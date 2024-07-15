import pygame
import numpy as np
from player import *
from renderer import Engine
from map import map

pygame.init()

height = 450
width = 800

windowDim = (width, height)
win = pygame.display.set_mode(windowDim)

if __name__ == "__main__":
    run = True
    david = Player(np.array([0, 0]))
    engine = Engine()

    while run:

        win.fill((0, 0, 0))

        pixelColumns = engine.render(map, david)

        currentCol = 0
        for col in pixelColumns:
            rectTop = (height - col) / 2
            pygame.draw.rect(win, (127, 127, 127), pygame.Rect(currentCol, rectTop, 10, col))
            currentCol += 8

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()

        if userInput[pygame.K_a]:
            david.turn(Player.LEFT)
        if userInput[pygame.K_d]:
            david.turn(Player.RIGHT)
        if userInput[pygame.K_w]:
            david.move(Player.FORWARD)
        if userInput[pygame.K_s]:
            david.move(Player.BACKWARD)

        pygame.time.delay(32)

        pygame.display.update()