#!/usr/bin/python2
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

"""
Fonction utilisée par la fonction simplexe, elle ne devrait pas être appelée
directement.
La matrice d'entrée doit avoir la forme suivante :
    Les premières colonnes correspondent aux produits :
    [bénéfice du produit, cout en ressource 1, cout en ressource 2, ...]
    (ce sont les variables libres)

    Les dernières colonnes correspondent aux variables de base :
    [0, ..., 0, 1, 0, ..., 0]
    sachant que le carré des variables de base forme une matrice identité.

    Et sur la toute dernière colonne :
    [0, stock en ressource 1, stock en ressource 2, ...]

Attention: la matrice doit être une matrice flottante pour numpy !
Càd déclarée avec np.array([...], dtype='f')

Retourne un triplet de la forme (gain, [a_produire...], [restes...]) où :
    - a_produire[n] est la quantité de produit n à produire;
    - restes[m]     est ce qu'il reste en ressource m.
"""

def simplexe_aux(matrice):
    size_y, size_x = matrice.shape

    # variables de base
    base = list(range(size_x-1-(size_y-1), size_x-1))

    # indice de colonne (pour le x à ajouter de la base)
    a_ajouter = np.argmax(matrice[0,])
    while matrice[0,a_ajouter] > 0:
        # indice de ligne (pour le x à retirer de la base)
        a_retirer = None
        meilleur_ratio = 0

        # la première ligne est pour z, on n'y cherche pas le ratio
        for y in range(1, size_y):
            if matrice[y,a_ajouter] == 0: #todo: comp float ?
                continue
            ratio = matrice[y,-1] / matrice[y,a_ajouter]
            if a_retirer is None or ratio < meilleur_ratio:
                a_retirer = y
                meilleur_ratio = ratio

        base[a_retirer-1] = a_ajouter

        # opérations sur les lignes
        for y in range(size_y):
            if y == a_retirer:
                matrice[y,] /= matrice[y,a_ajouter]
            else:
                ratio = matrice[y,a_ajouter] / matrice[a_retirer, a_ajouter]
                matrice[y,] -= ratio * matrice[a_retirer,]

        a_ajouter = np.argmax(matrice[0,])

    # recherche des quantités à produire (au début de la liste)
    # et des restes (à la fin)
    a_produire_et_restes = [0]*(size_x-1)
    for n in range(len(base)):
        a_produire_et_restes[base[n]] = matrice[n+1,-1]

    return -matrice[0,-1],                         \
           a_produire_et_restes[0:size_x-size_y],  \
           a_produire_et_restes[size_x-size_y:-1]


def simplexe(contraintes, profit):
    """
    Cette fonction prend en entrée la matrice contenant les
    inéquations définissant le problème, telle que définie dans le
    slide 3 des séances 2 et 3. Elle prend également la fonction
    profit, les variables devant être dans le même ordre que dans
    l'autre matrice.
    Les contraintes sont sous la forme "ax1 + bx2 + ... <= stock"
    Elle transforme cette matrice en une matrice utilisable par la
    fonction simplexe_aux.
    """

    nb_mat, nb_pdt = contraintes.shape
    nb_pdt -= 1 # Contraintes contient également les stocks

    m = np.array([[0] * (nb_pdt + nb_mat + 1)] * (nb_mat + 1), dtype='f')

    # Ajout du profit
    m[0,] = profit + [0] * (nb_mat + 1)

    for i in range(nb_mat):
        # Ajout des contraintes sur les variables libres
        m[i+1,:nb_pdt] = contraintes[i,:nb_pdt]
        # Ajout des variables de base
        m[i+1,nb_pdt+i] = 1

    # Ajout des stocks
    m[1:,-1] = contraintes[:,-1]

    return simplexe_aux(m)

if __name__ == '__main__':
    np.set_printoptions(precision=2, suppress=True)

    m = np.array([
        [7, 9, 18, 17, 0, 0, 0, 0],
        [2, 4, 5, 7,   1, 0, 0, 42],
        [1, 1, 2, 2,   0, 1, 0, 17],
        [1, 2, 3, 3,   0, 0, 1, 24]
    ], dtype='f')
    direct = simplexe_aux(m)
    print(direct)

    contraintes = np.array([[2,4,5,7,42],[1,1,2,2,17],[1,2,3,3,24]])
    profit = [7,9,18,17]
    assert(direct == simplexe(contraintes, profit))

    print("==============")

    m = np.array([
      [5, 8, 0, 0, 0],
      [5, 2, 1, 0, 42],
      [4, 7, 0, 1, 26]], dtype='f')
    print(simplexe_aux(m))

