import sys
input = sys.stdin.readline

n = int(input())
count = 0
c = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while c != n:
        if c >= n-c:
            c += n-c
            count += 1
        else:
            c += c
            count += 1

    print(count+1)