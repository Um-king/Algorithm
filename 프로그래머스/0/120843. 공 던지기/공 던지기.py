def solution(numbers, k):
    i = 1
    while i < k:
        numbers = numbers[2:] + numbers[:2]
        i += 1
    return numbers[0]