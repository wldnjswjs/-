n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

result = []

for i in range(n):
    result.append(t[i]+1+i)

print(max(result)+1)