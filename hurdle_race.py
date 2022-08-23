# link : https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true

n, k = map(int, input().split())
h = set([int(_) for _ in input().split()])
d = 0
for i in h:
    if i < k + d:
        continue
    else:
        while k + d < i:
            d += 1
print(d)


# Another method.

n, k = map(int, input().split())
h = set([int(_) for _ in input().split()])
print(0 if max(h) < k else max(h) - k)
