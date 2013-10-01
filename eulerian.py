#!/usr/bin/python2
# -*- coding: utf-8 -*-
import copy

def is_eulerian(graph):
    """
    Returns true if the graph is eulerian or semi-eulerian
    """
    if not graph.oriented():
        for n in graph.nodes:
            if len(n.edges_out) % 2 != 0:
                nb_odd_deg += 1
        return (nb_odd_deg == 0 or nb_odd_deg == 2) and graph.is_connected()
    else:
        print "TODO: is_eulerian case oriented"
        return None

def eulerian_path():
    return None
