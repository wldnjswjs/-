import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for _ in range(m):
    x = list(map(int, input().split()))
    if x[0] not in dic:
        dic[x[0]] = [x[1], x[2]]
        print('YES')
    else:
        if dic[x[0]][1] > x[1]:
            print('NO')
        else:
            dic[x[0]] = [x[1], x[2]]
            print('YES')
