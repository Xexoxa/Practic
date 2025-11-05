t=input("Исходный текст: ")
while '(' in t or ')' in t:
    l= t.rfind('(')
    r= t.find(')',l)
    t = t.replace(t[l:r + 1], '')
print("Укороченный текст: ",t)