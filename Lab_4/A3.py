import string
r=input()
n=0
t=0
if len(r)<5: print("Неверный ввод. Строка должна быть не меньше 5")
elif not all(char in '01' for char in r): print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    print("Общее количество пакетов:", len(r))
    print("Количество потерянных пакетов:", r.count('0'))
    for packet in r:
        if packet == '0':
            n+=1
            t=max(t, n)
        else: n=0
    print("Длина самой длинной последовательности потерянных пакетов:", t)
    t = r.count('0')/len(r)*100
    print("Процент потерь:", round(t, 1), "%")
    print("Качество связи: ", end='')
    if t<=1: print("Отличное качество")
    elif t<=5: print("Хорошее качество")
    elif t<=10: print("Удовлетворительное качество")
    elif t<=20: print("Плохое качество")
    else: print("Критическое состояние сети")