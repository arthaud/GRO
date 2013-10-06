#!/usr/bin/python2
# -*- coding: utf-8 -*-

def is_connected(graph):
    """
        Returns whether a graph is connected or not.
    """
    def visit(node, visited):
        visited.add(node)
        for e in node.edges_out:
            n = e.other_side(node)
            if n not in visited:
                visit(n, visited)

    if graph.order() <= 1: # useless cases                   
        return True

    if not graph.oriented:
        visited = set()
        x = next(iter(graph.nodes))
        visit(x, visited)
        return len(visited) == graph.order()
    else:
        raise NotImplementedError()
    
