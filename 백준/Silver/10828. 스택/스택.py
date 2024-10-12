import sys
n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    s = sys.stdin.readline().split()

    if s[0] == "push":
        lst.append(s[1])
    elif s[0] == "pop":
        if lst:
            print(lst.pop())
        else:
            print(-1) 
    elif s[0] == "size":
        print(len(lst))
    elif s[0] == "empty":
        print(0 if lst else 1)
    elif s[0] == "top":
        print(lst[-1] if lst else -1) 