#!/usr/bin/python2
# -*- coding: utf-8 -*-

def read_msp(path):
    """
    Read an MSP file such as those on:
        http://www.numerical.rl.ac.uk/cute/netlib.html
    File specification can be found there:
        http://lpsolve.sourceforge.net/5.5/mps-format.htm
    """

    with open(path) as f:
        # File parsing:
        line = None
        while line != "ROWS\n":
            line = f.readline()

        ineqs = {}
        line = f.readline()
        while line != "COLUMNS\n":
            line = line.split()
            if(line[0] == 'E'): #todo
                ineqs.setdefault(line[1], 'L')
            else:
                ineqs.setdefault(line[1], line[0])

            line = f.readline()

        coefs = {}
        line = f.readline()
        while line != "RHS\n":
            line = line.split()

            coefs.setdefault(line[0], []).append((line[1], float(line[2])))
            if len(line) == 5:
                coefs[line[0]].append((line[3], float(line[4])))

            line = f.readline()

        rhs = {}
        line = f.readline()
        while line != "BOUNDS\n" and line != "ENDATA\n":
            line = line.split()

            rhs.setdefault(line[0], []).append((line[1], float(line[2])))
            if len(line) == 5:
                rhs[line[0]].append((line[3], float(line[4])))

            line = f.readline()

        assert(len(rhs) == 1) # don't know what to do when there are multiple values
        rhs = next(iter(rhs.values())) # so keep only the first

        bounds = {}
        if line != "ENDATA\n":
            line = f.readline()

        while line != "ENDATA\n":
            line = line.split()
            bounds.setdefault(line[1], []).append((line[0], line[2], float(line[3])))
            line = f.readline()

        assert(len(bounds) <= 1) # don't know what to do when there are multiple values
        bounds = []
        if len(bounds) == 1:
            bounds = next(iter(bounds.values())) # so keep only the first

        # Now we have:
        #     ineqs:   a dictionary {"equation name": "equation type (L, E or G)"}
        #     coefs:   a dictionary {"variable name": **}
        #              where ** is a list of ("equation name", float(corr. coeficient))
        #              it may not contain the variable coeficient for all equation,
        #              in such case, it is 0
        #     rhs:     right hand side values of the inequations
        #     bounds:  list [("type", "variable", float(value))]
        #              where type is "UP" or "LO"
        #              means that variable <= value or >=

        # Matrix construction:
        constraints = [0 for i in range(len(coefs))]
        matrix = parameters=[[0 for i in range(len(coefs)+1)] for j in range(len(ineqs)-1)]

        current_line = 0
        var_col = {}
        eq_line = {}
        var_c = 0
        for c in coefs:
            var_col.setdefault(c, var_c)
            for e in coefs[c]:
                type = ineqs[e[0]]
                if type == 'N':
                    constraints[var_c] = e[1]
                    continue

                if e[0] not in eq_line:
                    eq_line.setdefault(e[0], current_line)
                    current_line += 1

                if type == 'L':
                    matrix[eq_line[e[0]]][var_c] =  e[1]
                elif type == 'G':
                    matrix[eq_line[e[0]]][var_c] = -e[1]
                else:
                    pass # todo case == 'E'

            var_c += 1

        for r in rhs:
            if ineqs[r[0]] == 'L':
                matrix[eq_line[r[0]]][-1] =  r[1]
            elif ineqs[r[0]] == 'G':
                matrix[eq_line[r[0]]][-1] = -r[1]
            else:
                pass # todo : case == 'E'

        for b in bounds:
            begin0 = [0] * var_col[b[1]]
            end0   = [0] * (len(var_col)-var_col[b[1]]-1)

            if b[0] == 'UP':
                matrix.append(begin0 + [1] + end0 + [ b[2]])
            else:
                matrix.append(begin0 + [1] + end0 + [-b[2]])

        return constraints, matrix, var_col, eq_line, ineqs, coefs, rhs, bounds

if __name__ == '__main__':
    import simplexe as s
    import numpy as np

    # la fonction construit correctement la matrice,
    # mais aucun exemple ne marche

    """
    sol = read_msp("tests/simple.msp")
    print(sol)
    print(s.simplexe(np.array(sol[1]), sol[0]))
    """

    """
    sol = read_msp("tests/AFIRO.SIF")
    s.simplexe(np.array(sol[1]), sol[0])
    """

    """
    sol = read_msp("tests/25FV47.SIF")
    s.simplexe(np.array(sol[1]), sol[0])
    """

    """
    sol = read_msp("tests/BOEING2_ineq.SIF")
    print(s.simplexe(np.array(sol[1]), sol[0]))
    """
