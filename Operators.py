#Arithmetic Operators (+, -, *, /, %, //, **)

#Relation Operators (=, ==, !=, <, >, <=, >=)
a=20
b=30
a,b=b,a
print("a = ",a,"b = ",b)


print(a==b)
a="Siva"
b="siva"
print(a==b)
print(a<b)

#ASCII values
print("s:", ord("s"))
print("S:", ord("S"))

#argumented assignment operators (+=, -=, *=, /=, %=, //=, **=)
a=10
a=a+5
print(a)
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a//=5
print(a)
a**=5
print(a)

#Practice Problems:
name, balance = "Siva", 200000.0
balance+=(0.05*balance) #5% interest
print("Balance after interest:", balance)

#Membership Operators (in, not in)
lst = [10,20,30,40,50]
print(20 in lst)
print(90 in lst)
print(90 not in lst)
print(20 not in lst)

name = "Indumathi"
print("I" in name)

print(ord("0"), ord("9"), sep="----")

#Logical Operators (and, or, not)
a, b = 10, 20
statement1 = (a==10)
statement2 = (b==30)
print(statement1 and statement2)
print(statement1 or statement2)
print(not statement1)

#Bitwise Operators (&, |, ^, ~, <<, >>)
a=2
b=3
print(a & b) #AND
print(a | b) #OR
print(a ^ b) #XOR

#String replication operator
a = "Siva"
print(a*100)

#String concatenation operator
b = "Indu"
print(a+b)

#practice problem:
star = "*"
greetings = "Happy" + " " + "Holidays!"
print(20*star,greetings,20*star,sep="\n")
print(star*20+"\n"+greetings+"\n"+star*20)