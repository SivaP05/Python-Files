age = int(input("Enter your age: "))
pizza = input("Do you like pizza? (yes/no): ")
exercise = input("Do you exercise regularly? (yes/no): ")
'''if age <=30:
    if pizza == "yes":
        print ("You are unfit!")
    elif exercise == "yes":
        print ("You are fit!")
    else:
        print ("You are unfit!")
else:
    if exercise == "yes":
        print ("You are fit!")
    else:
        print ("You are unfit!")

#tertiary operator
age = int(input("Enter your age: "))
print("teenager" if age < 18 else "adult")
'''
print(("Unfit" if pizza == "yes" else "unfit") if age < 30 else ("fit" if exercise == "yes" else "unfit"))