def solution(rank, attendance):
    answer = sorted([(j, i) for i, j in enumerate(rank) if attendance[i]])
    return 10000 * answer[0][1] + 100 * answer[1][1] + answer[2][1]