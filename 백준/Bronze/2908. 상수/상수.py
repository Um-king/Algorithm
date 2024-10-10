n, m = input().split()

n, m = n[::-1], m[::-1]

print(n if n > m else m)