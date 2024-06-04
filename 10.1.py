import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'a': {'b': 2, 'c': 1},
    'b': {'a': 2, 'd': 3},
    'c': {'a': 1, 'd': 2, 'f': 2, 'h': 1},
    'd': {'b': 3, 'c': 2, 'h': 3},
    'f': {'c': 2, 'g': 1},
    'g': {'f': 1, 'h': 2},
    'h': {'d': 3, 'c': 1, 'g': 2}
}

if __name__ == '__main__':
    while True:
        target = input('Введіть точку: ')
        if target in graph.keys():
            break
    shortest_paths = dijkstra(graph, target)

    print("Найкоротші шляхи до вершини", target, "з усіх інших вершин:")
    for vertex, distance in shortest_paths.items():
        if vertex == target:
            continue
        print(f"Від {vertex} до {target}: {distance}")
