#Conditional Statements
'''
a = 5
b = int(input("Enter b: "))

if (a == b):
    print("a and b are equal")
elif (b == 0):
    print("b is 0")

else:
    print("a and b are not equal")
'''
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is a negative number")