import numpy as np

class LineSeg:
    def __init__(self, vertice1: np.array, vertice2: np.array):
        self.vert1 = vertice1
        self.vert2 = vertice2

line1 = LineSeg(np.array([0, 100]), np.array([100, 100]))
line2 = LineSeg(np.array([100, 100]), np.array([100, 0]))
line3 = LineSeg(np.array([0, 200]), np.array([100, 200]))

map = [line1, line2, line3]
