t = int(input())

times = [300, 60, 10]
answer = []
    
if t % 10 != 0:
    print(-1)
else:
    for i in times:
        if t >= i:
            answer.append(t // i)
            t -= (t//i)*i
        else: 
            answer.append(0)

    print(*answer)