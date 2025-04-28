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













