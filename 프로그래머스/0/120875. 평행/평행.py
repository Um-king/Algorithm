def inclination(a, b, c, d):
    num1 = (b[1] - a[1]) / (b[0] - a[0])
    num2 = (d[1] - c[1]) / (d[0] - c[0])

    # 기울기가 같으면 평행한 것
    return int(num1 == num2)

def solution(dots):
    a, b, c, d = dots

    # 4개의 좌표에서 서로 직선을 그엇을 때의 조건
    x = inclination(a, b, c, d)
    y = inclination(a, c, b, d)
    z = inclination(a, d, b, c)

    return int(1 in [x, y, z])