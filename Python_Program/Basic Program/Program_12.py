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