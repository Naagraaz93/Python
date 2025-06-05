'''
for conditions:
    code
'''
# Range (Start , Stop, Difference)
# When we run loop with range then include the start value and exclude stop value.

# Range with 2 parameter range (Start, Stop), default difference value will be one
for i in range(1,10):
    print(i)

print("="*50)

for i in range(0,20,2): # Increment by 2
    print(i)
print("="*50)

# Print the negative value in reverse order.

for j in range(-10,0,1):
    print(j,end=" ")
print()
print("="*50)

# Range class rule:-
'''
--> Range accepts three parameters range(Start, Stop, Step).
--> Range output include start value and exclude stop value.
--> If don' define the initial value and step value then
      Default initial value start from (0)
      Defualt step value will be 1
      Example :-
      range(30)--> (0,30,1)
--> Range parameter accepts only int value.
--> If we define two parameter in the range, then it will consider start value, 
    Stop value default step value will we 1. 
    Example:-
    range(2,10)--> Start=2 Stop=10, Step=1

'''
###################################################################################
# How to apply condition in loop

# WAP get all the number divided by 7 from 1 to 100.

for i in range(1,100):
    if i%7==0:
        print(i,end=" ")
print("="*50)

# WAP the table of any given number.

Number=int(input("Enter A Number:"))
for i in range(1,11):
    print(i,"*","=",i*Number)

###################### Apply loop on list ##################
List=[20,30,40,50,60,70,80,90,100]
List1=[]

for i in List:
    print(i,"=",i**2)
    List1.append(i+2)
    print(List1)

print("="*50)


# WAP to print numbers that are divisible by 5 or 7 in a given range (say, from 1 to 100):

for i in range(1,100):
    if i%5==0 and i%7==0:
        print(i,end=" ")
print()
print("="*50)


# WAP to print the square and cube of numbers in a given range:

for num in range(1, 11):
    square = num ** 2
    cube = num ** 3
    print(f"Number: {num}, Square: {square}, Cube: {cube}")