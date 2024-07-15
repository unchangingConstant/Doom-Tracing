import numpy as np
import math

class Player:

    FORWARD = 2
    BACKWARD = -2

    RIGHT = -10 * (math.pi / 180)
    LEFT = 10 * (math.pi / 180)

    def __init__(self, position: np.array):
        self.pos = position
        self.facing = np.array([0, 1])

    def move(self, direction: int):
        self.pos = self.pos + self.facing * direction
    
    def turn(self, direction: int):
        self.facing = self.__rotateVector(direction, self.facing)
    
    #This exact function is in the Engine class. Maybe find another home for it?
    def __rotateVector(self, angle: int, vector: np.array) -> np.array:
        newX = math.cos(angle) * vector[0] - math.sin(angle) * vector[1]
        newY = math.sin(angle) * vector[0] + math.cos(angle) * vector[1]
        vector = np.array([newX, newY])

        return vector
