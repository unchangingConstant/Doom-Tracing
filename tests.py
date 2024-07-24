from engine import Engine
from actors import *
import map
from geometry import *

david = Camera()

def ray_segment_intersect_distance(ray_origin: list[float], ray_vector: list[float], segment: LineSeg) -> float:
        delta_y = ray_origin[1] - segment.get_y_pos()
        delta_x = ray_origin[0] - segment.get_x_pos()

        ray_x_component = ray_vector[0]
        seg_x_component = segment.get_orientation()[0]

        ray_y_component = ray_vector[1]
        seg_y_component = segment.get_orientation()[1]

        distance_to_intersect_along_ray = ((seg_x_component * delta_y) - (seg_y_component * delta_x)) / ((seg_y_component * ray_x_component) - (seg_x_component * ray_y_component))
        distance_to_intersect_along_seg = ((ray_x_component * -delta_y) - (ray_y_component * -delta_x)) / ((seg_y_component * ray_x_component) - (seg_x_component * ray_y_component))

        ray_intersect_valid = distance_to_intersect_along_ray > 0
        seg_intersect_valid = distance_to_intersect_along_seg > 0 and distance_to_intersect_along_seg < segment.get_length()

        if ray_intersect_valid and seg_intersect_valid:
            return distance_to_intersect_along_ray
        return 0

if __name__ == "__main__":
    print(Engine().render(map.map_1, david, (1600, 900), 100))
