max_value = 0
max_index = 0

for i, _ in enumerate(range(9)):
    n = int(input())
    if max_value < n:
        max_value = n
        max_index = i + 1

print(max_value)
print(max_index)
