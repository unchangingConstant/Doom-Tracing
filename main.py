import pygame
from actors import *
from engine import Engine
import map

pygame.init()

height = 900
width = 1600
rays = 100

columnWidth = width / rays

windowDim = (width, height)
win = pygame.display.set_mode(windowDim)

if __name__ == "__main__":
    run = True
    david = Camera()

    while run:
    
        win.fill((0, 0, 0))
        print(david.get_position())

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

        pygame.time.delay(32)

        pygame.display.update()