
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