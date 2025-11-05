import re
t=input("Ввод: ")
s = re.split(r'(?<=[.?!]) ', t)
for i in s:
    print(i)
print("Предложений в тексте: ", len(s))