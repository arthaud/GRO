#!/usr/bin/python2
# -*- coding: utf-8 -*-

import graphs

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
