def solution(sizes):
    w = []
    h = []

    for i in sizes:
        if i[0] >= i[1]:
            w.append(i[0])
            h.append(i[1])
        else: # 가로보다 세로가 긴 경우 세로를 가로로 넣는다.
            w.append(i[1])
            h.append(i[0])

    return max(w) * max(h)