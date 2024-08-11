def solution(a, b, c):
    return (a == b == c) * (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3) or (a == b or b == c or c == a) * (a + b + c) * (a**2 + b**2 + c**2) or (a + b+ c)