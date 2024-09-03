def solution(n):
    num = ""
    answer = 0
    while n > 0:
        x, y = n // 3, n % 3
        num += str(y)
        n = x 
    return sum([int(j) * (3**i) for i, j in enumerate(num[::-1])])