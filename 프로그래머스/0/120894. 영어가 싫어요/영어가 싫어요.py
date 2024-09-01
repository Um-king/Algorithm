def solution(numbers):
    dic = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
        'zero':'0'
    }

    s = ""
    answer = ""
    for i in numbers:
        s+=i
        if s in dic:
            answer += dic[s]
            s = ""
    return int(answer)