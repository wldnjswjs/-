s = input()

yonsei = ['Y','O','N','S','E','I']
korea = ['K','O','R','E','A']
y = 0
k = 0

for i in range(len(s)):
    if s[i] == yonsei[y]:
        y += 1
        if y == 6:
            print('YONSEI')
            break
    if s[i] == korea[k]:
        k += 1
        if k == 5:
            print('KOREA')
            break