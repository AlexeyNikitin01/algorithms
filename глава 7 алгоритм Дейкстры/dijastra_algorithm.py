from math import inf


def relax(result: list, way: int, points_in_v: list, passed: set) -> list:
    for vertex, edge in enumerate(points_in_v):
        if way + edge < result[vertex] and vertex not in passed:
            result[vertex] = way + edge
    return result


def search_min_v(result: list, passed: set) -> int:
    v = -1
    min_num = inf
    for i, j in enumerate(result):
        if i not in passed and min_num > j:
            v = i
            min_num = j
    return v


def dijkstra(graph: list, start_point: int) -> list:
    passed = set()
    result = [inf] * len(graph)
    v = start_point
    way = 0

    while v > -1:
        points_in_v = graph[v]
        result = relax(result, way, points_in_v, passed)
        passed.add(v)
        v = search_min_v(result, passed)
        way = result[v]
    return result


if __name__ == '__main__':
    # списки смежности сделать
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
