while True:
    a, b = map(int, input().split())

    if not a and not b:
        break

    if a > b and a % b == 0:
        print("multiple")
    elif a < b and b % a == 0:
        print("factor")
    else:
        print("neither")