#!/usr/bin/python2
# -*- coding: utf-8 -*-

import datetime
import sacados

if __name__ == '__main__':
    sad = ["tests/50.in", "tests/500.in", "tests/5000.in", "tests/50000.in"]

    for p in sad:
        obj = sacados.read_testfile(p)
        start = datetime.datetime.now()
        print(sacados.sacados(obj, 10))
        print(sacados.sacados(obj, 100))
        print(sacados.sacados(obj, 500))
        exec_time = (datetime.datetime.now() - start)/3
        print("Tested %s in %s" % (p, exec_time))

