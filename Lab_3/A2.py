import string
p=input()
n=0
if len(p)!=8: print("Длина пароля не равна 8")
else: n+=1
if p.lower()==p: print("В пароле отсутствуют заглавные буквы")
else: n+=1
if p.upper()==p: print("В пароле отсутствуют строчные буквы")
else: n+=1
if (any(symbol.isdigit() for symbol in p))=="False": print("В пароле отсутствуют цифры")
else: n+=1