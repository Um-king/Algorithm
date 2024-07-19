def solution(my_string, alp):
    # return ''.join([i.upper() if i == alp else i for i in my_string])
    return my_string.replace(alp, alp.upper())