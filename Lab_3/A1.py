x1 = int (input())
y1 = int (input())
x2 = int (input())
y2 = int (input())

if (x1>0 and y1>0):n="I"
elif (x1<0 and y1>0):n="II"
elif (x1<0 and y1<0):n="III"
elif (x1>0 and y1<0):n="IV"
else:n=0

if (x2>0 and y2>0):m="I"
elif (x2<0 and y2>0):m="II"
elif (x2<0 and y2<0):m="III"
elif (x2>0 and y2<0):m="IV"
else:m=0

if (n==0 or m==0):print("Ошибка")
elif (n==m):print("YES, ", n)
else:print("NO")