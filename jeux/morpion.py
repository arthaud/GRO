#!/usr/bin/python2
# -*- coding: utf-8 -*-

import morpion_strategies
import sys

def gagnant(morpion):
    taille = len(morpion)
    
    lignes = morpion[:] # lignes
    lignes += [[morpion[i][j] for i in range(taille)] for j in range(taille)] # colonnes
    lignes.append([morpion[i][i] for i in range(taille)]) # première diagonale
    lignes.append([morpion[taille-i-1][i] for i in range(taille)]) # deuxième diagonale

    for ligne in lignes:
        if ligne[0] is not None and ligne == [ligne[0]] * taille:
            return ligne[0]
    
    return None

def jeu_complet(morpion):
    taille = len(morpion)
    for i in range(taille):
        for j in range(taille):
            if morpion[i][j] is None:
                return False
    return True

def pprint(morpion):
    taille = len(morpion)

    print '+' + ('-' * 3 + '+') * taille

    def print_case(case):
        if case is None:
            return ' '
        elif case:
            return 'T'
        else:
            return 'F'

    for line in morpion:
        print '|' + '|'.join(map(lambda c: ' ' + print_case(c) + ' ', line)) + '|'
        print '+' + ('-' * 3 + '+') * taille

if __name__ == "__main__":
    try:
        taille = int(sys.argv[1])
        strategies = (getattr(morpion_strategies, "strat_" + sys.argv[2]),
                      getattr(morpion_strategies, "strat_" + sys.argv[3])
                      )
    except(AttributeError, IndexError):
        print """
Arguments non reconnus
Usage : ./morpion.py <taille> <strat1> <strat2>
voir le fichier morpion_strategies.py pour la liste des stratégies disponibles
"""
        exit(1)

    morpion = [[None] * taille for i in range(taille)]
    joueur_courant = False
    vainqueur = None
    
    while vainqueur is None and not jeu_complet(morpion):
        x, y = strategies[joueur_courant](morpion, joueur_courant)
        assert morpion[x][y] is None, 'tricheur !'
        morpion[x][y] = joueur_courant
        joueur_courant = not joueur_courant
        vainqueur = gagnant(morpion)
        pprint(morpion)
        print ''

    print "--------------------"
    if vainqueur == None:
        print "Pas de gagnant ! bande de noobs"
    else:
        print "Le gagnant est le joueur %s (joueur %s)." % (strategies[vainqueur].__name__[6:], int(vainqueur) + 1)

    
