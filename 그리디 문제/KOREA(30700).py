s = input()

korea = ['K', 'O', 'R', 'E', 'A']
count = 0
j = 0

for i in s:
    if i == korea[j]:
        j += 1
        count += 1
    
    if j == 5:
        j = 0

print(count)