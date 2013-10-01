#!/usr/bin/python2
# -*- coding: utf-8 -*-

def is_eulerian(graph):
    """
    Returns true if the graph is eulerian or semi-eulerian
    """
    if not graph.oriented:
        nb_odd_deg = 0
        for n in graph.nodes:
            if len(n.edges_out) % 2 != 0:
                nb_odd_deg += 1
        return (nb_odd_deg == 0 or nb_odd_deg == 2) and graph.is_connected()
    else:
        print "TODO: is_eulerian case oriented"
        return None

def eulerian_path_lat_mat(graph):
    def gen_lat_mat(graph):
        nb_n = len(graph.nodes)
        lat_mat = [[[[0]] for i in range(nb_n) ] for j in range(nb_n) ]
        for n in graph.nodes:
            for e in n.edges_out:
                n2 = e.other_side(n)
                lat_mat[n.data-1][n2.data-1] = [[n, n2]]
        return lat_mat
        
    gen_lat_mat(graph)
    return None
