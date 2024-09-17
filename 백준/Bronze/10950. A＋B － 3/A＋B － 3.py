n = int(input())

for i in range(n):
    s = input().split()
    print(eval(f"{s[0]} + {s[1]}"))