'''
t = int(input())

c = []

for i in range(t):
    c.append(int(input()))

q = 0
d = 0
n = 0
p = 0

for i in c:
    if i >= 25:
        q = i // 25
        i %= 25
        if i >= 10:
            d = i // 10
            i %= 10
            if i >= 5:
                n = i // 5
                p = i % 5
                print(q,d,n,p, sep=' ')
            else:
                p = i
                print(q,d,n,p, sep=' ')
        elif i >= 5:
            n = i // 5
            p = i % 5
            print(q,d,n,p, sep=' ')    
        else:
            p = i
            print(q,d,n,p, sep=' ')
    elif i >= 10:
        d = i // 10
        i %= 10
        if i >= 5:
            n = i // 5
            p = i % 5
            print(q,d,n,p, sep=' ')
        else: 
            p = i
            print(q,d,n,p, sep=' ')
    elif i >= 5:
        n = i // 5
        p = i % 5
        print(q,d,n,p, sep=' ')
    else:
        p = i
        print(q,d,n,p, sep=' ')
    q = 0
    d = 0
    n = 0
    p = 0
'''

t = int(input())

coins=[25,10,5,1]

for _ in range(t):
    change = int(input())
    change_coin = []

    for i in coins:
        change_coin.append(change // i)
        change %= i

    print(*change_coin)