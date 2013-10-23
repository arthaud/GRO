#!/usr/bin/python2
# -*- coding: utf-8 -*-

INFINI = 10**6

def evaluation(morpion, joueur):
    '''
    Retourne l'évaluation d'une position du point de vue du joueur
    '''
    adversaire = not joueur
    n = len(morpion[0])
    score = 0

    lignes = morpion[:]
    lignes += [[morpion[i][j] for i in range(n)] for j in range(n)]
    lignes.append([morpion[i][i] for i in range(n)])
    lignes.append([morpion[n-i-1][i] for i in range(n)])

    for ligne in lignes:
        if ligne == [joueur] * n:
            return INFINI
        if ligne == [not joueur] * n:
            return -INFINI

        if adversaire not in ligne:
            score += len(list(filter(lambda i:i == joueur, ligne)))

        if joueur not in ligne:
            score -= len(list(filter(lambda i:i == adversaire, ligne)))

    return score

def minmax(morpion, noeud_joueur, profondeur_max):
    '''
    Retourne l'évaluation maximale atteignable par l'algorithme du min max,
    avec une profondeur maximale profondeur_max.
    '''
    if profondeur_max == 0:
        return evaluation(morpion, noeud_joueur)

