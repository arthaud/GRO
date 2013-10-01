#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def nearest_neighbor(graph, node_from=None, first_node=None, nodes_done=frozenset()):
    """
    Nearest Neighbor algorithm, simple approximation for TSP problem.
    Requires the graph to be complete.
    Returns (cost, [nodes...]).
    """

    if node_from is None:
        node_from = graph.nodes[0]

    if first_node is None:
        first_node = node_from

    nodes_done = nodes_done | frozenset((node_from,))

    if len(nodes_done) == graph.order():
        return_distance = 0
        for edge in first_node.edges_out:
            if edge.other_side(node_from) == first_node:
                return_distance = edge.cost
                break

        return (return_distance, [node_from, first_node])

    closest = None
    closest_distance = sys.maxint
    for edge in node_from.edges_out:
        other = edge.other_side(node_from)

        if edge.cost < closest_distance and other not in nodes_done:
            closest = other
            closest_distance = edge.cost

    path_end = nearest_neighbor(graph, closest, first_node, nodes_done)
    return (closest_distance + path_end[0], [node_from] + path_end[1])
