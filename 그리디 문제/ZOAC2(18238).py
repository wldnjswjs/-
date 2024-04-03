s = list(input())

count = 0
first = 'A'

for i in s:
    right = ord(i) - ord(first)
    left = ord(first) - ord(i)

    if left < 0:
        left += 26
    elif right < 0:
        right += 26
    
    count += min(left, right)
    first = i

print(count)