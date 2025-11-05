t=input("Ввод: ")
w=t.split()
print("Вывод: ", end='')
for i in range(len(w)):
    if len(w[i])<3: print('', end='')
    else: print(w[i][0], end='')
