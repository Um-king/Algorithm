import datetime

def solution(a, b):
    date = datetime.datetime(2016, a, b)
    week = date.strftime('%a')
    return week.upper()