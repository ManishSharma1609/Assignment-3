#Question 1
input_number=int(input("Enter your Number:"))
Binary=bin(input_number)
print("Binary equivalent:",Binary, "\n")

#Question 2
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_cal = input("Let's do next calculation? (yes/no): ")
        if next_cal == "no":
            break

    else:
        print("Invalid Input")


#Question 3
import math
print("a)")
a=3
b=4
c=5
print((a+b)*c,"\n")

print("b)")
n=int(input("Enter the value of n:"))
print(n*(n-1)/2, "\n")

print("c)")
r=int(input("Enter the value of radius:"))
print(4*math.pi*r**2, "\n")

print("d)")
r=int(input("Enter the value of r:"))
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print((r*(math.cos(a))**2+r*(math.sin(b))**2)**1/2, "\n")

print("e)")
y1 = int(input("Enter Number y1:"))
y2 = int(input("Enter Number y2:"))
x1 = int(input("Enter Number x1:"))
x2 = int(input("Enter Number x2:"))
ansr = (y1 - y2)/(x1 - x2)
print(ansr, "\n")

#Question 4
print("a part")
for a in range(5):
    print(a,"\n")
print("b part")
for b in range(3,10):
    print(b,"\n")
print("c part")
for c in range(4,13,3):
    print(c,"\n")
print("d part")
for d in range(15,5,-2):
    print(d,"\n")
print("e part")
for e in range(5,3):
    print(e,"\n")

#Qustion 5
h=int(input("Enter Number of Hydrogen atoms:"))
c=int(input("Enter Number of Carbon atoms:"))
o=int(input("Enter Number of Oxygen atoms:"))
total=h*1.00794+c*12.0107+o*15.9994
print("The total combined molecular weight in grams per mole is",total)
