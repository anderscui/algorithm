# coding=utf-8
import unittest

from commons.structs.graphs import Graph


class TestGraphs(unittest.TestCase):
    def test_graph_basic(self):
        g = Graph()
        v1 = g.insert_vertex('u')
        v2 = g.insert_vertex('v')
        v3 = g.insert_vertex('w')
        v4 = g.insert_vertex('z')

        self.assertEqual(4, len(g.vertices()))

        g.insert_edge(v1, v2, 'e')
        g.insert_edge(v2, v3, 'f')
        g.insert_edge(v1, v3, 'g')
        g.insert_edge(v3, v4, 'h')

        self.assertEqual(4, len(g.edges()))

        e1 = g.get_edge(v1, v2)
        self.assertEqual((v1, v2), e1.endpoints())
        self.assertEqual('e', e1.element())

        e0 = g.get_edge(v1, v4)
        self.assertIsNone(e0)

        components = g.dfs_components(v1)
        path_vertices = g.construct_path(v1, v4, components)
        self.assertListEqual(['u', 'v', 'w', 'z'], [v.element() for v in path_vertices])

        components = g.bfs_components(v1)
        path_vertices = g.construct_path(v1, v4, components)
        self.assertListEqual(['u', 'w', 'z'], [v.element() for v in path_vertices])

        components = g.bfs_components(v4)
        path_vertices = g.construct_path(v4, v1, components)
        self.assertListEqual(['z', 'w', 'u'], [v.element() for v in path_vertices])

    def test_dijkstra_shortest(self):
        # raw article: https://stackabuse.com/dijkstras-algorithm-in-python/
        g = Graph()
        vertices = {}
        for i in range(9):
            vertices[i] = g.insert_vertex(i)

        g.insert_edge(vertices[0], vertices[1], 4)
        g.insert_edge(vertices[0], vertices[6], 7)
        g.insert_edge(vertices[1], vertices[6], 11)
        g.insert_edge(vertices[1], vertices[7], 20)
        g.insert_edge(vertices[1], vertices[2], 9)
        g.insert_edge(vertices[2], vertices[3], 6)
        g.insert_edge(vertices[2], vertices[4], 2)
        g.insert_edge(vertices[3], vertices[4], 10)
        g.insert_edge(vertices[3], vertices[5], 5)
        g.insert_edge(vertices[4], vertices[5], 15)
        g.insert_edge(vertices[4], vertices[7], 1)
        g.insert_edge(vertices[4], vertices[8], 5)
        g.insert_edge(vertices[5], vertices[8], 12)
        g.insert_edge(vertices[6], vertices[7], 1)
        g.insert_edge(vertices[7], vertices[8], 3)

        self.assertEqual(9, len(g.vertices()))
        self.assertEqual(15, g.edge_count())

        distances = g.dijkstra(vertices[0])
        distances = sorted([(v.element(), dist) for v, dist in distances.items()])
        self.assertListEqual([(0, 0), (1, 4), (2, 11), (3, 17), (4, 9), (5, 22), (6, 7), (7, 8), (8, 11)], distances)
