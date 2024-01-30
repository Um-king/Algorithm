# def solution(my_string):
#     return my_string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')


def solution(my_string):
    return "".join(i for i in my_string if i not in ['a','e','i', 'o', 'u'])

# 정규식
# import re
# def solution(my_string):
#     return re.sub('[aeiou]', '', my_string)