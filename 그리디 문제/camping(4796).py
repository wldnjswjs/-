i = 1
# while문을 활용하여 무한반복
while True:
    l, p, v = map(int, input().split())
    # l,p,v가 모두 0인 경우 break로 탈출
    if l+p+v == 0:
        break

    # 휴가의 v일 중 (v//p)만큼 l일을 온전히 캠핑장을 이용 가능
    res = (v//p)*l
    # 휴가의 v일 중 (v%p)에서 l과 작은 일만큼 캠핑장을 이용 가능
    res += min((v%p), l)
    print('Case %d: %d' %(i, res))
    i += 1