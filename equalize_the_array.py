# link : https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

n = int(input())
arr = [int(_) for _ in input().split()]

def most(arr):
    c = 0
    for i in set(arr):
        cc = 0
        for j in arr:
            cc = cc + 1 if i == j else cc + 0
        if cc >= c:
            c = cc
    return c

m = most(arr)

print(len(arr) - m)
