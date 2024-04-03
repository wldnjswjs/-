n = int(input())
arr = list(map(int, input().split()))

high = 0
count = 0
answer = []

for i in arr:
    if i > high:
        high = i
        count = 0
    else:
        count += 1
    answer.append(count)

print(max(answer))