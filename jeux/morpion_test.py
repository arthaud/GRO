#!/usr/bin/python2
# -*- coding: utf-8 -*-

import morpion_strategies
import sys

def get_strategies():
    """
    Retourne toutes les stratégies disponibles, à l'exception de la stratégie humaine
    """
    return map(lambda f : getattr(morpion_strategies, f),filter(lambda f : f.startswith("strat") and f != 'strat_humain', dir(morpion_strategies)))

if __name__ == '__main__':
    strats = get_strategies()
    file = open(sys.argv[1], 'w')
    
    for i, strat in enumerate(strats):
        for opponent in strats[i:]:
            pass
