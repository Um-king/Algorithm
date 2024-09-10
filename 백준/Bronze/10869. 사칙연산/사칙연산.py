a,b = map(int, input().split())

for i in ['+', '-', '*', '//', '%']:
    print(eval(f'{a}{i}{b}'))