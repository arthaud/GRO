#!/usr/bin/python2
# -*- coding: utf-8 -*-
from graphs import *
from hamiltonian import *
from connected import *
from eulerian import *
from tsp import *
import datetime

def print_ok(string):
    print "\033[92m" + string + "\033[0m"

def print_warn(string):
    print "\033[93m" + string + "\033[0m"

def print_err(string):
    print "\033[91m" + string + "\033[0m"

def test(condition, tested_fn, graph_nb, graph_name, exec_time):
    if condition:
        print_ok("OK in %s.%ss"% (exec_time.seconds, exec_time.microseconds))
    else:
        print_err("Error testing %s on graph number %s: %s" % (tested_fn, graph_nb, graph_name))

def test_one(graphs, fun, indice):
    fun_name = "Graph." + fun.__name__ + "()"
    print "Testing " + fun_name + "..."
    i = 0
    for g in graphs:
        i = i + 1
        start = datetime.datetime.now()
        condition = fun(g[0]) == g[indice]
        exec_time = datetime.datetime.now() - start
        test(condition, fun_name, i, g[0].name, exec_time)

if __name__ == '__main__':
    graphs = []

    # Format: [Graph, connected, eulerian, semi-eulerian, semi-hamiltonian]
    graphs.append([read_gph('tests/1.gph'), True, True, False, True])
    graphs.append([read_gph('tests/2.gph'), True, False, True, False])
    graphs.append([read_gph('tests/3.gph'), False, False, False, False])
    graphs.append([read_gph('tests/4.gph'), True, False, False, True])
    graphs.append([read_tsp('tests/berlin52.tsp'), True, False, False, True])
    graphs.append([read_tsp('tests/d657.tsp'), True, True, False, True])
#    graphs.append([read_tsp('tests/fl1577.tsp'), False, False, False, False])
    graphs.append([read_tsp('tests/bier127.tsp'), True, True, False, True])
    graphs.append([read_tsp('tests/u724.tsp'), True, False, False, True])
    graphs.append([read_gph('tests/complete.gph'), True, True, False, True])
    graphs.append([read_gph('tests/complete_cost.gph'), True, True, False, True])
#    graphs.append([read_hcp('tests/alb1000.hcp'), True, True, False, True]) #todo
#    graphs.append([read_hcp('tests/alb2000.hcp'), True, True, False, True]) #todo

    #tests connexité
    test_one(graphs, is_connected, 1)

    #tests eulérianité
    test_one(graphs, is_eulerian, 2)

    # tests semi eulerianité
    test_one(graphs, is_semi_eulerian, 3)

    # tests semi hamiltoniannité
    test_one(graphs, is_semi_hamiltonian, 4)
