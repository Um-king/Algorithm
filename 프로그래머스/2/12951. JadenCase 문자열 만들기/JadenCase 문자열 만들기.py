def solution(s):
    return ' '.join([j[0].upper() + j[1:].lower() if j != "" and not j.isdigit() else j for i,j in enumerate(s.split(' '))])