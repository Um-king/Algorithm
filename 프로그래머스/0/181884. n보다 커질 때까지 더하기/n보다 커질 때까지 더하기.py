def solution(numbers, n):
    return min(filter(lambda x : x > n, [sum(numbers[:i+1]) for i in range(0, len(numbers))]))