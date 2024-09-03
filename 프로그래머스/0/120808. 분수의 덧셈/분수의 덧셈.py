 # 최대 공약수 확인
def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

def solution(numer1, denom1, numer2, denom2):
    # 최소공배수는 (x * y) // 최대공약수
    # 최대공약수는 x,y의 최대공약수 == y와 (x % y == r)의 최대공약수

    # 최대 공약수 확인
    num = gcd(denom1, denom2)

    # 최대 공배수 확인
    answer = (denom1 * denom2) // num

    # 그 후 분자와 분모의 최대공약수로 약분한다. 
    # 결과가 5/4 라면 약분이 필요없지만, 10/6이라면 5/3으로 약분해줘야한다.
    value = gcd((numer1 * answer // denom1) + (numer2 * answer // denom2), answer)

    return [((numer1 * answer // denom1) + (numer2 * answer // denom2)) // value, answer // value]