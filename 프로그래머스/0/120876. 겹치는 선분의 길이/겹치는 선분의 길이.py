def solution(lines):
    a, b, c = lines
    a = set(range(a[0], a[1]))
    b = set(range(b[0], b[1]))
    c = set(range(c[0], c[1]))

    n1 = a.intersection(b)
    n2 = a.intersection(c)
    n3 = b.intersection(c)

    return len(n1.union(n2).union(n3))