#!/usr/bin/python2
# -*- coding: utf-8 -*-

def simplexe(stock, costs, benefits):
    '''
    Retourne la liste [x1, x2, .., xn] tel que le benefice soit maximal.

    stock est une liste de ressources disponibles
    costs est une matrice. costs[i][j] représente le cout en ressource j pour le produit i
    benefits est la liste des benefices pour chaque produit

    Attention: stock, costs et benefits seront modifiés.
    '''
    n = len(stock)
    m = len(costs)

    # Ajout des variables « restes »
    for i in range(n):
        costs.append([int(i == j) for j in range(n)])

    benefits += [0 for _ in range(n)]
    solution = [0 for _ in range(m)] + stock

    # TODO : vérifier que l'origine est un sommet de départ admissible

    while True:
        # Recherche du produit le plus rentable
        index_max_benef = max(range(m + n), key=lambda i: benefits[i])
        max_benef = benefits[index_max_benef]

        if max_benef <= 0:
            return solution

        # Quantité maximale que l'on peut prendre
        indexes_costs_not_zero = filter(lambda i: costs[index_max_benef][i] > 0, range(n))
        index_limiting = min(indexes_costs_not_zero, key=lambda i: stock[i] / costs[index_max_benef][i])
        taken_quantity = stock[index_limiting] / costs[index_max_benef][index_limiting]

        solution[index_max_benef] += taken_quantity

if __name__ == '__main__':
    print '------- Exemple du TP ---------------'
    stock = [42, 17, 24]
    costs = [
        [2, 1, 1],
        [4, 1, 2],
        [5, 2, 3],
        [7, 2, 3],
    ]
    benefits = [7, 9, 18, 17]
    print simplexe(stock, costs, benefits)

    print '------- Exemple qui fait planter -----------'
    stock = [42, 26]
    costs = [
        [5, 4],
        [2, 7],
    ]
    benefits = [5, 8]
    print simplexe(stock, costs, benefits)
