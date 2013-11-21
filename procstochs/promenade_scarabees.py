#!/usr/bin/python2
# -*- coding: utf-8 -*-
import numpy
import argparse
from random import random, randrange
import sys

class Graphe:
    def __init__(self, fichier):
        self.sommets = []
        self.scarabees = []
        for sommet in open(fichier, 'r').readlines():
            self.sommets.append([int(i) for i in sommet.split(' ')])

    def __repr__(self):
        print """
TODO: Graphe.__repr__
Cette fonction devra retourner la représentation du graphe au format dot, en colorant d'une couleur différente les points où un scarabée est stationné, et d'une couleur plus visible les points où plusieurs scarabées sont présents.
"""
        return null

class Scarabee:
    def __init__(self, graphe, fichier_probas):
        self.graphe = graphe
        self.probas = []
        self.position = randrange(len(graphe.sommets))

        for ligne in open(fichier_probas, 'r').readlines():
            self.probas.append([float(i) for i in ligne.split(' ')])

        assert len(self.probas) == len(graphe.sommets), 'La matrice de probabilité ne correspond pas au graphe !'
        self.probas = numpy.array(self.probas)
        verifier_matrice(self.probas)

    def __repr__(self):
        return generer_dot(self.probas)

def promenade(graphe, nb_iterations):
    for _ in range(nb_iterations):
        for s in graphe.scarabees:
            probas = [sum(s.probas[s.position][:i+1]) for i in range(len(s.probas))]
            destin = random()
            for i, p in enumerate(probas):
                if destin < p:
                    s.position = i
                    break

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

def proba_rencontre(scarabees, tour):
    '''
    scarabees est une liste de couple (position, matrice) qui représente chaque scarabée
    Retourne une matrice ligne où chaque case contient la probabilité que les scarabées se rencontrent à cette position
    '''
    assert len(scarabees) >= 2
    n = scarabees[0][1].shape[0]
    probas = numpy.array([1.0 for _ in range(n)])

    for (pos, matrice) in scarabees:
        probas *= position_proba(matrice, pos, tour)

    return probas

def temps_moyen(scarabees_matrices, pos_initiale, epsilon=10e-6):
    '''
    scarabees_matrices est la liste des matrices de probabilités pour chaque scarabée
    epsilon est la précision voulue sur la valeur de retour
    '''
    scarabees = [(pos_initiale, m) for m in scarabees_matrices]
    k = 1
    proba = U_k = V_k = sum(proba_rencontre(scarabees, 1))

    while True:
        k = k + 1
        tmp = sum(proba_rencontre(scarabees, k))
        V_k *= (1.0 - U_k) / U_k * tmp
        U_k = tmp

        proba += k * V_k
        if k * V_k < epsilon:
            break

    return proba

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Promenade des petits scarabées')
    parser.add_argument('fichier_graphe')
    parser.add_argument('fichier_proba', nargs='+')

    args = parser.parse_args()

    g = Graphe(args.fichier_graphe)
    scarabees = []
    for scarabee in args.fichier_proba:
        scarabees.append(Scarabee(g, scarabee))
    g.scarabees = scarabees
    promenade(g, 10)
