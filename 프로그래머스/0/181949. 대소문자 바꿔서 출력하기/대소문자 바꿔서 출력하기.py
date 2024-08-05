str = input()
str = ''.join([i.lower() if i.isupper() else i.upper() for i in str])
print(str)