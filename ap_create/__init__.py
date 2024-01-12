from random import randint
from math import sqrt

def quadratic_formula(a:int, b:int, c:int) -> list:
    # ( -b +- sqrt( b^2 - 4ac ) ) / 2a
    opposite_b = 0 - b
    discriminant = ( b ** 2 ) - ( 4 * a * c )
    two_a = 2 * a

    roots = []
    if discriminant < 0:
        roots = [None, None]
    else:
        root_1 = ( opposite_b + sqrt(discriminant) ) / two_a
        root_2 = ( opposite_b - sqrt(discriminant) ) / two_a
        roots = [root_1, root_2]
        roots.sort()

    return roots

def generate_quadratic(range_min: int = -10, range_max: int = 10) -> list:
    b = randint(range_min, range_max)
    c = randint(range_min, range_max)

    return [1, b, c]

if __name__ == "__main__":
    print(f'{"-" * 10}\nQuadSolver\n{"-" * 10}')
    print('What do you want to do today?')
    options = {
        '1': 'Practice Solving Quadratics'
        '2': 'Generate a Random Quadratic'
        '3': 'Solve a Quadratic'
        '4': 'Quit QuadSolver'
    }
