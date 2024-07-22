from math import *
from geometry import *

def scale_vector(vector: list[float], scalar: float) -> list[float]:
    new_vector = []
    for comp in vector:
        new_vector.append(comp * scalar)

    return new_vector

def add_vectors(vector_1: list[float], vector_2: list[float]) -> list[float]:
    if len(vector_1) != len(vector_2):
        raise ValueError("Length of vectors differ from each other in vector addition")
    
    new_vector = []
    for comp in range(len(vector_1)):
        new_vector.append(vector_1[comp] + vector_2[comp])

    return new_vector

def find_orthongonal_vector(vector: list[float]) -> list[float]:
    if len(vector) != 2:
        raise ValueError("vector length not 2 when finding orthogonal vector")
    
    new_vector = []
    new_vector.append(-1 * vector[1])
    new_vector.append(vector[0])

    return new_vector

def find_dot_product(vector_1: list[float], vector_2: list[float]) -> float:
    if len(vector_1) != len(vector_2):
        raise ValueError("Length of vectors differ from each other when calculating dot product")
    
    dot_product = 0
    for component in range(len(vector_1)):
        dot_product += vector_1[component] * vector_2[component]
    
    return dot_product

def normalize_vector(vector: list[float]) -> list[float]:
    dot_product = find_dot_product(vector, vector)
    new_vector = scale_vector(vector, 1 / sqrt(dot_product))

    return new_vector

def find_proj_of_vector(vector: list[float], projected_vector: list[float]) -> list[float]:
    shared_component = find_dot_product(projected_vector, vector) / find_dot_product(vector, vector)
    return shared_component
