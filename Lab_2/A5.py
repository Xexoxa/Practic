A=int(input("Введите число А: "))
B=int(input("Введите число B: "))
result = ["YES", "NO"][A % B == 0]
print(result)