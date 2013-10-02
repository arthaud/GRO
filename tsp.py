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

        return (node_from.cost_to(first_node), [node_from, first_node])

    closest = None
    closest_distance = sys.maxint
    for edge in node_from.edges_out:
        other = edge.other_side(node_from)

        if edge.cost < closest_distance and other not in nodes_done:
            closest = other
            closest_distance = edge.cost

    path_end = nearest_neighbor(graph, closest, first_node, nodes_done)
    return (closest_distance + path_end[0], [node_from] + path_end[1])

def two_opt(solution, max_iteration):
    """
        2-opt algorithm, try to find a better solution than a given one.
    """

    best_cost, best_path = solution

    for iterations in range(1, max_iteration):
        got_better_solution = False
        for i in range(1, len(best_path)-2):
            # [..., a, b, c, d, ...] -> [..., a, c, b, d, ...]
            a, b, c, d = (best_path[j] for j in range(i-1, i+3))
            new_cost = best_cost - a.cost_to(b) - c.cost_to(d) + a.cost_to(c) + b.cost_to(d)

            if new_cost < best_cost:
                got_better_solution = True
                best_cost = new_cost
                best_path = best_path[:i] + [c, b] + best_path[i+2:]

        if not got_better_solution:
            return None 

    return None if best_cost == solution[0] else (best_cost, best_path)
