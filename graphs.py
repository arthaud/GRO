#!/usr/bin/python2
# -*- coding: utf-8 -*-

class Edge:
    """
        Class that represents an edge as an origin vertice and a destination
        vertice and a cost.
    """
    def __init__(self, origin, dest, cost=1):
        self.origin = origin
        self.dest = dest
        self.cost = cost

    def other_side(self, node):
        return self.origin if node is self.dest else self.dest
    
    def __repr__(self):
        return "Edge(%s, %s, %s)" % (self.origin.data, self.dest.data, self.cost)

class Node:
    """
        Represents a vertex as a set of edges.
    """
    def __init__(self, data):
        self.edges_out = set() # set of nodes that go out of that vertex
        self.data = data # an unique identifient for that vertex
    
    def __hash__(self):
        return hash(self.data)
    
    def degree(self):
        """
            Returns the degree of that vertex, that is, the number of edges
            that connect to it."
        """
        return len(self.edges_out)

    def __repr__(self):
        return "Node(%s, [%s])" % (self.data, ', '.join(map(repr, self.edges_out)))

    def cost_to(self, other):
        """
            Returns the cost to go from that node to the node other.
        """
        return self.edge_to(other).cost

    def edge_to(self, other):
        """
            Returns the edge from that vertex to the vertex other.
            Throw a RuntimeError if there is no such edge.
        """
        for edge in self.edges_out:
            if edge.other_side(self) == other:
                return edge
        raise RuntimeError("Not complete graph")

class Graph:
    """
        Represents a graph as a list of node.
    """
    def __init__(self, path=None):
        self.nodes = [] # nodes of the graph

        if path:
            self.name = path.split('/')[-1]
        else:
            self.name = ""

    def __repr__(self):
        return 'Graph(\n%s\n)' % ',\n'.join(map(repr, self.nodes))

    def order(self):
        return len(self.nodes)

def read_gph(path):
    """
        Construct a Graph from a file of the form:
            4 2 0
            1
            2
            3
            4
            1 2
            3 4
    """
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

