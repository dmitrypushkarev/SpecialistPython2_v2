def distance(p1: dict, p2: dict) -> float:
    """
    Расстояние между двумя точками
    """ 
    dist = [abs(p1[0]) + abs(p2[0]), abs(p1[1]) + abs(p2[1])]
    print(f'{dist}')

distance([1,2], [-2, 1])
