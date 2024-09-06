# def solution(n,a,b):
#     answer = 1
#     x, y = min(a, b), max(a, b)
#     n = bin(n)[2:]
#     num = len(n) - (n.index("1") + 1)
#     while answer < num:
#         if x%2 and x + 1 == y:
#             return answer

#         x = x // 2 + x % 2
#         y = y // 2 + y % 2
        
#         answer += 1
#     return answer
def solution(n, a, b):
    answer = 0
    while a!=b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer