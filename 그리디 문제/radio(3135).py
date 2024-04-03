a, b = map(int, input().split())
n = int(input())
radio = []

for i in range(n):
    radio.append(int(input()))

min_radio = []

for i in radio:
        min_radio.append(abs(b-i))

if abs(b-a) <= min(min_radio):
        print(abs(b-a))
else:
    print(min(min_radio)+1)