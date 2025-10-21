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
print()
print("РАМКА",n,"*",m)
for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            print("#", end="") 
        else:
            print(" ", end="") 
    print()

