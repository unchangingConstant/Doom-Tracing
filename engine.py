from geometry import LineSeg
from math import *
from vector_math import *
from actors import Camera

#   100 pixels = 1 meter

class Engine:

    def render(cls, map: list[LineSeg], camera: Camera, resolution: tuple[int], ray_count: int):
        ray_columns = []
        for curr_ray_column in range(ray_count):

            ray_x_position = (ray_count - (2 * curr_ray_column)) / camera.get_dist_from_view_plane()
            #   Optimize below code? Normalization doesn't have to be a seperate step...
            ray_vector = cls.__find_hypotenuse_vector(camera.get_orientation(), camera.get_dist_from_view_plane(), ray_x_position)
            ray_vector = normalize_vector(ray_vector)
            print(ray_vector)

            column_height = cls.__cast_ray(map, camera.get_position(), ray_vector)
            column_height = int((column_height * resolution[0] * 15) / find_proj_of_vector(camera.get_orientation(), ray_vector))
            ray_columns.append(column_height)

        return ray_columns
    
    def __cast_ray(cls, map: list[LineSeg], ray_origin: list[float], ray_vector: list[float]) -> float:
        shortest_dist_to_wall = 10000000

        for wall in map:
            intersect_distance = cls.__ray_segment_intersect_distance(ray_origin, ray_vector, wall)
            if intersect_distance == 0:
                continue
            if intersect_distance < shortest_dist_to_wall:
                shortest_dist_to_wall = intersect_distance
        
        return (1 / shortest_dist_to_wall)

    def __find_hypotenuse_vector(cls, adj_side_vector: list[float], adj_side_length: float, opp_side_length: float) -> list[float]:
        scaled_adj_vector = scale_vector(adj_side_vector, adj_side_length)
        scaled_opp_vector = scale_vector(find_orthongonal_vector(adj_side_vector), opp_side_length)
        hypotenuse_vector = add_vectors(scaled_adj_vector, scaled_opp_vector)
        
        return hypotenuse_vector
    
    def __ray_segment_intersect_distance(cls, ray_origin: list[float], ray_vector: list[float], segment: LineSeg) -> float:
        delta_y = ray_origin[1] - segment.get_y_pos()
        delta_x = ray_origin[0] - segment.get_x_pos()

        ray_x_component = ray_vector[0]
        seg_x_component = segment.get_orientation()[0]

        ray_y_component = ray_vector[1]
        seg_y_component = segment.get_orientation()[1]

        distance_to_intersect_along_ray = ((seg_x_component * delta_y) - (seg_y_component * delta_x)) / ((seg_y_component * ray_x_component) - (seg_x_component * ray_y_component))
        distance_to_intersect_along_seg = ((ray_x_component * -delta_y) - (ray_y_component * -delta_x)) / ((seg_x_component * ray_y_component) - (seg_y_component * ray_x_component))

        print(f"{distance_to_intersect_along_ray}, {distance_to_intersect_along_seg}")

        ray_intersect_valid = distance_to_intersect_along_ray > 0
        seg_intersect_valid = distance_to_intersect_along_seg > 0 and distance_to_intersect_along_seg < segment.get_length()

        if ray_intersect_valid and seg_intersect_valid:
            return distance_to_intersect_along_ray
        return 0
