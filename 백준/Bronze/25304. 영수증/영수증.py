X = int(input())
N = int(input())

money = 0

for i in range(N):
    a, b = map(int, input().split())
    money += a * b

print("Yes" if money == X else "No")