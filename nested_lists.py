# link : https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

res = []
scores = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        res += [[name, score]]
        scores += [score]
        
    sec_low = sorted(list(set(scores)))[1]
    
    for a, b in sorted(res):
        if b == sec_low:
            print(a)
