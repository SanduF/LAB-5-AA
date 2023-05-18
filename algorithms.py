from queue import PriorityQueue


def dijkstra(graph, start_vertex):
    D = {
        v: float('inf') for v in range(graph.v)
    }
    D[start_vertex] = 0

    priority_queue = PriorityQueue()
    priority_queue.put((0, start_vertex))

    while not priority_queue.empty():
        dist, curr_vertex = priority_queue.get()
        graph.visited.append(curr_vertex)

        for neighbor in range(graph.v):
            if graph.edges[curr_vertex][neighbor] != -1:
                distance = graph.edges[curr_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_weight = D[neighbor]
                    new_weight = D[curr_vertex] + distance
                    if new_weight < old_weight:
                        priority_queue.put((new_weight, neighbor))
                        D[neighbor] = new_weight
    return D


def floyd_warshall(graph):
    D = graph.edges.copy()

    for k in range(graph.v):
        for i in range(graph.v):
            for j in range(graph.v):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    return D

