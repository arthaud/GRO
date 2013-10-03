#!/usr/bin/python2
# -*- coding: utf-8 -*-
import graphs

def dirac_test(graph):
    """
        Dirac's theorem.
    """
    return len(graph.nodes) < 3 and min(node.degree() for node in graph.nodes) >= graph.order() / 2

def posa_test(graph):
    """
        Pósa's theorem.
    """
    n = len(graph.nodes)
    if n < 3: return False

    k = int((n+1)/2)
    degrees = [0 for i in range(0, k)]
    for node in graph.nodes:
        for d in range(0, node.degree()+1):
            if d < k:
                degrees[d] += 1

    for i in range(0, k):
        if degrees[i] > i:
            return False

    return True

def is_semi_hamiltonian(graph):
    """
        Returns whether a graph is hamilonian or not.
        The graph must be a simple graph and non-oriented.
    """
    # rapid tests, only sufficient
    if dirac_test(graph) or posa_test(graph):
        return True

    # general test, complexity sucks
    return hamiltonian_path2(graph) != None

def hamiltonian_path(graph, node_from=None, nodes_done=frozenset()):
    """
        Return a hamiltinian path if one exists or None.
        This is brute force.
        The graph must be non-oriented.
    """
    if node_from is None:
        node_from = graph.nodes[0]

    nodes_done = nodes_done | frozenset((node_from,))

    if len(nodes_done) == graph.order():
        return [node_from]

    for edge in node_from.edges_out:
        other = edge.other_side(node_from)
        if other in nodes_done:
            continue
        path = hamiltonian_path(graph, other, nodes_done)
        if path:
            return [node_from] + path

    return None

def hamiltonian_path2(graph, node_from=None, nodes_done=frozenset()):
    """
        Return a hamiltinian path if one exists or None.
        This is slitghly more efficient than brute force as it tries to stop sonner.
        The graph must be non-oriented.
    """
    if node_from is None:
        node_from = graph.nodes[0]

    nodes_done = nodes_done | frozenset((node_from,))

    if len(nodes_done) == graph.order():
        return [node_from]

    poss = filter(lambda x: x.other_side(node_from).degree() == 1, node_from.edges_out)

    if len(poss) == 1:
        path = hamiltonian_path(graph, poss[0].other_side(node_from), nodes_done)
        return [node_from] + path if path else None
    elif len(poss) > 1:
        return None

    for edge in node_from.edges_out:
        other = edge.other_side(node_from)
        if other in nodes_done:
            continue
        path = hamiltonian_path2(graph, other, nodes_done)
        if path:
            return [node_from] + path

    return None

def read_hcp(path):
    """
        Create a graph from a file of the form:
            [3 useless lines]
            DIMENSION : 1000
            [2 useless lines]
            node1 node2
            node3 node4
            ...
            -1
        These graphs are found here http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/tsp/
    """
    with open(path, 'r') as f:
        for i in range(1,4): f.readline()

        line = f.readline()
        nb_nodes = int(line.split()[2])

        f.readline()
        f.readline()

        nodes = []
        for i in range(0, nb_nodes):
            nodes.append(graphs.Node(i))

        line = f.readline()
        while line != "-1\n":
            a, b = map(int, line.split())
            edge = graphs.Edge(nodes[a-1], nodes[b-1])
            nodes[a-1].edges_out.add(edge)
            nodes[b-1].edges_out.add(edge)
            line = f.readline()

        g = graphs.Graph(path)
        g.nodes = nodes
        g.oriented = False
        return g

