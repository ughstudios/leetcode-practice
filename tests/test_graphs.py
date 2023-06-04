""" Tests for graphs module """
from graphs import Graph, WeightedGraph


def test_topological_sort() -> None:
    graph = Graph()
    graph.add_edge('A', 'C')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'H')
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'G')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'C')
    graph.add_edge('D', 'F')

    assert graph.topological_sort() == ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']


def test_dijkstra_algorithm() -> None:
    graph = WeightedGraph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node('G')

    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 5)
    graph.add_edge('C', 'F', 8)
    graph.add_edge('F', 'G', 7)
    graph.add_edge('B', 'C', 6)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('B', 'E', 3)
    graph.add_edge('D', 'E', 4)
    graph.add_edge('E', 'G', 9)

    print(graph.dijkstra('A'))
