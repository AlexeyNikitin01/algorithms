from collections import namedtuple
from math import inf


Point = namedtuple('Point', 'to weight')


def relax(result: list, points, way: int, passed: set) -> list:
    for e in points:
        if e.to not in passed and e.weight + way < result[e.to]:
            result[e.to] = e.weight + way
    return result


def search_min_v(passed: set, result: list) -> int:
    v = -1
    min_num = inf
    for i, j in enumerate(result):
        if i not in passed and j < min_num:
            v = i
            min_num = j
    return v


def dijakstra(graph: dict, start_point: int) -> list:
    passed = set()
    way = 0
    result = [inf]*len(graph)
    result[start_point] = 0
    v = start_point

    while v > -1:
        points = graph[v]
        result = relax(result, points, way, passed)
        passed.add(v)
        v = search_min_v(passed, result)
        way = result[v]
    return result


if __name__ == '__main__':
    graph = {
        0: {Point(1, 1), Point(3, 1)},
        1: {Point(0, 1), Point(2, 5), Point(3, 2), Point(4, 2)},
        2: {Point(1, 5), Point(4, 2)},
        3: {Point(0, 1), Point(1, 2), Point(4, 1)},
        4: {Point(1, 2), Point(2, 2), Point(3, 1)},
    }
    for v in graph.keys():
        print(f'v: {v}')
        for e in graph[v]:
            print(f'to - {e.to} weight - {e.weight}')
    start_point = 0
    result = dijakstra(graph, start_point)
    print(f'\nstart_point - {start_point} result - {result}')
