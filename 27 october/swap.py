# swap two numbers with the help of third variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

temp = a
a=b
b=temp

print("After swapping: ")
print("First number:", a)
print("Second number:", b)





# swap two numbers without the help of third variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a= a+b
b= a-b
a= a-b

print("After swapping: ")
print("a=", a)
print("b=", b)  
