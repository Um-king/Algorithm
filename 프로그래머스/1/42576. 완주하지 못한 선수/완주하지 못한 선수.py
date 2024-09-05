def solution(participant, completion):
    d = {}

    for i in participant:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for i in completion:
        if i in d:
            d[i] -= 1
        

    return list(filter(lambda x:d[x] == 1, d.keys()))[0]
    