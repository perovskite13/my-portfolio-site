#Variables and User input
#Q1
n1 = int(input("Give a number: "))
n2 = int(input("Give another number: "))
sum = n1 + n2
print(sum)

#Q2
n3 = int(input("Give a number: "))
n4 = int(input("Give another number: "))
multiply = n3*n4
print(multiply)

#Q3
n5 = float(input("Hello! I convert km to m/cm. Give me a number!: "))
m = int(n5*1000)
cm = int(n5*100000)
print(f"{n5} km can be converted to: {m} meters; {cm} centimeters")

#Q4
name = input("Hi, what's your name? ")
age = int(input(f"Hi {name}, How tall are you in cm? "))
output = f"{name} is {age}cms tall"
print(output)