while True:
    n = list(map(int, input().split()))
    if not n[0] and not n[1]:
        break
    print(n[0] + n[1])
