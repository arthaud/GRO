#!/usr/bin/python2
# -*- coding: utf-8 -*-

def carre_magique(n):
    '''
    Retourne un carré magique d'ordre n
    '''
    if n % 2 == 0:
        return carre_magique_pair(n)
    else:
        return carre_magique_impair(n)

def carre_magique_impair(n):
    m = n // 2
    matrice = [[None] * n for _ in range(n)]

    i = 1
    for x in range(n-1, -1, -1):
        y = n - x - 1
        for j in range(n):
            if x+j < n // 2:
                matrice[x+j+n-m][y+j-m] = i
            elif x+j >= n + n // 2:
                matrice[x+j-n-m][y+j-m] = i
            elif y+j < n // 2:
                matrice[x+j-m][y+j+n-m] = i
            elif y+j >= n + n // 2:
                matrice[x+j-m][y+j-n-m] = i
            else:
                matrice[x+j-m][y+j-m] = i

            i += 1

    return matrice
