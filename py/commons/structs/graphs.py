# coding=utf-8
from queue import PriorityQueue


class Vertex:
    __slots__ = '_element'

    def __init__(self, value):
        self._element = value

    def element(self):
        return self._element

    def __lt__(self, other):
        return self.element() < other.element()

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return str(self._element)

    def __repr__(self):
        return f'Vertex({str(self._element)})'


class Edge:
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, value):
        self._origin = u
        self._destination = v
        self._element = value

    def endpoints(self):
        return self._origin, self._destination

    def opposite(self, v):
        return self._destination if v is self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))


class Graph:
    """Represents a simple graph using an adjacency mao."""

    def __init__(self, is_directed=False):
        self._outgoing = {}
        self._incoming = {} if is_directed else self._outgoing

    def is_directed(self):
        return self._outgoing is not self._incoming

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj_map = self._outgoing if outgoing else self._incoming
        return len(adj_map[v])

    def incident_edges(self, v, outgoing=True):
        adj_map = self._outgoing if outgoing else self._incoming
        for edge in adj_map[v].values():
            yield edge

    def insert_vertex(self, value=None):
        v = Vertex(value)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, value=None):
        edge = Edge(u, v, value)
        self._outgoing[u][v] = edge
        self._incoming[v][u] = edge

    def _dfs(self, u, discovered):
        for e in self.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                self._dfs(v, discovered)

    def dfs_components(self, u):
        discovered = {u: None}
        self._dfs(u, discovered)
        return discovered

    def construct_path(self, u, v, discovered):
        if v not in discovered:
            return []
        vertices = [v]
        cur = v
        while cur is not u:
            edge = discovered[cur]
            vertices.append(edge.opposite(cur))
            cur = edge.opposite(cur)
        return list(reversed(vertices))

    def _bfs(self, s, discovered):
        cur_level = [s]
        while len(cur_level) > 0:
            next_level = []
            for u in cur_level:
                for e in self.incident_edges(u):
                    v = e.opposite(u)
                    if v not in discovered:
                        discovered[v] = e
                        next_level.append(v)
            cur_level = next_level

    def bfs_components(self, u):
        discovered = {u: None}
        self._bfs(u, discovered)
        return discovered

    def dijkstra(self, u):
        D = {v: float('inf') for v in self.vertices()}
        D[u] = 0

        visited = []
        pq = PriorityQueue()
        pq.put((0, u))
        while not pq.empty():
            dist, cur_vertex = pq.get()
            visited.append(cur_vertex)

            for e in self.incident_edges(cur_vertex):
                v = e.opposite(cur_vertex)
                if v not in visited:
                    edge_dist = e.element()
                    old_cost = D[v]
                    new_cost = D[cur_vertex] + edge_dist
                    if new_cost < old_cost:
                        pq.put((new_cost, v))
                        D[v] = new_cost
        return D
