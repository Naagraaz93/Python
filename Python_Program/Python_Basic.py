# 1. WAP to add two integer.
Num = int(input("Enter a number: "))
Num1 = int(input("Enter a number: "))

# Add two integer
Add=Num+Num1
print('Addition of Num and Num1:',Add)
print("="*60)

# Subtraction 
print('Subtraction of Num and Num1:',Num-Num1)
print("="*60)

# Multiplication
print('Multiply of Num and Num1:',Num*Num1)
print("="*60)

# Divided
print('Divide of Num and Num1:',Num/Num1)
print("="*60)

# 2. WAP to repeat a given string 5 times.

String = str(input("Enter string: "))

print(String*5)
print("="*60)

# 3. WAP to get the Average of given numbers.
A=120 
B=520
C=260
Avg=(A+B+C)/3
print("Average of A B and C is :",Avg)
print("="*60)

# From list
List=[200,300,600,400]
Length=len(List)

print(Length)
print("="*60)

Add=sum(List)
print(Add)
print("="*60)

Avg=Add/Length
print('Average of given list:', Avg)
print("="*60)

# 4. WAP to get the median of given numbers.
# Formula= (n+1)/2

List=eval (input("Enter list: "))
Length=len(List)
mean=sum=0
for i in range (0,Length):
    sum=+List[i]
mean=sum/Length
print("The median of list:",mean)

print("="*60)

# 5. WAP to print the square and cube of a given number.

NUmber = int(input("Enter a number: "))

Square=(NUmber**2)
Cube=(NUmber**3)
print("Square of number:",Square)
print("Cube of number:",Cube)
print("="*60)

# 6. WAP to interchange values between variables.
Num = int(input("Enter a number: "))
Num1 = int(input("Enter a number: "))
Num,Num1=Num1,Num
print("Interchange value:",Num,Num1)
print("="*60)

# 7. WAP to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)

Num = int(input("Enter First number: "))
Num1= int(input("Enter Second number: "))
Num2=  int(input("Enter Third number: "))

# 8. WAP to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab

A=int(input("Enter a number:"))
B=int(input("Enter a number:"))

Result=A**2 + B**2 +2*(A*B)


print("The value of ((A+B)**2) is :",Result)

LHS=((A+B)**2)

RHS=A**2 + B**2 +2*(A*B)

if LHS==RHS:
    print("Correct Program:")
else:
    print("Wrong Program:")

print("="*50)

# 9. WAP  to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab

A=int(input("Enter a number:"))
B=int(input("Enter a number:"))

Result=A**2 + B**2 -2*(A*B)


print("The value of ((A+B)**2) is :",Result)

LHS=((A-B)**2)

RHS=A**2 + B**2 -2*(A*B)

if LHS==RHS:
    print("Correct Program:")
else:
    print("Wrong Program:")

print("="*50)

# 10. WAP  to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)

A=int(input("Enter a number:"))
B=int(input("Enter a number:"))

Result=(A-B)*(A+B)


print("The value of (A)**2-(B)**2) is :",Result)

LHS=((A-B)**2)

RHS=A**2 + B**2 -2*(A*B)

if LHS==RHS:
    print("Correct Program:")
else:
    print("Wrong Program:")

print("="*50)

# 11. WAP to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3 

A=int(input("Enter a number:"))
B=int(input("Enter a number:"))

Result=A**3 + B**3 +3*A*B*(A+B)


print("The value of (a + b)3 is :",Result)

LHS=(A+B)**3

RHS=A**3 + B**3 +3*A*B*(A+B)

if LHS==RHS:
    print("Correct Program:")
else:
    print("Wrong Program:")

print("="*50)

# 12. WAP to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

A=int(input("Enter a number:"))
B=int(input("Enter a number:"))

# Find the Value of=(A-B)**3
# (A – B)3 = A3 – 3A2B + 3AB2 – B3

Result= A**3-3*A**2*B+3*A*B**2-B**3

print("The value of (A-B)3 is :",Result)

LHS=(A-B)**3

RHS=A**3-3*A**2*B+3*A*B**2-B**3

if LHS==RHS:
    print("Correct Program:")
else:
    print("Wrong Program:")

print("="*50)

# 13. WAP to calculate the area of the square.
#Formula : Area = a*a

Side=int(input("Enter the side length of Square:"))

Area=(Side)**2

print("Area of square:",Area)

print("="*50)

# 14. WAP to calculate the area of a circle.

# Formula = PI*r*r

Radius = int(input("Enter the radius of Circle: "))

PI = 3.14

Area = PI * Radius**2

print("Area of circle:", Area)

# 15. WAP to calculate the area of a cube.
# Formula = 6*a*a

Side=int(input("Enter the side of cube:"))

Area=6*Side**2
print("Area of cube:",Area)

# 16. WAp to find the area of cylinder.

# Formula= 2*PI*r*h + 2*PI*r*r

R=int(input("Enter the Radius of cylinder:"))
H=int(input("Enter the Height of cylinder:"))
PI=3.14
Area=2*PI*R*H + 2*PI*R**2
print("Area of Cylinder:",Area)

# 17. WAP  to check whether the enter number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

Number=int(input("Enter a Number:"))












