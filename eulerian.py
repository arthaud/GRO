#!/usr/bin/python2
# -*- coding: utf-8 -*-

def get_odd_vertices(graph):
    """
    Returns true if the graph is eulerian or semi-eulerian
    """
    if not graph.oriented:
        nb_odd_deg = 0
        odd_list = []
        for n in graph.nodes:
            if len(n.edges_out) % 2 != 0:
                odd_list.append(n)
        return odd_list
    else:
        print "TODO: is_eulerian case oriented"
        return None

def is_eulerian(graph):
    nb_odd_vertices=len(get_odd_vertices(graph))
    return nb_odd_vertices == 0 and graph.is_connected()

def is_semi_eulerian(graph):
    nb_odd_vertices = len(get_odd_vertices(graph))
    return nb_odd_vertices == 2 and graph.is_connected()

# no multigraph nor reflexive edge
# equivalent to bruteforce
def eulerian_path_lat_mat(graph):
    def gen_lat_mat(graph):
        nb_n = len(graph.nodes)
        lat_mat = [[None for i in range(nb_n) ] for j in range(nb_n) ]
        for n in graph.nodes:
            for e in n.edges_out:
                n2 = e.other_side(n)
                lat_mat[n.data-1][n2.data-1] = [[n.data, n2.data]]
        return lat_mat

    def lat_mat_mul(a, b):
        nb_n = len(a)
        result = [[None for i in range(nb_n) ] for j in range(nb_n) ]
        for i in range(nb_n):
            for j in range(nb_n):
                # for each cell
                result[i][j] = []
                for k in range(nb_n):
                    # "multiplication"
                    cell_a = a[i][k]
                    cell_b = b[k][j]
                    if cell_a is not None and cell_b is not None:
                        for l in cell_a: # for each path in cell_a
                            for m in cell_b: # for each path in cell_b
                                path = l[:]
                                path.extend(m[1:])
                                edges = set()
                                for n in range(len(path)-1):
                                    edge = (path[n], path[n+1])
                                    edge_rev = (path[n+1], path[n])
                                    if edge not in edges:
                                        edges.add(edge)
                                        edges.add(edge_rev)
                                    else:
                                        path = None
                                        break
                                if path is not None:
                                    result[i][j].append(path)
                if result[i][j] == []:
                    result[i][j] = None
        return result

    def lat_mat_pow(lat_mat, n):
        result = lat_mat_mul(lat_mat, lat_mat)
        for i in range(n-2):
            result = lat_mat_mul(lat_mat, result)

        return result


    nb_a = 0
    for n in graph.nodes:
        nb_a += len(n.edges_out)
    nb_a /=2
    a = gen_lat_mat(graph)
    b = lat_mat_pow(a, nb_a)
    for row in b:
        for cell in row:
            print cell
    
    return None
