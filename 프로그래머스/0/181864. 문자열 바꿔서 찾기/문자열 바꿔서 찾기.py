def solution(myString, pat ):
    return int(pat in ''.join(['B' if i == 'A' else 'A'  for i in myString]))