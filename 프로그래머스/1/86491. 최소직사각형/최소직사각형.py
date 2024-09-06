def solution(sizes):
    w = []
    h = []
    for i, j in sizes:
        if i < j:
            i, j = j, i  # 가로보다 세로가 긴 경우 세로를 가로로 넣는다.
        w.append(i)
        h.append(j)

    return max(w) * max(h)