def solution(a, b, n):
    answer = 0
    
    while n >= a:
        x, y = n // a * b, n % a
        answer += x
        n = x + y

    return answer