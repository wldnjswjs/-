import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
count = 1

while n2 != n1:
    count += 1

    # n2를 임시 보관
    tmp = n2

    # 오른쪽에 1을 추가한 경우: n2를 1을 추가하기 전 값으로 변경
    if n2 % 10 == 1:
        n2 //= 10
    # 2를 곱한 경우: n2를 *2 하기 전 값으로 변경
    elif n2 % 2 == 0:
        n2 //= 2

    # 만일 n2값이 만들어질 수 없는 값이라면
    # 즉 if문을 아무것도 거치지 않은 경우
    if tmp == n2:
        print(-1)
        break
else:
    print(count)