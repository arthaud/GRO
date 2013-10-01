#!/usr/bin/python2
# -*- coding: utf-8 -*-
from graphs import Graph, Node, Edge
import hamiltonien

def print_ok(string):
    print "\033[92m" + string + "\033[0m"

def print_warn(string):
    print "\033[93m" + string + "\033[0m"

def print_err(string):
    print "\033[91m" + string + "\033[0m"

def test(condition, tested_fn, graph_nb):
    if(condition):
        print_ok("OK")
    else:
        print_err("Error testing " + tested_fn + " on graph number " + str(graph_nb))

if __name__ == '__main__':
    graphs = []

    # Format: [Graph, connected]
    graphs.append([Graph('tests/1.gph'), True])
    graphs.append([Graph('tests/2.gph'), True])
    graphs.append([Graph('tests/3.gph'), False])

    #tests connexité
    tested_fn = "Graph.is_connected"
    i = 0
    for g in graphs:
        i = i + 1
        test(g[0].is_connected() == g[1], tested_fn, i)
