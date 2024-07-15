from map import LineSeg
from player import *
import math

#30 units = 1 meter
#450 pixels = 2 meters about

class Engine:
    def render(self, map: list[LineSeg], player: Player):

        pixelCols = []
        for deltaX in range(100):

            xCoord = 50 - deltaX
            angleRadians = self.__findProjAngle(xCoord, 50)

            ray = self.rotateVector(angleRadians, player.facing)
            colDist = self.__castRay(player.pos, ray, map)
            if colDist == 0:
                colDist = 810000
            colHeight = (450 * 30) / (colDist * math.cos(angleRadians))
            colHeight = int(colHeight)

            pixelCols.append(colHeight)

        return pixelCols

    def __castRay(self, rayOrigin: np.array, rayVector: np.array, map: list[LineSeg]) -> float:
        closestIntersection = 810000

        for line in map:
            intersection = self.__findIntersection(rayOrigin, rayVector, line.vert1, line.vert2)
            if intersection is None:
                continue

            intersectDist = self.__distBetweenPoints(rayOrigin, intersection)

            if intersectDist < closestIntersection or closestIntersection is None:
                closestIntersection = intersectDist
        
        return closestIntersection

    def rotateVector(self, angle: int, vector: np.array) -> np.array:
        newX = math.cos(angle) * vector[0] - math.sin(angle) * vector[1]
        newY = math.sin(angle) * vector[0] + math.cos(angle) * vector[1]
        vector = np.array([newX, newY])

        return vector

    #ChatGPT wrote this I was too lazy
    def __findIntersection(self, rayOrigin: np.array, rayVector: np.array, segVert1: np.array, segVert2: np.array):
        p = rayOrigin
        r = rayVector
        q = segVert1
        s = segVert2 - segVert1

        # Calculate cross product of r and s
        r_cross_s = np.cross(r, s)

        if np.all(r_cross_s == 0):
            # Lines are parallel or collinear
            return None

        # Calculate t and u
        q_minus_p = q - p
        t = np.cross(q_minus_p, s) / r_cross_s
        u = np.cross(q_minus_p, r) / r_cross_s

        if t >= 0 and 0 <= u <= 1:
            # Calculate the intersection point
            collision_point = p + t * r
            return collision_point
        else:
            # Ray does not intersect the segment within the bounds
            return None
        
    def __distBetweenPoints(self, point1: np.array, point2: np.array) -> float:
        vector = np.array(point2 - point1)
        distance = np.sqrt(np.sum(vector ** 2))

        return distance

    def __findProjAngle(self, xCoord: float, distanceFromPlane: float):
        return math.atan(xCoord / distanceFromPlane)
