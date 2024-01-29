while True:
    s = sorted(list(map(int, input().split())), reverse = True)

    if s[0] == 0 and s[1] == 0 and s[2] == 0:
        break;

    n = len(set(s))

    t_lst = ['Invalid', 'Equilateral', 'Isosceles', 'Scalene']

    if s[0] >= s[1] + s[2]:
        print(t_lst[0])
    else:
        print(t_lst[n])