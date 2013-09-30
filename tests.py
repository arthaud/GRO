# -*- coding: utf-8 -*-
from graphs import Graph, Node, Edge

def test1():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    edge1 = Edge(node1, node2)
    edge2 = Edge(node2, node3)
    edge3 = Edge(node3, node1)
    edge4 = Edge(node3, node4)
    edge5 = Edge(node4, node5)
    edge6 = Edge(node5, node3)

    node1.edges_out = [edge1, edge3]
    node2.edges_out = [edge1, edge2]
    node3.edges_out = [edge2, edge3, edge4, edge6]
    node4.edges_out = [edge4, edge5]
    node5.edges_out = [edge6, edge5]

    g = Graph()
    g.nodes = [node1, node2, node3, node4, node5]
    return g

def test2():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    edge1 = Edge(node1, node2)
    edge2 = Edge(node2, node3)
    edge3 = Edge(node3, node4)
    edge4 = Edge(node4, node5)
    edge5 = Edge(node5, node2)
    edge6 = Edge(node2, node4)
    edge7 = Edge(node4, node6)

    node1.edges_out = [edge1]
    node2.edges_out = [edge1, edge2, edge5, edge6]
    node3.edges_out = [edge2, edge3]
    node4.edges_out = [edge3, edge4, edge6, edge7]
    node5.edges_out = [edge4, edge5]
    node6.edges_out = [edge7]

    g = Graph()
    g.nodes = [node1, node2, node3, node4, node5, node6]
    return g

def test3():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    edge1 = Edge(node1, node2)
    edge2 = Edge(node3, node4)

    node1.edges_out = [edge1]
    node2.edges_out = [edge1]
    node3.edges_out = [edge2]
    node4.edges_out = [edge2]

    g = Graph()
    g.nodes = [node1, node2, node3, node4]
    return g

def test(toto):
    print "OK" if toto else "BOOOO"

if __name__ == '__main__':
    g = test1()
    test(g.is_connected())
    g = test2()
    test(g.is_connected())
    g = test3()
    test(not g.is_connected())
