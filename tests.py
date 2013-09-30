#!/usr/bin/python2
# -*- coding: utf-8 -*-
from graphs import Graph, Node, Edge

def print_ok(string):
    print "\033[92m" + string

def print_warn(string):
    print "\033[93m" + string

def print_err(string):
    print "\033[91m" + string

def test(condition):
    print "OK" if condition else "BOOOO"

if __name__ == '__main__':
    graphs = []
    # Format: [Graph, connected]
    #graphs.append([Graph('tests/1.gph'), True])
    #graphs.append([Graph('tests/2.gph'), True])
    #graphs.append([Graph('tests/3.gph'), False])

    for g in graphs:
        test(g[0].is_connected == g[1])
