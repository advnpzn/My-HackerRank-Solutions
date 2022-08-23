# link : https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

from math import floor

like = 0
shared = 5
for i in range(int(input())):
    shared = floor(shared / 2)
    like += shared
    shared = shared * 3
print(like)
