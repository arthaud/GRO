#!/usr/bin/python2
# -*- coding: utf-8 -*-

import morpion_strategies
import sys
import datetime

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

def match(taille, strategies, display=False):
    morpion = [[None] * taille for i in range(taille)]
    joueur_courant = False
    vainqueur = None
    temps = ([], []) # liste des temps mis pour jouer un coup
    
    while vainqueur is None and not morpion_strategies.jeu_complet(morpion):
        debut = datetime.datetime.now()
        x, y = strategies[joueur_courant](morpion, joueur_courant)
        fin = datetime.datetime.now() - debut
        temps[joueur_courant].append(fin.seconds + fin.microseconds/float(1000000))
        assert morpion[x][y] is None, 'Tricheur !'
        morpion[x][y] = joueur_courant
        joueur_courant = not joueur_courant
        vainqueur = gagnant(morpion)
        if display:
            pprint(morpion)
            print ''
        
    return vainqueur, temps

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

    vainqueur, _ = match(taille, strategies, display=True)
    
    print "--------------------"
    if vainqueur == None:
        print "Pas de gagnant ! bande de noobs"
    else:
        print "Le gagnant est le joueur %s (joueur %s)." % (strategies[vainqueur].__name__[6:], int(vainqueur) + 1)
