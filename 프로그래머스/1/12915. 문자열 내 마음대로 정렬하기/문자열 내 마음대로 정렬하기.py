def solution(strings, n):
    # x의 n번째 인덱스를 기준으로 먼저 정렬한 후 동일한 값이 존재하면 문자열 x를 기준으로 정렬
    return sorted(strings, key=lambda x:(x[n], x))