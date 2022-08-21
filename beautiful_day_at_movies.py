#link : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

def rev(n):
    rem = 0
    r = 0
    while (n > 0):
        rem = n % 10
        r = r * 10 + rem
        n = n // 10
    return r

def beautifulDays(i, j, k):
    # Write your code here
    b = 0
    for d in range(i, j+1):
        if (abs(d - rev(d)) % k == 0):
            b += 1
    return b
