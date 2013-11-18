#!/usr/bin/python2
# -*- coding: utf-8 -*-
import numpy
import argparse

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
    parser = argparse.ArgumentParser(description='Promenade des petits scarabées')
    parser.add_argument('graphe_file')
    parser.add_argument('nb_scarabees', type=int)

    args = parser.parse_args()
    verifier_matrice(exemple)
