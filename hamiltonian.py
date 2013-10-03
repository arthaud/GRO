#!/usr/bin/python2
# -*- coding: utf-8 -*-
import graphs

def is_hamiltonian(graph):
    # rapid test, only sufficient, not necessary
    min_degree = min(node.degree() for node in graph.nodes)
    if min_degree >= graph.order() / 2:
        return True

    # general test, complexity sucks
    return hamiltonian_path2(graph) != None

def hamiltonian_path(graph, node_from=None, nodes_done=frozenset()):
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
        path = hamiltonian_path(graph, other, nodes_done)
        if path:
            return [node_from] + path

    return None

def read_hcp(path):
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

        g = graphs.Graph()
        g.nodes = nodes
        return g

