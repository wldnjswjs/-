a, b, c, m = map(int, input().split())

work = 0
stamina = 0

for i in range(24):
    if stamina > m:
        print(0)
    else:
        if stamina + a <= m:
            stamina += a
            work += b
        else:
            if stamina - c >= 0:
                stamina -= c
            else:
                stamina = 0
      
print(work)