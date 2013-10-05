#!/usr/bin/python2
# -*- coding: utf-8 -*-

import graphs
import heapq
import random

def ant(graph, max_iter_without_improvement=100, node_from=None):
    """ Ant colony optimization """

    def weight(edge):
        try:
            return 1 / float(edge.cost) + edge.ph * graph.order()
        except AttributeError:
            return 1 / float(edge.cost)

    best_cost = 0
    best_solution = None
    iter_without_improvement = 0

    if node_from is None:
        node_from = graph.nodes[0]

    while iter_without_improvement < max_iter_without_improvement:
        nodes_done = set((node_from,))
        path = [node_from]
        edges = []
        node = node_from
        cost = 0

        while len(nodes_done) < graph.order():
            valid_edges = filter(lambda edge: edge.other_side(node) not in nodes_done, node.edges_out)

            sum_costs = sum(weight(i) for i in valid_edges)
            r = random.random() * sum_costs
            c = 0
            for e in valid_edges:
                c += weight(e)
                if c > r:
                    edge = e
                    break

            cost += edge.cost
            node = edge.other_side(node)
            nodes_done.add(node)
            path.append(node)
            edges.append(edge)
        
        if cost < best_cost or best_solution is None:
            best_cost = cost
            best_solution = path
            iter_without_improvement = 0
        else:
            iter_without_improvement += 1

        for e in edges:
            try:
                e.ph += 1 / float(cost)
            except AttributeError:
                e.ph = 1 / float(cost)


    return (best_cost, best_solution)


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

    heap = []
    for edge in node_from.edges_out:
        other = edge.other_side(node_from)
        if other not in nodes_done:
            heapq.heappush(heap, (edge.cost, other))

    best_cost = 0
    best_path = None
    for i in range(1): #range(2 if len(nodes_done) < 14 else 1):
        if not heap:
            break
        edge_cost, node = heapq.heappop(heap)
        cost, path_end = nearest_neighbor(graph, node, first_node, nodes_done)
        cost += edge_cost

        if cost < best_cost or best_path is None:
            best_cost = cost
            best_path = path_end

    return (best_cost, [node_from] + best_path)

def two_opt(solution):
    """
        2-opt algorithm, try to find a better solution than a given one.
    """

    best_cost, best_path = solution
    improvement_made = True
    
    while improvement_made:
        improvement_made = False
        for i in range(len(best_path)-1):
            for j in range(i + 1, len(best_path)-1):
                ni = best_path[i]
                nj = best_path[j]
                new_cost = best_cost - best_path[i+1].cost_to(ni) - best_path[j+1].cost_to(nj) + ni.cost_to(nj) + best_path[j+1].cost_to(best_path[i+1])

                if new_cost < best_cost:
                    improvement_made = True
                    best_cost = new_cost
                    best_path = best_path[:i+1] + best_path[i+1:j+1][::-1] + best_path[j+1:]

    return (best_cost, best_path)

def read_tsp(path):
    """
        Create a graph from a file of the form:
            [6 useless lines]
            1 x1 y1
            2 x2 y2
            ...
        These graphs are found here http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/tsp/
    """
    def distance(a, b):
        return ( (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]) ) ** 0.5

    points = []
    with open(path, 'r') as f:
        for i in range(1, 7): f.readline()

        line = f.readline()
        while line != "EOF\n":
            x, y = map(float, line.split()[1:3])
            points.append((x, y))
            line = f.readline()

    node_id = 0
    nodes = []
    for (x, y) in points:
        new_node = graphs.Node(node_id)
        node_id += 1
        for other in nodes:
            edge = graphs.Edge(other[1], new_node, distance((x, y), other[0]))
            other[1].edges_out.add(edge)
            new_node.edges_out.add(edge)

        nodes += [((x, y), new_node)]

    g = graphs.Graph(path)
    g.nodes = map(lambda x: x[1], nodes)
    g.oriented = False
    g.name = path.split('/')[-1]
    return g

