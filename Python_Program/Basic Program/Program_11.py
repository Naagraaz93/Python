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
