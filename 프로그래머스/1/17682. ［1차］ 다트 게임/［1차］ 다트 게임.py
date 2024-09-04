def solution(dartResult):
    answer = 0
    bonus = {'S':1, 'D':2, 'T':3}
    numbers = []
    num = ""
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i.isalpha():
            numbers.append(int(num) ** bonus[i])
            num = ""
        elif i == "*":
            if len(numbers) > 1:
                numbers[-2] *= 2
            numbers[-1] *= 2
        elif i == "#":
            numbers[-1] *= -1
    return sum(numbers)