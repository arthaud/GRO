#!/usr/bin/python2
# -*- coding: utf-8 -*-
import morpion_strategies
import argparse
from datetime import datetime

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
    '''
    Joue un match de morpion.

    Retourne le couple (v, t) avec v le vainqueur et t la liste des temps mis pour jouer un coup
    '''
    morpion = [[None] * taille for i in range(taille)]
    joueur_courant = False
    vainqueur = None
    temps = [], [] # liste des temps mis pour jouer un coup

    while vainqueur is None and not morpion_strategies.jeu_complet(morpion):
        debut = datetime.now()
        x, y = strategies[joueur_courant](morpion, joueur_courant)
        fin = datetime.now() - debut
        temps[joueur_courant].append(fin.total_seconds())

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
    parser = argparse.ArgumentParser(description='Jouer au jeu du morpion')
    parser.add_argument('n', type=int)
    parser.add_argument('strategie1')
    parser.add_argument('strategie2')

    args = parser.parse_args()

    try:
        strat1 = getattr(morpion_strategies, 'strat_' + args.strategie1)
    except AttributeError:
        parser.print_usage()
        print "error: la stratégie \"%s\" n'existe pas" % args.strategie1
        exit(0)

    try:
        strat2 = getattr(morpion_strategies, 'strat_' + args.strategie2)
    except AttributeError:
        parser.print_usage()
        print "error: la stratégie \"%s\" n'existe pas" % args.strategie2
        exit(0)

    strategies = strat1, strat2
    vainqueur, _ = match(args.n, strategies, display=True)
    
    print "--------------------"
    if vainqueur is None:
        print "Pas de gagnant ! bande de noobs"
    else:
        print "Le gagnant est le joueur %s (joueur %s)." % (strategies[vainqueur].__name__[6:], int(vainqueur) + 1)
