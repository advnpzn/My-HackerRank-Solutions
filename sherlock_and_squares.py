# link : https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

def squares(a, b):
    res = 0
    if a == b:
        e = int(math.sqrt(a))
        if e*e == a :
            return 1
    c = math.floor(a ** .5)
    d = math.ceil(b ** .5)
    
    if c != d:
        res = abs(c - d) - 1
    
    if c*c == a:
        res += 1
    if d*d == b:
        res+= 1
    return res
