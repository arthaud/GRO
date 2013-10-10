#!/usr/bin/python2
# -*- coding: utf-8 -*-

from connected import *

def get_odd_vertices(graph):
    """
        Returns the number of nodes with odd number of vertices.
    """
    if not graph.oriented:
        nb_odd_deg = 0
        odd_list = []
        for n in graph.nodes:
            if len(n.edges_out) % 2 != 0:
                odd_list.append(n)
        return odd_list
    else:
        raise NotImplementedError()

def is_eulerian(graph):
    """
        Returns whether the graph is eulerian or not.
    """
    nb_odd_vertices=len(get_odd_vertices(graph))
    return nb_odd_vertices == 0 and is_connected(graph)

def is_semi_eulerian(graph):
    """
        Returns whether the graph is semi-eulerian but not eulerian or not.
    """
    nb_odd_vertices = len(get_odd_vertices(graph))
    return nb_odd_vertices == 2 and is_connected(graph)

def eulerian_path_euler(graph):
    """
        Returns an eulerian path og the graph or None if no such path exists.
    """
    def aux(node, visited_edges):
        result = [node]
        final_result = [node]

        while True:
            edges = [e for e in node.edges_out if e not in visited_edges]
            if not edges:
                break
            else:
                edge = edges[0]
                node = edge.other_side(node)
                result.append(node)
                visited_edges.add(edge)

        for node in result[1:]:
            cycle = aux(node, visited_edges)
            final_result += cycle

        return final_result

    if not is_connected(graph):
        return None

    odd_vertices = get_odd_vertices(graph)
    if len(odd_vertices) == 0:
        return aux(graph.nodes[0], set())
    elif len(odd_vertices) == 2:
        return aux(odd_vertices[0], set())
    else:
        return None

# no multigraph nor reflexive edge
# equivalent to bruteforce
def eulerian_path_lat_mat(graph):

    # computes the latin matrix of a graph
    def gen_lat_mat(graph):
        nb_n = len(graph.nodes)
        lat_mat = [[None for i in range(nb_n) ] for j in range(nb_n) ]

        # for each edge of the graph
        for n in graph.nodes:
            for e in n.edges_out:
                n2 = e.other_side(n)

                # add the correspondant path list to the matrix
                lat_mat[n.data-1][n2.data-1] = [[n.data, n2.data]]
        return lat_mat

    # computes the product of two path lists
    def path_list_mul(list1,list2):
        result = []

        # for each pair of paths
        for i in list1:
            for j in list2:

                # compute the product path
                path = i[:]
                path.extend(j[1:])

                # compute the edges to follow for this path
                edges = set()
                for n in range(len(path)-1):
                    edge = (path[n], path[n+1])
                    edge_rev = (path[n+1], path[n])
                    if edge not in edges:
                        edges.add(edge)
                        edges.add(edge_rev)
                    else:
                        # if the edge is already computed
                        # the path won't be eulerian
                        path = None
                        break
                if path is not None:
                    # if a correct path is computed, add it to the result
                    result.append(path)
        return result;

    # computes the product of two latin matrices
    def lat_mat_mul(a, b):
        nb_n = len(a)
        result = [[None for i in range(nb_n) ] for j in range(nb_n) ]
        for i in range(nb_n):
            for j in range(nb_n):
                # for each cell of the result matrix
                result[i][j] = []
                # compute the classic multiplication of matrices
                # with the path_list_mul function
                # sum(a[i][k] * b[k][j]) where some is union
                for k in range(nb_n):
                    cell_a = a[i][k]
                    cell_b = b[k][j]
                    if cell_a is not None and cell_b is not None:
                      result[i][j].extend(path_list_mul(cell_a,cell_b))
                if result[i][j] == []:
                    result[i][j] = None
        return result

    # computes the power of a latin matrix
    def lat_mat_pow(lat_mat, n):
        result = lat_mat_mul(lat_mat, lat_mat)
        for i in range(n-2):
            result = lat_mat_mul(lat_mat, result)

        return result

    # computes the powered latin matriced
    nb_a = 0
    for n in graph.nodes:
        nb_a += len(n.edges_out)
    nb_a /=2
    a = gen_lat_mat(graph)
    b = lat_mat_pow(a, nb_a)

    # compute the result as a list of pathes
    # may contain doubloons
    list = []
    for row in b:
        for cell in row:
            if cell is not None:
                list.extend(cell)

    return list
