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
        return "Edge(%s, %s, %s)" % (repr(self.origin), repr(self.dest), cost)

class Node:
    def __init__(self, data):
        self.edges_out = set() # liste des arêtes qui sortent du nœud pour pointer sur d'autres
        self.data = data # must be unique
    
    def __hash__(self):
        return hash(self.data)
    
    def degree(self):
        return len(self.edges_out)

    def __repr__(self):
        return "Node(%s)" % self.data

class Graph:
    def __init__(self, path):
        self.nodes = [] # liste des noeuds du graphe

        nodes_added = dict()
        f = open(path, 'r')
        (nb_v, nb_e, oriented) = map(int, f.readline().split(' '))
        self.oriented = oriented == 1
        for i in range(nb_v):
            data = int(f.readline())
            n = Node(data)
            self.nodes.append(n)
            nodes_added[data] = n
        for i in range(nb_e):
            #(orig, dest, cost) = map(int, (f.readline()+" 1").split(' ')[:3])
            line = f.readline()
            try:
                (orig, dest, cost) = map(int, line.split(' '))
            except(ValueError):
                (orig, dest) = map(int, line.split(' '))
                cost = 1
                
            n_orig = nodes_added[orig]
            n_dest = nodes_added[dest]
            n_orig.edges_out.add(Edge(n_orig, n_dest, cost))
            if not self.oriented:
                n_dest.edges_out.add(Edge(n_orig, n_dest, cost))
        
    def order(self):
        return len(self.nodes)

    def is_connected(self):
        def visit(node, visited):
            visited.add(node)
            for e in node.edges_out:
                n = e.other_side(node)
                if n not in visited:
                    visit(n,visited)

        if self.order() <= 1: # useless cases                   
            return True
        if not self.oriented:
            visited = set()
            x = next(iter(self.nodes))
            visit(x, visited)
            return len(visited) == self.order()
        else:
            print "TODO: Graph.is_connected : case oriented"
            return None

