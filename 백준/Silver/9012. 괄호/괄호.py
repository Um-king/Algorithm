n = int(input())

for _ in range(n):
    stack = []
    s = input()
    for i in s:
        if stack and i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print("NO" if stack else "YES")