num_list = []

for _ in range(10):
    n = int(input()) % 42

    if n not in num_list:
        num_list.append(n)

print(len(num_list))