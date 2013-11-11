#!/usr/bin/python2
# -*- coding: utf-8 -*-
from copy import deepcopy
from random import choice
from morpion_minmax import minmax as c_minmax # Pensez à faire un make !

INFINI = 10**6

def jeu_complet(morpion):
    taille = len(morpion)
    for i in range(taille):
        for j in range(taille):
            if morpion[i][j] is None:
                return False
    return True

def evaluation(morpion, joueur):
    '''
    Retourne l'évaluation d'une position du point de vue du joueur
    '''
    adversaire = not joueur
    n = len(morpion)
    score = 0

    lignes = morpion[:] # lignes
    lignes += [[morpion[i][j] for i in range(n)] for j in range(n)] # colonnes
    lignes.append([morpion[i][i] for i in range(n)]) # première diagonale
    lignes.append([morpion[n-i-1][i] for i in range(n)]) # deuxième diagonale

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

def minmax(morpion, joueur, profondeur_max, eval_fn, elagage=True, noeud_joueur=True, alpha_beta=None):
    '''
    Retourne le couple (c, e) avec :
    * c le coup (x,y) optimal à jouer
    * e l'évaluation maximale atteignable par l'algorithme du min max, avec une profondeur maximale profondeur_max.

    morpion est l'état actuel du morpion ;
    joueur indique notre joueur (True ou False) ;
    eval_fn est la fonction d'évaluation ;
    elagage indique s'il faut appliquer l'élagage alpha-beta.

    noeud_joueur et alpha_beta sont des paramètres utiles uniquement lors des appels récursifs :
    * noeud_joueur vaut true si on doit prendre le max, sinon on doit prendre le min.
    * alpha_beta est soit alpha, soit beta, en fonction de noeud_joueur
    '''
    if profondeur_max == 0 or jeu_complet(morpion):
        return (None, eval_fn(morpion, joueur))

    evaluation = eval_fn(morpion, joueur)
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
                fils[x][y] = joueur if noeud_joueur else not joueur
                coup, evaluation = minmax(fils, joueur, profondeur_max - 1, eval_fn, elagage, not noeud_joueur, evaluation_optimale)

                if evaluation_optimale is None:
                    evaluation_optimale = evaluation
                    coup_optimal = (x,y)
                elif comp(evaluation, evaluation_optimale):
                    evaluation_optimale = evaluation
                    coup_optimal = (x, y)

                if elagage and alpha_beta is not None:
                    if noeud_joueur and evaluation_optimale >= alpha_beta:
                        return coup_optimal, evaluation_optimale
                    elif not noeud_joueur and evaluation_optimale <= alpha_beta:
                        return coup_optimal, evaluation_optimale

    return coup_optimal, evaluation_optimale

def coups_possibles(morpion):
    coups_possibles = []
    taille = len(morpion)
    for i in range(taille):
        for j in range(taille):
            if morpion[i][j] is None:
                coups_possibles.append((i,j))
    return coups_possibles
                
def strat_minmax_2(morpion, joueur):
    return minmax(morpion, joueur, 2, evaluation, False)[0]

def strat_minmax_4(morpion, joueur):
    return minmax(morpion, joueur, 4, evaluation, False)[0]

def strat_minmax_6(morpion, joueur):
    return minmax(morpion, joueur, 6, evaluation, False)[0]

def strat_minmax_8(morpion, joueur):
    return minmax(morpion, joueur, 8, evaluation, False)[0]

def strat_minmax_10(morpion, joueur):
    return minmax(morpion, joueur, 10, evaluation, False)[0]

def strat_minmax_elagage2(morpion, joueur):
    return minmax(morpion, joueur, 2, evaluation, True)[0]

def strat_minmax_elagage4(morpion, joueur):
    return minmax(morpion, joueur, 4, evaluation, True)[0]

def strat_minmax_elagage6(morpion, joueur):
    return minmax(morpion, joueur, 6, evaluation, True)[0]

def strat_minmax_elagage8(morpion, joueur):
    return minmax(morpion, joueur, 8, evaluation, True)[0]

def strat_minmax_elagage10(morpion, joueur):
    return minmax(morpion, joueur, 10, evaluation, True)[0]

def strat_c_minmax_2(morpion, joueur):
    return c_minmax(morpion, joueur, 2, False)[0]

def strat_c_minmax_4(morpion, joueur):
    return c_minmax(morpion, joueur, 4, False)[0]

def strat_c_minmax_6(morpion, joueur):
    return c_minmax(morpion, joueur, 6, False)[0]

def strat_c_minmax_8(morpion, joueur):
    return c_minmax(morpion, joueur, 8, False)[0]

def strat_c_minmax_10(morpion, joueur):
    return c_minmax(morpion, joueur, 10, False)[0]

def strat_c_minmax_elagage2(morpion, joueur):
    return c_minmax(morpion, joueur, 2, True)[0]

def strat_c_minmax_elagage4(morpion, joueur):
    return c_minmax(morpion, joueur, 4, True)[0]

def strat_c_minmax_elagage6(morpion, joueur):
    return c_minmax(morpion, joueur, 6, True)[0]

def strat_c_minmax_elagage8(morpion, joueur):
    return c_minmax(morpion, joueur, 8, True)[0]

def strat_c_minmax_elagage10(morpion, joueur):
    return c_minmax(morpion, joueur, 10, True)[0]

def strat_aleatoire(morpion, joueur):
    return choice(coups_possibles(morpion))

def strat_premier_dispo(morpion, joueur):
    return coups_possibles(morpion)[0]

def strat_humain(morpion, joueur):
    return input()
