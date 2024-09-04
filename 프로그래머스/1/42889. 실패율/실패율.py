def solution(N, stages):
    answer = []
    people = len(stages)

    for i in range(1, N+1):
        cnt = stages.count(i)
        loss = 0 if cnt == 0 else cnt/people
        answer.append((i, loss))
        people -= cnt

    return [i for i, j  in sorted(answer, key=lambda x:x[1], reverse=True)]