from math import inf


def process_graph(result: list, way: int, points_in_v: list, passed: list) -> list:
    for i, j in enumerate(points_in_v):
        if way + j < result[i] and i not in passed:
            result[i] = way + j
    return result


def search_min_v(result: list, passed: list) -> int:
    v = -1
    min_num = inf
    for i, j in enumerate(result):
        if i not in passed and min_num > j:
            v = i
            min_num = j
    return v


def dijkstra(graph: list, start_point: int) -> list:
    passed = []
    result = [inf] * len(graph)
    v = start_point
    way = 0

    while v > -1:
        points_in_v = graph[v]
        result = process_graph(result, way, points_in_v, passed)
        passed.append(v)
        v = search_min_v(result, passed)
        way = result[v]
    return result


if __name__ == '__main__':
    graph = [
        [0, 1, inf, 1, inf],
        [1, 0, 5, 2, 2],
        [inf, 5, 0, inf, 2],
        [1, 2, inf, 0, 1],
        [inf, 2, 2, 1, 0]
    ]
    start_point = 0
    result = dijkstra(graph, start_point)
    print(result)
