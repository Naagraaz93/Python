
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