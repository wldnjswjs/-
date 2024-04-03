'''
n = int(input())
answer = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))

test_a = sorted(a, reverse=True)
test_b = sorted(b)

for i in range(n):
    answer += test_a[i] * test_b[i]

print(answer)
'''

n = int(input())
answer = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b)))
    answer += x*y

print(answer)