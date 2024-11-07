# def solution(wallpaper):
#     answer = []
#     lux, luy, rdx, rdy = 0, 0, 0, 0

#     for i, word in enumerate(wallpaper):
#         for j, file in enumerate(word):
#             if file == "#":
#                 answer.append((i, j))

#     lux, luy = min(answer, key=lambda x:x[0])[0], min(answer, key=lambda x:x[1])[1]
#     rdx, rdy = max(answer, key=lambda x:x[0])[0] + 1, max(answer, key=lambda x:x[1])[1] + 1

#     return [lux, luy, rdx, rdy]

def solution(wallpaper):
    a, b = [], []

    for i, word in enumerate(wallpaper):
        for j, file in enumerate(word):
            if file == "#":
                a.append(i)
                b.append(j)

    return [min(a), min(b), max(a) + 1, max(b) + 1]