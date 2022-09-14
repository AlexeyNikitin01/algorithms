from collections import deque


def beard_first_search(graph: dict) -> bool:
    search_queue = deque()
    search_queue.extend(graph['you'])
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person, 'is seller')
                return True
            else:
                search_queue.extend(graph[person])
                searched.append(person)
    return False


def person_is_seller(person: str) -> bool:
    if person[-1] == 'm':
        return True
    return False


if __name__ == '__main__':
    graph = {'you': ['alice', 'jon', 'alex'],
             'alice': ['you', 'perri', 'worm'],
             'jon': [],
             'alex': [],
             'perri': [],
             'worm': [],
             }
    beard_first_search(graph)
