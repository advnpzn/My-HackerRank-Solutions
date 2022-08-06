# link : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

tup = tuple(map(int, input().split()))

print(numpy.zeroes(tup, int))
print(numpy.ones(tup, int))
