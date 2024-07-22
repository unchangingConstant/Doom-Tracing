from vector_math import *

class LineSeg:
    def __init__(self, origin: tuple[float], orientation_vector: tuple[float], length: float):
        self._origin = origin
        self._orientation_vector = normalize_vector(orientation_vector)
        self._length = length
    
    def get_origin(self) -> tuple[float]:
        return self._origin
    
    def get_x_pos(self) -> float:
        return self._origin[0]
    
    def get_y_pos(self) -> float:
        return self._origin[1]
    
    def get_orientation(self) -> tuple[float]:
        return self._orientation_vector
    
    def get_length(self) -> float:
        return self._length
