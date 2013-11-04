#!/usr/bin/python2
# -*- coding: utf-8 -*-

import datetime
import knapsack as sad

def test_sad(obj, file_name, max_mass):
    start = datetime.datetime.now()
    best = sad.knapsack(obj, max_mass)
    exec_time = datetime.datetime.now() - start
    print("Tested %s with max_mass=%s in %s" % (file_name, max_mass, exec_time))
    print("    optimum:    %s" % best)
    r = sad.greedy(obj, max_mass, sad.best_price)
    print("    best price: %s / %.1f%%" % (r, 100.*(best-r)/best))
    r = sad.greedy(obj, max_mass, sad.worst_mass)
    print("    worst mass:  %s / %.1f%%" % (r, 100.*(best-r)/best))
    r = sad.greedy(obj, max_mass, sad.best_ratio)
    print("    best ratio: %s / %.1f%%" % (r, 100.*(best-r)/best))

if __name__ == '__main__':
    sad_files = [
            "tests/50,25,1,1,1000.in",
            "tests/500,25,1,1,1000.in",
            "tests/5000,25,1,1,1000.in",
            "tests/5000,300,1,1,1000.in",
            "tests/50000,25,1,1,1000.in",
            "tests/50000,300,1,1,1000.in",
            "tests/50000,1000,1,1,1000.in",
            "tests/50000,5000,1,1,1000.in"
    ]

    for p in sad_files:
        obj = sad.read_testfile(p)
        test_sad(obj[:], p, 20)
        test_sad(obj[:], p, 100)
        test_sad(obj[:], p, 500)
        print("")
