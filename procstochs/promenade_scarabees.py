#!/usr/bin/python2
# -*- coding: utf-8 -*-
import numpy
import sys

class Graphe:
    def __init__(self, fichier):
        self.sommets = []
        for sommet in open(fichier, 'r').readlines():
            self.sommets.append([int(i) for i in sommet.split(' ')])

class Scarabee:
    def __init__(self, graphe, fichier_probas):
        self.graphe = graphe
        self.probas = []

        for ligne in open(fichier_probas, 'r').readlines():
            self.probas.append([float(i) for i in ligne.split(' ')])

        assert len(self.probas) == len(graphe.sommets), 'La matrice de probabilité ne correspond pas au graphe !'
        self.probas = numpy.array(self.probas)
        verifier_matrice(self.probas)

    def __repr__(self):
        return generer_dot(self.probas)

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

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print """
Usage: promenade_scarabees fichier_graphe fichier_proba fichier_proba...
"""
    fichier_graphe = sys.argv[1]
    g = Graphe(fichier_graphe)
    scarabees = []
    for scarabee in sys.argv[2:]:
        scarabees.append(Scarabee(g, scarabee))
