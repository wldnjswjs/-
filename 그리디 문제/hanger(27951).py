n = int(input())
hanger = list(map(int,input().split()))
u, d = map(int,input().split())
ans = []
sign = 0

for i in range(len(hanger)):
    if hanger[i] == 1:
        u -= 1
        ans.append('U')
        if u < 0:
            sign = 1
            break
    elif hanger[i] == 2:
        d -= 1
        ans.append('D')
        if d < 0:
            sign = 1
            break
    else:
        if u > 0:
            u -= 1
            ans.append('U')
        elif d > 0:
            d -= 1
            ans.append('D')
        else:
            break

if sign == 0:
    print('YES')
    print(*ans, sep='')
else:
    print('NO')