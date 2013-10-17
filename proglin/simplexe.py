#!/usr/bin/python2
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

"""
La matrice d'entrée doit avoir la forme suivante :

À chaque colonne correspond un produit :
[benef_du_produit, cout_ressource_1, cout_ressource_2, ...]
(c'est les variables libres)

Sur les dernières colonnes, on a les variables de base :
[0, 0, ..., 0, 1, 0, ..., 0]
sachant que le carré des variables de base forme une matrice identité.

Et sur la toute dernière colonne :
[0, stock_ressource_1, stock_ressource_2, ...]

Attention: la matrice doit être une matrice flotante pour numpy !
Càd déclarée avec np.array([...], dtype='f')
"""

def simplexe(matrice, base=None):
    #print(matrice)
    size_y, size_x = matrice.shape

    if base==None:
      base = range(size_x-1-(size_y-1), size_x-1)
      #print(base)

    # indice de colonne (pour le x à virer de la base)
    a_virer = np.argmax(matrice[0,])
    if matrice[0,a_virer] <= 0:
        return -matrice[0,-1]

    # indice de ligne (pour le x à ajouter dans la base)
    a_ajouter = None
    meilleur_ratio = 0
    for y in range(1, size_y): # la première ligne est pour z, osef
        if matrice[y,a_virer] == 0: #todo: comp float ?
            continue
        ratio = matrice[y,-1] / matrice[y,a_virer]
        if a_ajouter is None or ratio < meilleur_ratio:
            a_ajouter = y
            meilleur_ratio = ratio

    print(a_virer, a_ajouter)
    for i in range(len(base)):
        if base[i] == a_ajouter+1:
            base[i] = a_virer
            break

    print(base)
    # opérations sur les lignes
    for y in range(size_y):
        if y == a_ajouter:
            matrice[y,] /= matrice[y,a_virer]
        else:
            ratio = matrice[y,a_virer] / matrice[a_ajouter, a_virer]
            matrice[y,] -= ratio * matrice[a_ajouter,]

    return simplexe(matrice, base)

if __name__ == '__main__':
    np.set_printoptions(precision=2)
    m = np.array([
        [7, 9, 18, 17, 0, 0, 0, 0],
        [2, 4, 5, 7,   1, 0, 0, 42],
        [1, 1, 2, 2,   0, 1, 0, 17],
        [1, 2, 3, 3,   0, 0, 1, 24]
    ], dtype='f')
    print(simplexe(m))

    print("==============")
    m = np.array([
      [5, 8, 0, 0, 0],
      [5, 2, 1, 0, 42],
      [4, 7, 0, 1, 26]], dtype='f')
    print(simplexe(m))

