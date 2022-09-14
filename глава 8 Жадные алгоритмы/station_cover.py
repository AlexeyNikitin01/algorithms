def search_covered_states(states: set, stations: dict) -> set:
    final_station = set()
    passed_station = []

    while states:
        best_station = ''
        covered_station = set()
        for station, covered_states_of_station in stations.items():
            if not station in passed_station:
                if len(states & covered_states_of_station) > len(covered_station):
                    best_station = station
                    covered_station = states & covered_states_of_station
        passed_station.append(best_station)
        states -= stations[best_station]
        final_station.add(best_station)

    return final_station


if __name__ == '__main__':
    states = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
    stations = {
        'kone': {'id', 'nv', 'ut'},
        'ktwo': {'wa', 'id', 'mt'},
        'kthree': {'or', 'nv', 'ca'},
        'kfour': {'nv', 'ut'},
        'kfive': {'ca', 'az'},
    }
    result = search_covered_states(states, stations)
    print(f'stations for covering all states: {result}')
