# link : https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

t = int(input())

for i in range(t):
    n = int(input())
    s = 1
    for j in range(1, n+1):
        if j % 2 == 0:
            s += 1
        else:
            s *= 2
    print(s)
