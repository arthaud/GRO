#!/usr/bin/python2
# -*- coding: utf-8 -*-
from graphs import Graph, Node, Edge
from hamiltonian import *
from connected import *
from eulerian import *
from tsp import *

def print_ok(string):
    print "\033[92m" + string + "\033[0m"

def print_warn(string):
    print "\033[93m" + string + "\033[0m"

def print_err(string):
    print "\033[91m" + string + "\033[0m"

def test(condition, tested_fn, graph_nb):
    if condition:
        print_ok("OK")
    else:
        print_err("Error testing %s on graph number %s" % (tested_fn, graph_nb))

def test_one(graphs, fun, indice):
    fun_name = "Graph." + fun.__name__ + "()"
    print "Testing " + fun_name + "..."
    i = 0
    for g in graphs:
        i = i + 1
        test(fun(g[0]) == g[indice], fun_name, i)

if __name__ == '__main__':
    graphs = []

    # Format: [Graph, connected, eulerian, semi-eulerian, hamiltonian]
    graphs.append([Graph('tests/1.gph'), True, True, False, True])
    graphs.append([Graph('tests/2.gph'), True, False, True, False])
    graphs.append([Graph('tests/3.gph'), False, False, False, False])
    graphs.append([Graph('tests/4.gph'), True, False, False, True])
    graphs.append([read_tsp('tests/berlin52.tsp'), True, False, False, True])
    graphs.append([read_tsp('tests/d657.tsp'), True, True, False, True])

    #tests connexité
    test_one(graphs, is_connected, 1)

    #tests eulérianité
    test_one(graphs, is_eulerian, 2)

    # tests semi eulerianité
    test_one(graphs, is_semi_eulerian, 3)

    # tests hamiltonian
    test_one(graphs, is_hamiltonian, 4)
