def solution(progresses, speeds):
    days = []
    answer = []
    i = 1

    for p, s in zip(progresses, speeds):
        if (100 - p) % s == 0:
            days.append((100 - p) // s)
        else:
            days.append((100 - p) // s + 1)

    while True:
        if len(days) > i and days[0] >= days[i]:
            i+=1
        elif len(days) > i and days[0] < days[i]:
            answer.append(i)
            days = days[i:]
            i = 1
        else:
            answer.append(i)
            break;

    return answer