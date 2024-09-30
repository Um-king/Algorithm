n = int(input())

for i, _ in enumerate(range(n)):
    x, y = map(int, input().split())
    print(f"Case #{i + 1}: {x} + {y} = {x + y}")