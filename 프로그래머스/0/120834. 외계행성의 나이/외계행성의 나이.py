def solution(age):
    return ''.join([chr(97 + i) for i in (map(int, str(age)))]) 