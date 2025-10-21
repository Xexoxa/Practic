import string
r=input()
if len(r)<5: print("Неверный ввод. Строка должна быть не меньше 5")
elif not all(char in '01' for char in r): print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    