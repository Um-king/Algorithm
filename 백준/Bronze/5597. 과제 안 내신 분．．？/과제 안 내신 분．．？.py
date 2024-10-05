student = [i + 1 for i in range(30)]

for _ in range(28):
    x = int(input())
    student.remove(x)

for i in student:
    print(i)