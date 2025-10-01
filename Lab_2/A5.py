A=int(input("Введите число А: "))
B=int(input("Введите число B: "))
result = ["NO", "YES"][A % B == 0]
print(result)