class Camera:

    FORWARD = 3
    BACKWARD = -3

    RIGHT = -1
    LEFT = 1

    def __init__(self, position = (0, 0), orientation = (0, 1)):
        self._position = position
        self._orientation = orientation
        self._dist_from_view_plane = 10
    
    def get_orientation(self) -> list[float]:
        return [self._orientation[0], self._orientation[1]]
    
    def get_position(self) -> list[float]:
        return [self._position[0], self._position[1]]
    
    def get_dist_from_view_plane(self) -> int:
        return self._dist_from_view_plane

    def move(self, direction: int):
        self._position = (self._position[0] + (direction* self._orientation[0]), self._position[1] + (direction * self._orientation[1]))

    def turn(self, direction: int): #   Turns 6 degrees
        new_orientation_x = (0.994521895368 * self._orientation[0]) - (direction * 0.104528463268 * self._orientation[1])
        new_orientation_y = (direction * 0.104528463268 * self._orientation[0]) + (0.994521895368 * self._orientation[1])
        self._orientation = (new_orientation_x, new_orientation_y)
