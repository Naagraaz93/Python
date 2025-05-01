'''
if: -> Condition is True
   Code-> Execute
else: -> Condition is Flase
   code-> Execute
'''
A = int(input("Enter a number: "))
B = int(input("Enter b number: "))

if A==B: # Condition is True
    print("A and B are same:",A,",",B)
else: # Condition is Flase
    print("A and B are not same:",A,",",B)
print("="*50)

# WAP to check given number is even or odd.

# if any number divided by 2 that it is even number.
# If any number not divided by 2 that is odd number. 

Number=int(input("Enter a number:"))

if Number%2==0:
    print("Number is even:",Number)
else:
    print("Number is odd:",Number)

print("="*50)
# Wap to check number is divisible by 3 or not.

Number=int(input("Enter a number:"))

if Number%3==0:
    print("Number is divisible by 3:",Number)
else:
    print("Number is not divisible by 3:",Number)

print("="*50)

# Wap print square if number is even and print cube if number is odd.

Number=int(input("Enter a number:"))

if Number % 2 == 0:
    print("Square of the number is:", Number ** 2)
else:
    print("Cube of the number is:", Number ** 3)

print("="*50)

# Wap given number to check is postive or negative.

Number=int(input("Enter a number:"))

if Number>=0:
    print("Number is postive:", Number)
else:
    print("Number is negative:", Number)

print("="*50)

# Check  number is divisible by 7 then add 50 in number and else subtract 50 in number.

Number=int(input("Enter a number:"))

if Number % 7 == 0:
    print("Divisble by 7:", Number+50)
else:
    print("Not divisible by 7:", Number-50)
    
print("="*50)