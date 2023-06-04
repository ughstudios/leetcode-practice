from collections import defaultdict
from typing import Any, Optional


class Graph:
    """ Implementation of a graph using a python dictionary """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex: Any, edge: Any):
        """ Adds a edge to the graph """
        self.graph[vertex].append(edge)

    def breadth_first_search(self, vertex):
        queue = [vertex]
        visited = set(vertex)
        while queue:
            popped_vertex = queue.pop(0)
            print(popped_vertex)
            for adjacent_vertex in self.graph[popped_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def depth_first_search(self, vertex):
        stack = [vertex]
        visited = set(vertex)
        while stack:
            popped_vertex = stack.pop()
            print(popped_vertex)
            for adjacent_vertex in self.graph[popped_vertex]:
                if popped_vertex not in visited:
                    visited.add(adjacent_vertex)
                    stack.append(adjacent_vertex)

    def _topological_sort(self, vertex: Any, visited: list, stack):
        visited.append(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self._topological_sort(i, visited, stack)

        stack.insert(0, vertex)

    def topological_sort(self):
        visited = []
        stack = []

        for key in list(self.graph):
            if key not in visited:
                self._topological_sort(key, visited, stack)

        return stack

    def find_path(self, start: Any, end: Any, path: list = []) -> Optional[list]:
        """ https://www.python.org/doc/essays/graphs/ """
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
        return None

    # Single Source Shortest Path Algorithms
    # BFS
    # Dijsktra's
    # Bellman Ford

    def bfs(self, start, end):
        """ Find shortest path using breadth first search, iteratively, only works with unweighted graphs """
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adj_vert in self.graph.get(node, []):
                # creates a copy of the list
                new_path = list(path)
                new_path.append(adj_vert)
                queue.append(new_path)


class WeightedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value: Any):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def dijkstra(self, initial):
        visited = {initial: 0}
        path = defaultdict(list)
        nodes = set(self.nodes)
        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                weight = current_weight + self.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(min_node)
        return visited, path
