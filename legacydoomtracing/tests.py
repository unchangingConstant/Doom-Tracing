from renderer import Engine
from map import map
from player import Player
import numpy as np

if __name__ == "__main__":
    engine = Engine()
    david = Player(np.array([0, 0]))

    engine.render(map, david)

    #print(engine.rotateVector(45, np.array([0, 1])))

'''
if self.rayDebug:
    print(f"[{intersection[0]}, {intersection[1]}]")
    print(f"({rayOrigin[0]}, {rayOrigin[1]}) + [{rayVector[0]}, {rayVector[1]})")
    print(f"[{line.vert1}, {line.vert2}]")
'''

