x = int(input())
y = int(input())
z = int(input())

result = x + y + z

if result != 180:
    print("Error")

else:
    if x == y == z:
        print("Equilateral")
    elif x == y or x == z or y == z:
        print("Isosceles")
    else:
        print("Scalene")