# WAP to find middle among 3 number using multiple if.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > b and a < c) or (a < b and a > c):
    print("Middle number is:", a)

if (b > a and b < c) or (b < a and b > c):
    print("Middle number is:", b)

if (c > a and c < b) or (c < a and c > b):
    print("Middle number is:", c)