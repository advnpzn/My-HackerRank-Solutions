# link : https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true

def permutationEquation(p):
    res = []
    for i in range(1, len(p) + 1):
        res.append(p.index(p.index(i) + 1) + 1)
    return res
