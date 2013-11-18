#!/usr/bin/python2
# -*- coding: utf-8 -*-
import numpy
import argparse

def verifier_matrice(a):
    assert a.shape[0] == a.shape[1] # matrice carrée
    assert all(sum(line) == 1.0 for line in a) # somme d'une ligne = 1

def generer_dot(a):
    '''
    Retourne le contenu d'un .dot représentant le graphe représenté par la matrice a
    '''
    s = 'digraph Graphe {\n'
    n = a.shape[0]

    for i in range(n):
        for j in range(n):
            if a[i,j] > 0:
                s += '\t%s -> %s [label=%s]\n' % (chr(ord('A') + i), chr(ord('A') + j), a[i,j])

    s += '}'
    return s

def position_proba(matrice_graphe, scarabee, tour):
    '''
    scarabee : entier qui indique la position initiale du scarabée (A=0, B=1, ..)
    Retourne une matrice ligne où chaque case contient la probabilité que le scarabée se retrouve à cette position après un certain nombre de tours.
    '''
    n = matrice_graphe.shape[0]
    pos_scarabee = numpy.array([int(i == scarabee) for i in range(n)])

    for _ in range(tour):
        pos_scarabee = pos_scarabee.dot(matrice_graphe)

    return pos_scarabee

exemple = numpy.array([
    [0.0, 0.6, 0.2, 0.0, 0.2, 0.0],
    [0.6, 0.0, 0.4, 0.0, 0.0, 0.0],
    [0.2, 0.4, 0.0, 0.4, 0.0, 0.0],
    [0.0, 0.0, 0.4, 0.0, 0.4, 0.2],
    [0.2, 0.0, 0.0, 0.4, 0.0, 0.4],
    [0.0, 0.0, 0.0, 0.2, 0.4, 0.4],
])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Promenade des petits scarabées')
    parser.add_argument('graphe_file')
    parser.add_argument('nb_scarabees', type=int)

    args = parser.parse_args()
    verifier_matrice(exemple)
