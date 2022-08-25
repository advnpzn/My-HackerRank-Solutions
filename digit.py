t = int(input())
for i in range(t):
    count = []
    n = int(input())
    temp = n
    while temp > 0:
        rem = temp % 10
        if rem != 0:
            count.append(rem)
        temp = temp // 10
    print(len([i for i in count if n % i == 0]))
