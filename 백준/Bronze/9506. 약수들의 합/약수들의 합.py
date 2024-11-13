while True:
    n = int(input())
    lst = []

    if n == -1:
        break

    for i in range(1, n//2 + 1):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        s = str(n) + " = "
        for i in lst:
            s += str(i) + " + "
        print(s[:-3])
    else:
        print(f'{n} is NOT perfect.')