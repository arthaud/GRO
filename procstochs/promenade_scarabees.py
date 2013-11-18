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
        verifier_matrice(self.probas)

def verifier_matrice(a):
    assert all(sum(line) == 1.0 for line in a)

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
