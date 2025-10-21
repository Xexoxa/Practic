import random
import time
N=int(input("Введите количество примеров: "))
all_start_time = time.time()
o=0
for i in range(N):
    print("Вопрос ", i+1, "/", N)
    a=random.randint(2, 9)
    b=random.randint(2, 9)
    start_time = time.time()
    while True:
        try:
            answer = int(input(f"{a} × {b} = ")) 
            break 
        except ValueError:
            print("Пожалуйста, введите целое число!")
    time_spend = time.time() - start_time
    if a*b==answer: print("Верно! (Время: ", round(time_spend, 1), " сек)"); o+=1
    else: print("Неверно! Правильно:", a*b, "(Время: ", round(time_spend, 1), " сек)")
all_time_spend = time.time() - all_start_time
print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print("Общее время:", round(all_time_spend, 1))
print("Среднее время на вопрос:", round(all_time_spend/N, 1))
print("Правильных ответов:", o, "/", N)
print("Процент правильных:", round(o/N*100, 1), "%")