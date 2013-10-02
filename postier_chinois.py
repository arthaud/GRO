#!/usr/bin/python2
# -*- coding: utf-8 -*-
from graphs import Graph, Node, Edge

def postier_chinois(g):
    '''
    Retourne le chemin optimal pour le problème du postier chinois, ou None s'il n'y a pas de chemin.
    '''
    if not g.is_connected():
        return None

    if g.oriented:
        raise NotImplementedError()

    # Création du graphe partiel
    pg = Graph(False)

    # copie des nœuds de degré impaire
    for node in g.nodes:
        if len(node.edges_out) % 2 == 1:
            pg.nodes.append(Node(node.data))

    # copie des arêtes
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
