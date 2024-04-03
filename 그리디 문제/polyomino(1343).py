s = input().split('.')
sign = 0

for i in range(len(s)):   
    if len(s[i])%2 == 1:
        sign += 1
        break
    else:
        s[i] = s[i].replace('XXXX','AAAA')
        s[i] = s[i].replace('XX','BB')

if sign != 0:
    print(-1)
else:
    print(*s, sep='.')