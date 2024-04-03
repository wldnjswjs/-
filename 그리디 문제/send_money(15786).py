n, m = map(int, input().split())
s = input()

for i in range(m):
    p = input()
    k = 0
    for j in p:
        if j == s[k]:
            k += 1
            if k == len(s):
                break
    if k < len(s):
        print('false')
    else:
        print('true')