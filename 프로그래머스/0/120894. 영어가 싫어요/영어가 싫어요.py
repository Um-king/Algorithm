def solution(numbers):
    for i,j in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
        numbers = numbers.replace(j, str(i))
    return int(numbers)