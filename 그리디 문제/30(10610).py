n = input()

if "0" not in n:    # 문자열로 입력을 받았기 때문에 "0" 문자가 있는지 확인
    print(-1)

else:
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    
    if sum % 3 != 0:    # 3의 배수인지 확인
        print(-1)

    else:
        n = sorted(n,reverse=True)  # 큰 수를 출력하기 위해 내림차순 정렬
        print(''.join(n))