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
        self.edges_out = [] # liste des arêtes qui sortent du nœud pour pointer sur d'autres
        self.data = data
    
    def __hash__(self):
        return hash(self.data)
    
    def degree(self):
        return len(self.edges_out)

    def __repr__(self):
        return "Node(%s)" % self.data

class Graph:
    def __init__(self, oriented=False):
        self.nodes = set() # liste des noeuds du graphe
        self.oriented = oriented

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
            visit(self.nodes[0], visited)
            return len(visited) == self.order()
        else:
            print "TODO: Graph.is_connected : case oriented"
            return None
