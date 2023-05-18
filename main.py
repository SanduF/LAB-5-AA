import time
import random
import matplotlib.pyplot as plt

from graph import Graph
from algorithms import dijkstra, floyd_warshall


def generate_graph(graph, number_of_vertices):
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            if j != i and random.randint(0, 10) < 2:
                graph.add_edge(i, j, random.randint(1, 30))


def measure_execution_time(func: callable, *args: any) -> int:
    start = time.time()
    func(*args)
    end = time.time()
    return end - start


def display_results(x: list, y: list, title: str) -> None:
    plt.plot(x, y)
    plt.xlabel("Number of nodes")
    plt.ylabel("Execution Time")
    plt.title(title)
    plt.show()
    print(f"Results for {title}")
    for i in range(max(len(x), len(y))):
        print(f"V:{x[i]} -> t: {y[i]}")


if __name__ == "__main__":

    x = []
    y = []
    for v in range(1, 11):
        v *= 100

        g = Graph(v)
        generate_graph(g, v)

        t = measure_execution_time(floyd_warshall, g)
        y.append(t)
        x.append(v)

    display_results(x, y, "Floyd Warshall")

    # G = generate_nx_graph(...)
    # draw_graph(G)