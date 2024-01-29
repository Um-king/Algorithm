def solution(array, height):
    l = list(map(lambda x : x > height, array))
    return sum(l)