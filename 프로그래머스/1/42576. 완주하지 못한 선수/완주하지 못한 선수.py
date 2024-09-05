# def solution(participant, completion):
#     d = {}

#     for i in participant:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
    
#     for i in completion:
#         if i in d:
#             d[i] -= 1

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i,j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1] 
        

    return list(filter(lambda x:d[x] == 1, d.keys()))[0]
    