n, l, k = map(int, input().split())
score = []


for i in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:              # 어려운 버전일 경우, 140점
        score.append(140)
    elif sub1 <= l:            # 쉬운 버전일 경우, 100점
        score.append(100)

score.sort(reverse=True)       # 고득점 가능 점수 우선으로 정렬
print(sum(score[:k]))          # 풀 수 있는 문제수만큼 점수 득점