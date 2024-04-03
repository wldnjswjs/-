while 1:
    try:
        a, b, c = map(int, input().split())
        jump = max(b-a, c-b) - 1
        print(jump)
    except:
        break