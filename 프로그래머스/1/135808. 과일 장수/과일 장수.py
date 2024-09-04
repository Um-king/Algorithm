# def solution(k, m, score):
#     answer = 0
#     score.sort(reverse=True)
#     for i in range(len(score) // m): # m만큼 배열을 나눠서 합을 구해야하니깐
#         box = score[m*i:m*(i+1)]
#         answer += box[-1] * m
#     return answer

def solution(k, m, score):
    return sum(sorted(score)[len(score) % m::m]) * m