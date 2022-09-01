# link : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true

n = int(input())
c = [int(_) for _ in input().split()]
s = 0
curr_index = 0
while curr_index != len(c) -1:
    if curr_index == len(c) - 2:
        if c[curr_index + 1] == 0:
            s += 1
            break
        else:
            break
    if c[curr_index + 1] == 0 and c[curr_index + 2] == 0:
        curr_index += 2
        s += 1
    elif c[curr_index + 1] == 0 and c[curr_index + 2] != 0:
        curr_index += 1
        s += 1
    elif c[curr_index + 1] != 0 and c[curr_index + 2] == 0:
        curr_index += 2
        s += 1
print(s)
        
