a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
a3 = ["White", "Black"][(a1-a2)%2==1]
b3 = ["White", "Black"][(b1-b2)%2==1]
print(a3,b3)