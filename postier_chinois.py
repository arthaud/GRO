#!/usr/bin/python2
# -*- coding: utf-8 -*-
from graphs import Graph, Node, Edge
from eulerian import eulerian_path_euler

def dijkstra_min_cost(origin, dest):
    '''
    Retourne le coût minimum pour aller de origin vers dest.
    précondition: le graphe est connexe
    '''
    if origin is dest:
        return 0

    reachable_nodes = [(e.cost, e.other_side(origin)) for e in origin.edges_out]
    reachable_nodes.sort(key=lambda n: n[0])

    while True:
        cost, node = reachable_nodes.pop(0)
        if node is dest:
            return cost

        for edge in node.edges_out:
            node_reachable = edge.other_side(node)
            reachable_nodes.append((cost + edge.cost, node_reachable))

        reachable_nodes.sort(key=lambda n: n[0])

def dijkstra_min_cost_path(origin, dest):
    '''
    Retourne le chemin (liste d'arêtes) de coût minimum pour aller de origin vers dest.
    précondition: le graphe est connexe
    '''
    if origin is dest:
        return []

    reachable_nodes = [(e.cost, [e], e.other_side(origin)) for e in origin.edges_out]
    reachable_nodes.sort(key=lambda n: n[0])

    while True:
        cost, path, node = reachable_nodes.pop(0)
        if node is dest:
            return path

        for edge in node.edges_out:
            node_reachable = edge.other_side(node)
            reachable_nodes.append((cost + edge.cost, path + [edge], node_reachable))

        reachable_nodes.sort(key=lambda n: n[0])

def postier_chinois(g):
    '''
    Retourne le chemin optimal pour le problème du postier chinois, ou None s'il n'y a pas de chemin.
    Attention : l'algorithme peut modifier le graphe.
    '''
    if not g.is_connected():
        return None

    if g.oriented:
        raise NotImplementedError()

    # Création du graphe partiel
    pg = Graph()
    pg.oriented = False

    # Copie des nœuds de degré impaire
    for node in g.nodes:
        if len(node.edges_out) % 2 == 1:
            pg.nodes.append(Node(node.data))

    if not pg.nodes: # graphe eulérien
        return eulerian_path_euler(g)

    # Copie des arêtes
    pg_nodes = set(pg.nodes)
    while pg_nodes:
        node_pg = pg_nodes.pop()
        node = filter(lambda n: n.data == node_pg.data, g.nodes)[0]
        for edge in node.edges_out:
            other_side_pg = filter(lambda n: n.data == edge.other_side(node).data, pg_nodes)
            if other_side_pg:
                other_side_pg = other_side_pg[0]
                edge_pg = Edge(node_pg, other_side_pg, edge.cost)
                node_pg.edges_out.add(edge_pg)
                other_side_pg.edges_out.add(edge_pg)

    # Transformation en clique
    pg_nodes = set(pg.nodes)
    while pg_nodes:
        node_pg = pg_nodes.pop()
        for node in pg_nodes:
            if not node_pg.exists_edge_to(node):
                # Récuperation des nœuds dans le graphe initial
                node_pg_g = filter(lambda n: n.data == node_pg.data, g.nodes)[0]
                node_g = filter(lambda n: n.data == node.data, g.nodes)[0]

                # Création de l'arête
                edge = Edge(node_pg, node, dijkstra_min_cost(node_pg_g, node_g))
                node_pg.edges_out.add(edge)
                node.edges_out.add(edge)

    # Recherche du couplage parfait de coût minimum
    edges = set() # ensemble des arêtes
    for node_pg in pg.nodes:
        edges.update(node_pg.edges_out)

    def aux(matching, nodes, cost):
        if len(nodes) == len(pg.nodes):
            return matching, cost

        best_matching, best_cost = None, 0

        for edge in edges:
            if edge.origin not in nodes and edge.dest not in nodes:
                matching_copy = matching[:]
                matching_copy.append(edge)
                nodes_copy = set(nodes)
                nodes_copy.add(edge.origin)
                nodes_copy.add(edge.dest)

                result_matching, result_cost = aux(matching_copy, nodes_copy, cost + edge.cost)
                if best_matching is None or best_cost > result_cost:
                    best_matching, best_cost = result_matching, result_cost

        return best_matching, best_cost

    best_matching, best_cost = aux([], set(), 0)

    # On double les arêtes dans best_matching
    for edge_pg in best_matching:
        origin = filter(lambda n: n.data == edge_pg.origin.data, g.nodes)[0]
        dest = filter(lambda n: n.data == edge_pg.dest.data, g.nodes)[0]
        path = dijkstra_min_cost_path(origin, dest)

        for edge in path:
            new_edge = Edge(edge.origin, edge.dest, edge.cost)
            edge.origin.edges_out.add(new_edge)
            edge.dest.edges_out.add(new_edge)

    return eulerian_path_euler(g)
