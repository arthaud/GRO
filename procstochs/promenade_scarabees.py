#!/usr/bin/python2
# -*- coding: utf-8 -*-
import numpy
import sys

def verifier_matrice(a):
    assert all(sum(line) == 1.0 for line in a)

exemple = numpy.array([
    [0.0, 0.6, 0.2, 0.0, 0.2, 0.0],
    [0.6, 0.0, 0.4, 0.0, 0.0, 0.0],
    [0.2, 0.4, 0.0, 0.4, 0.0, 0.0],
    [0.0, 0.0, 0.4, 0.0, 0.4, 0.2],
    [0.2, 0.0, 0.0, 0.4, 0.0, 0.4],
    [0.0, 0.0, 0.0, 0.2, 0.4, 0.4],
])
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print """
Usage: promenade_scarabees fichier_graphe nb_scarabees
"""

    verifier_matrice(exemple)
