# Python program to get the factorial of number.

Num = int(input("Enter a number: "))
for i in range(1,Num+1):
    if i == 1:
        fact = 1
    else:
        fact = fact * i
