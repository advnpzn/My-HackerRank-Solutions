# link : https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

arr = sorted([int(_) for _ in input().split()])
print("{} {}".format(sum(arr[:len(arr)-1]), sum(arr[1:])))
