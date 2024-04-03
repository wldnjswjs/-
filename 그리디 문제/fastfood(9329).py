t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    k = []
    price = 0

    for _ in range(x[0]):
        k.append(list(map(int, input().split())))
    
    sticker = list(map(int, input().split()))

    for i in range(x[0]):
        m = 100
        for j in range(1,k[i][0]+1):
            m = min(m, sticker[k[i][j]-1])
        price += m*k[i][-1]

    print(price)    