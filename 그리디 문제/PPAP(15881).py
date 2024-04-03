import sys
input = sys.stdin.readline

n = int(input())
s = list(input())
count = 0

for i in range(n):
    if s[i] == 'p' and s[i+1] == 'P' and s[i+2] == 'A' and s[i+3] == 'p':
        count += 1
        s[i+3] = 0

print(count)