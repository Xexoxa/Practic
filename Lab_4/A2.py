n=int(input())
m=int(input())
print("ПРЯМОУГОЛЬНИК",n, "x",m)
for i in range(n): 
    for j in range(m): 
        print('#', end='')
    print()
print()
print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
o=1
for i in range(n):
    print(o*'#', end='')
    o+=1
    print()
    

