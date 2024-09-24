n = int(input())

for index, value in enumerate(range(1, n + 1)):
    x, y = map(int, input().split())
    print(f"Case #{index + 1}: {x + y}")