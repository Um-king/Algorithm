def solution(numbers):
    arr = [0,1,2,3,4,5,6,7,8,9]
    return sum([i for i in arr if i not in numbers])