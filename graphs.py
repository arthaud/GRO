#!/usr/bin/python2
# -*- coding: utf-8 -*-

class Edge:
    def __init__(self, origin, dest, cost=1):
        self.origin = origin
        self.dest = dest
        self.cost = cost

    def other_side(self, node):
        return self.origin if node is self.dest else self.dest
    
    def __repr__(self):
        return "Edge(%s, %s, %s)" % (self.origin.data, self.dest.data, self.cost)

class Node:
    def __init__(self, data):
        self.edges_out = set() # liste des arêtes qui sortent du nœud pour pointer sur d'autres
        self.data = data # must be unique
    
    def __hash__(self):
        return hash(self.data)
    
    def degree(self):
        return len(self.edges_out)

    def __repr__(self):
        return "Node(%s, [%s])" % (self.data, ', '.join(map(repr, self.edges_out)))

    def cost_to(self, other):
        return self.edge_to(other).cost

    def edge_to(self, other):
        for edge in self.edges_out:
            if edge.other_side(self) == other:
                return edge
        raise RuntimeError("Not complete graph")

class Graph:
    def __init__(self, path=None):
        self.nodes = [] # liste des noeuds du graphe

        self.name = ""
        if path:
            self.name = path.split('/')[-1]

    def __repr__(self):
        return 'Graph(\n%s\n)' % ',\n'.join(map(repr, self.nodes))

    def order(self):
        return len(self.nodes)

    def copy(self):
        g = Graph()
        g.oriented = self.oriented

        for node in self.nodes:
            g.nodes.append(Node(node.data))

        g_nodes = set(g.nodes)
        while g_nodes:
            node_g = g_nodes.pop()
            node = filter(lambda n: n.data == node_g.data, self.nodes)[0]
            for edge in node.edges_out:
                other_side_g = filter(lambda n: n.data == edge.other_side(node).data, g.nodes)[0]
                if self.oriented:
                    node_g.edges_out.add(Edge(node_g, other_side_g, edge.cost))
                elif other_side_g in g_nodes:
                    edge_g = Edge(node_g, other_side_g, edge.cost)
                    node_g.edges_out.add(edge_g)
                    other_side_g.edges_out.add(edge_g)

        return g

def read_gph(path):
    nodes_added = dict()
    g = Graph(path)

    with open(path, 'r') as f:
        nb_v, nb_e, oriented = map(int, f.readline().split(' '))
        g.oriented = oriented == 1

        for i in range(nb_v):
            data = int(f.readline())
            n = Node(data)
            g.nodes.append(n)
            nodes_added[data] = n

        for i in range(nb_e):
            #(orig, dest, cost) = map(int, (f.readline()+" 1").split(' ')[:3])
            line = f.readline()
            try:
                orig, dest, cost = map(int, line.split(' '))
            except(ValueError):
                orig, dest = map(int, line.split(' '))
                cost = 1

            n_orig = nodes_added[orig]
            n_dest = nodes_added[dest]
            edge = Edge(n_orig, n_dest, cost)
            n_orig.edges_out.add(edge)
            if not g.oriented:
                n_dest.edges_out.add(edge)

    return g

