import math
import numpy as np


def generate_falloff_map(size):
    '''Generate a falloff map with size (x,x) size'''
    generated_map = np.zeros((size, size), dtype=float)

    for i in range(size):
        for j in range(size):
            x = i / size * 2 - 1
            y = j / size * 2 - 1

            value = max(abs(x), abs(y))
            generated_map[i][j] = _evaluate(value)

    return generated_map


def _evaluate(value):
    a = 3.0
    b = 2.2

    return math.pow(value, a) / (math.pow(value, a) + math.pow(b - b * value, a))
