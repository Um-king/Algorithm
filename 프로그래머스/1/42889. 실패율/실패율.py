def solution(N, stages):
    answer = []
    p = len(stages)

    for i in range(1, N+1):
        cnt = stages.count(i)
        loss = 0 if cnt == 0 else cnt / p
        answer.append((i, loss))
        p -= cnt
    return [i for i, _ in sorted(answer, key=lambda x:x[1], reverse=True)]