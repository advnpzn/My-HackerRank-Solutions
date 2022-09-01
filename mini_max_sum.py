# link : https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

arr = sorted(map(int, input().split()))
print(f"{sum(arr)-arr[len(arr)-1]} {sum(arr)-arr[0]}")
