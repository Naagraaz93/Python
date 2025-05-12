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

##################### Multiple Condition ##################

######### Logical Opreator:-
'''
> -> Grater than
< -> Less than
<= -> Less than equal
>= -> Greater than equal
!= -> Not equal
== -> Equal
in -> In opreator
is -> Is opreator
is not -> Is not opreator

#################################

And logical Opreator:-

True and False ->  False
False and True ->  False
True and True ->   True
False and False ->  False

Or logical Opreator:-

True or False ->  True
False or True ->  True
True or True ->   True
False or False ->  False


#    Multiple Condition Format

if condition 1:

        Code /

elif conditon 2:
          
        Code /

elif conditon 3:
          
        Code /

Else :
      Code /

'''

# WAP to check greater number of among three number.
#Type 1

############### AND CONDITION ######################
a=120
b=250
c=236

if a>b and a>c:
    print("A has greater value:",a)
elif b>a and b>c:
    print("B has greater value:",b)
elif c>a and c>b:
    print("C is greater value:",c)
elif a==b==c:
    print("A B C are equal number:")
else:
    print("No one is greater number:")
print("="*50)

A=int(input("Enter the First Number:"))

B=int(input("Enter the Second Number:"))

C=int(input("Enter the Third Number:"))

#Type 2

if A>B and A>C:
    print("Largest Number is:",A)
elif B>A and B>C:
    print("Largest Number is:",B)
else:
    print("The Greatest Number is:",C)

print("="*50)
#Type 3

if A>B>C:
    print("Largest Number is:",A)
elif B>A>C:
    print("Largest Number is:",B)
else:
    print("The Greatest Number is:",C)

print("="*50)

# WAP to provide the grade to students as per marka obtained.

Total_Marks=int(input("Enter your total marks:"))

if Total_Marks>=60 and Total_Marks<=100:
    print("Passed with A Grade:")
elif Total_Marks<60 and Total_Marks>=45:
    print("Passed with B Grade:")
elif Total_Marks<45 and Total_Marks>=30:
     print("Passed with C Grade:")
elif Total_Marks>100:
    print("Inavild marks it is not posiible more than 100 marks:",Total_Marks)
else:
    print("Better luck next time")

print("="*50)


Math_Marks=int(input("Enter your total marks in Math:"))
Science_Marks=int(input("Enter your total marks in Science:"))
Arts_Marks=int(input("Enter your total marks in Arts:"))
Hindi_Marks=int(input("Enter your total marks in Hindi:"))
English_Marks=int(input("Enter your total marks in English:"))

Total_Marks=Math_Marks+Science_Marks+Arts_Marks+Hindi_Marks+English_Marks
print("Total Marks is:",Total_Marks)

Percentage=(Total_Marks)//5
print("Total Percentage is:",Percentage)

if Percentage>=60:
    print("Passed with First Division:")
elif Percentage<60 and Percentage>=45:
    print("Passed with Second Division:")
elif Percentage<45 and Percentage>=30:
     print("Passed with Third Division:")
else:
    print("Fail")

print("="*50)

#################### OR CONDITION ######################

# WAP a program input number is divisible by 3 and 7

Number=int(input("Enter a random number:"))

if Number%3==0 or Number%7==0:
    print("Number is divisible by 3 or 7",Number)
else:
    print("Number is not divisible by 3 or 7:",Number)
print("="*50)
# WAP to create a calculator 

'''
Three input from user NUMBER NUMBER1 DECISION
1 FOR ADD
2 FOR SUBTRACT
3 FOR MULTIPLY
4 FOR DIVIED
5 FOR SQUARE
6 FOR CUBE
GREATER THAN 6 INVALID INPUT
'''
NUMBER=25
NUMBER1=5

DECISION=int(input("Enter number:"))

if DECISION==1:
    print("Addition of number:",NUMBER+NUMBER1)
if DECISION==2:
    print("Subtraction of number:",NUMBER-NUMBER1)
if DECISION==3:
    print("Multiply of number:",NUMBER*NUMBER1)
if DECISION==4:
    print("Divide of number:",NUMBER/NUMBER1)
if DECISION==5:
    print("Square of NUMBER:",NUMBER**2,"Square of NUMBER1:",NUMBER1**2)
if DECISION==6:
    print("Cube of NUMBER:",NUMBER**3,"Cube of NUMBER1:",NUMBER1**3)
if DECISION>6:
    print("Invalid input")
print("="*50)
