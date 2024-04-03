s = input().replace(' ','')
ucpc = 'UCPC'
j = 0

for i in s:
    if i == ucpc[j]:
        j += 1
    if j == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')