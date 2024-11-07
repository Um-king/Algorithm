def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 0, 0, 0, 0

    for i, word in enumerate(wallpaper):
        for j, file in enumerate(word):
            if file == "#":
                answer.append((i, j))

    lux, luy = min(answer, key=lambda x:x[0])[0], min(answer, key=lambda x:x[1])[1]
    rdx, rdy = max(answer, key=lambda x:x[0])[0] + 1, max(answer, key=lambda x:x[1])[1] + 1

    return [lux, luy, rdx, rdy]
