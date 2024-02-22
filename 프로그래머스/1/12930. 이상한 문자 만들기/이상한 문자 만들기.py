def solution(s):
    word = ""
    lst = []
    for i in s.split(' '):
        for num, j in enumerate(i):
            if num % 2 == 0:
                word += j.upper()
            else:
                word += j.lower()
        lst.append(word)
        word = ""
    return ' '.join(lst)