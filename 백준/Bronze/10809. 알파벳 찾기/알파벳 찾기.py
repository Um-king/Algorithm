lst = ["-1"] * 26
s = input()
for i, j in enumerate(s):
    if lst[ord(j) - 97] == "-1":
        lst[ord(j) - 97] = str(i)

print(' '.join(lst))