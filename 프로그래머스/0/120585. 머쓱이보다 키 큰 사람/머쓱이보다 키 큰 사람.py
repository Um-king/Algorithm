def solution(array, height):
    return sum(list(map(lambda x : x > height, array)))