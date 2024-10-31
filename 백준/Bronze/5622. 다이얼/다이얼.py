number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
dial = input()
answer = 0

for i in dial:
    for j, k in enumerate(number):
        if i in k:
            answer += j + 3

print(answer)
