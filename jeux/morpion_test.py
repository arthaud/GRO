#!/usr/bin/python2
# -*- coding: utf-8 -*-

import morpion_strategies

def get_strategies():
    return filter(lambda f : f.startswith("strat") and f != 'strat_humain', dir(morpion_strategies))

print get_strategies()
