# link : https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true

rd = list(map(int, input().split()))
dd = list(map(int, input().split()))
if rd[2] > dd[2]:
    print(10000)
elif rd[2] == dd[2]:
    if rd[1] > dd[1]:
        print(500 * (abs(dd[1] - rd[1])))
    elif rd[1] == dd[1]:
        if dd[0] < rd[0]:
            print(15 * abs(rd[0] - dd[0]))
        elif rd[0] < dd[0]:
                print(0)
        else:
            print(0)    
    else:
        print(0)
else:
      print(0)          
