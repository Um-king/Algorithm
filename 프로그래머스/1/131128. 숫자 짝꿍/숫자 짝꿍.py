# def solution(X, Y):
#     answer = []
#     d1 = {}
#     d2 = {}
#     s = sorted((set(X) & set(Y)), reverse=True)

#     if len(s) == 0:
#         return "-1"

#     for i in X:
#         if i in d1:
#             d1[i] += 1
#         else:
#             d1[i] = 1
    
#     for i in Y:
#         if i in d2:
#             d2[i] += 1
#         else:
#             d2[i] = 1

#     for i in s:
#         answer.extend([int(i)] * min(d1[i], d2[i]))
    
#     return ''.join(map(str, answer)) if any(answer) else "0"

def solution(X, Y):
    answer = ""

    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
    
    if answer == "":
        return "-1"
    elif len(answer) == answer.count("0"):
        return "0"
    else:
        return answer