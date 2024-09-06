def solution(elements):
    s = set()
    for i in range(len(elements)):
        v = elements[i]
        s.add(v)
        for j in range(i+1, i+len(elements)):
            v += elements[j%len(elements)]
            s.add(v)
    return len(s)

