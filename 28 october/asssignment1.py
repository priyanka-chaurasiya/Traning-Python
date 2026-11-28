# WAP to find max. among 3 number using multiple if.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Maximum number is:", a)

if b > a and b > c:
    print("Maximum number is:", b)

if c > a and c > b:
    print("Maximum number is:", c)
