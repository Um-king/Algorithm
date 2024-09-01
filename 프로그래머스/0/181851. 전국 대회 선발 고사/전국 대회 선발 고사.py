def solution(rank, attendance):
    cnt = 0
    tmp = []
    for i in range(1, len(rank) + 1):
        index = rank.index(i)
        if attendance[index]:
            tmp.append(index)
            cnt += 1

        if cnt == 3:
            break
    return 10000 * tmp[0] + 100 * tmp[1] + tmp[2]