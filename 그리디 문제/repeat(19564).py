s = input()
count = 1

for i in range(len(s)-1):
    if ord(s[i]) < ord(s[i+1]):
        continue
    else:
        count += 1
        
print(count)