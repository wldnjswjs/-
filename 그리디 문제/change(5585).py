# 지불할 금액
m = int(input())

# 동전 단위
money = [500, 100, 50, 10, 5, 1]
answer = []
count = 0
# 받아야할 거스름돈
c = 1000 - m

# 거스름돈을 단위별로 나누어 개수를 저장한다. 
for i in money:
    answer.append(c//i)
    c -= (c//i)*i

# 개수의 총합을 출력 
for i in answer:
    count += i

print(count)