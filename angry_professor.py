#link : https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

def angryProfessor(k, a):
    return "NO" if (len([i for i in a if i <= 0]) >= k) else "YES"
