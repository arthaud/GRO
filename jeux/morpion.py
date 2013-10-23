#!/usr/bin/python2
# -*- coding: utf-8 -*-
from copy import deepcopy 

INFINI = 10**6

def evaluation(morpion, joueur):
    '''
    Retourne l'évaluation d'une position du point de vue du joueur
    '''
    adversaire = not joueur
    n = len(morpion)
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

def minmax(morpion, noeud_joueur, profondeur_max, eval_fn):
    '''
    Retourne le couple (c, e) avec :
    * c le coup (x,y) optimal à jouer
    * e l'évaluation maximale atteignable par l'algorithme du min max, avec une profondeur maximale profondeur_max.

    noeud_joueur vaut true si on doit prendre le max, sinon on doit prendre le min.
    eval_fn est la fonction d'évaluation
    '''
    if profondeur_max == 0:
        return (None, eval_fn(morpion, noeud_joueur))

    evaluation = eval_fn(morpion, not noeud_joueur)
    if abs(evaluation) == INFINI:
        return (None, evaluation)

    n = len(morpion)
    evaluation_optimale = None
    coup_optimal = None
    comp = (lambda x,y: x>y) if noeud_joueur else (lambda x,y: x<y)

    for x in range(n):
        for y in range(n):
            if morpion[x][y] is None:
                fils = deepcopy(morpion)
                fils[x][y] = noeud_joueur
                coup, evaluation = minmax(fils, not noeud_joueur, profondeur_max - 1, eval_fn)

                if evaluation_optimale is None:
                    evaluation_optimale = evaluation
                    coup_optimal = (x,y)
                elif comp(evaluation, evaluation_optimale):
                    evaluation_optimale = evaluation
                    coup_optimal = (x, y)

    return coup_optimal, evaluation_optimale
