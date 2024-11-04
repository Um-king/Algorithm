n = int(input())
stack = []

for _ in range(n):
    num = int(input())
    
    if num:
        stack.append(num)
    else:
        if stack:
            stack.pop()

print(sum(stack))