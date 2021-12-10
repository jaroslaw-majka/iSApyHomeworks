from math import sqrt


def rectangular_triangle_calculator(a: int, b: int) -> float:
    for side_length in (a, b):
        if not isinstance(side_length, int):
            raise ValueError('Please pass integers only')
    return sqrt(a**2 + b**2)
