                                ############ CLASS : 1 ############
############################################ Variable  ######################################################
# What is variable?
#-> A variable is a reserved memory location to store values. 
#-> variables are created when you assign a value to them using the assignment operator (=).

A=10
# : A is variable.
# : = is Assignment Opreator.
# : 10 is value.

print("==============================================================================")

print(A)

print(A,id(A)) # 140723957540040

B=20

print(A)

print(B,id(B)) # 140723957540360


# Note- Every diffrent variable holding diffrent value will have diffrent address.

########### Two Variable have same value #############

# If two varibale is same value then address will same 

print("==============================================================================")

X=40
Y=40

print("X:", X,"Address:",id(X)) # 140723957541000

print("Y:", Y,"Address:",id(Y)) # 140723957541000

##### How to assign multiple value to multiple value at a time #####

print("==============================================================================")

P,Q,R=50,60,70
print("Value Of p:", P)
print("Value Of Q:", Q)
print("Value Of R:", R)

print("Value of P,Q,R:",P,Q,R) # Value of P,Q,R: 50 60 70

                           ####### -:Assign same value to multiple variable:- ########
print("==============================================================================")

a=b=c=120

print("Value of a:",a,id(a)) # Value of a: 120 = 140724971319944
print("Value of b:",b,id(b)) # Value of b: 120 = 140724971319944
print("Value of c:",c,id(c)) # Value of c: 120 = 140724971319944

                           ####### Rules to declare variables ########
print("==============================================================================")
# 1. Variable name can not start with number
# Example
# 123krishna = 12 - Wrong
Krishna123= 12 # Right

# 2. Variable name not have space in the name.
# Example
# Krishna Murari= 12 Wrong
KrishnaMurari= 12 # Right

# 3. There is no spacfic length for variable.

Var_name_has_not_Limit_Length=123
print("The Id of variablr:",Var_name_has_not_Limit_Length,(id)(Var_name_has_not_Limit_Length))

# 4. Python is case-sesitive, variable name will treat diffrently with diffrent case.
# Example
print("==============================================================================")
Name='Krishna'
nAme='Rahul'
NamE='Murari'
NAME='Kumar'

print(Name,nAme,NamE,NAME) # Single line print

print("==============================================================================")

print(Name + "\n" + nAme + "\n" + NamE + "\n" + NAME) # Multiple line print.

print(Name, nAme, NamE, NAME, sep="\n") # Using sepreator for multiple line.

# 5. Can not use special character in variable name expect underscore('_').
# Example
# Krishna#=123  Wrong
# Murari%=234   Wrong

Krishna_M=123 # Right

# 6. Can not use as variable inbuilt variable
# Example
# true=700 Wrong
# class=300 Wrong

################################## Python have 36 keyword ###################################
print("==============================================================================")
import keyword
print(keyword.kwlist) 
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 
 
"""
                                ############ CLASS : 2 ############

""" 
                                       -:Math Opreations:-
+ : Plus opreator
- : Subtraction opreator
* : Multiplication
/ : Divide with single /
// : Divide with double //
% : Reminder Opreator
** : Power opreator
== : Equal Opreator
!= : Equal not opreator

"""
# + : Plus opreator

# Addition of two number 
print("==============================================================================")
N1=40 
N2=30
print("Addition of N1+N2=:",N1+N2)

# Addition of two String
print("==============================================================================")
Name="Krishna Murari"
Say="Good Morning"
print("Addition of string",Name+Say)     # Without space
print("Addition of string",Name+" "+Say) # With space

# - : Subtraction opreator
print("==============================================================================")
M1=500
M2=600
print("Subtraction of M1-M2=",M1-M2) # -100

print("Subtraction of M2-M1=",M2-M1) # 100

# * : Multiplication
print("==============================================================================")

Q1=58
Q2=78
print("Multiply of Q1*Q2=",Q1*Q2) # 4524

# Multiply with string
# Note: We multiply the string with number then it will repeat the string that number of time
print("==============================================================================")

Z1="Krishna"
Z2=5
print("Multiply string with number:",Z1*Z2) # KrishnaKrishnaKrishnaKrishnaKrishna

print("==============================================================================")
# Draw a line
print("/"*10) # //////////

# / : Divide with single / 
# Note: Return with flot and pointer output
print("==============================================================================")
D1=52  
D2=50
print("Divided with single line:",D1/D2) #1.04

# / : Divide with double // 
# Note: Return integer output or whole number
print("==============================================================================")
D1=52
D2=50
print("Divided with single line:",D1//D2) #1

# % : Reminder Opreator
# Note: Return only reminder value.
print("==============================================================================")
R1=586
R2=256
print("Reminder is:",R1%R2) # 74

# ** : Power opreator
print("==============================================================================")

P1=5
print("Square of P1:",P1**2) #25
print("Cube of P1:",P1**3)   # 125

# Solve this equation (a+b)^2=a^2+b^2+2ab
print("==============================================================================")
a=5
b=6
LHS= (a+b)**2
RHS= a**2+b**2+2*a*b
print('LHS=RHS',LHS,"=",RHS)

# WAP (a+b)^3 = a^3+b^3ab(a+b)
print("==============================================================================")
a=5
b=6
LHS= (a+b)**3
RHS= a**3+b**3+3*a*b*(a+b)
print("Formula of (a+b)^3",'LHS=RHS',LHS,"=",RHS) # 1331

# WAP (a-b)(a+b)=a^2-b^2
print("==============================================================================")
a=5
b=6
LHS= (a+b)*(a-b)
RHS= a**2-b**2
print("Formula of a^2-b^2",'LHS=RHS',LHS,"=",RHS) # -11

# WAP a^3+b^3=(a-b)**3+3ab(a-b)
print("==============================================================================")
a=5
b=6
LHS= a**3-b**3
RHS= (a-b)**3+3*a*b*(a-b)
print("Formula of a^3+b^3",'LHS=RHS',LHS,"=",RHS) # -91

# WAP Pythagorean theorem
print("==============================================================================")
L=12
b=15
H=L**2+b**2
print("Pythagorean theorem",H)

# WAP Calculate the area of circle
# Formula Area=πr^2
print("==============================================================================")
r=14
π=22/7
Area=π*r**2
print("Area of circlr is:",Area)

# WAP for simple intrest
# Formula= P*R*T/100
print("==============================================================================")
P=2000
R=10
T=5
Simple_Intrest=(P*R*T)/100
print("Simple intrest is:",Simple_Intrest)

# WAP compound intrest 
# Formula P(1+r/100)^t
print("==============================================================================")

P=2000
R=10
T=5
A= P*(1+R/100)**T
CI=(P*(1+R/100)**T)-P
print("Amount is:",A)
print("Compound intrest:",CI)


########################### Interview question for variable in python ###################################
"""
 1. What is variable in python?
 Ans: A variable is a reserved memory location to store values. 
 variables are created when you assign a value to them using the assignment operator (=).

 2. How do you declare and initialize a variable in Python?
 Ans: You declare and initialize a variable in Python by writing the variable name followed by the assignment 
 operator (=) and the initial value.
 For example: x = 100.

 3.Are variable names case-sensitive in Python?
 And: Yes, variable names are case-sensitive in Python. 
 For example, `myVar` and `myvar` are treated as different variables.

 4. What are the rules for naming variables in Python?
 Ans: Variable names in Python must start with a letter (a-z, A-Z) or an underscore (_), 
 followed by letters, digits (0–9), or underscores. 
 Variable names cannot start with a digit. Python keywords cannot be used as variable names.

 5. What is the difference between local and global variables in Python?
 Ans: Local variables are defined within a function and can only be accessed within that function. 
 Global variables are defined outside of any function and can be accessed from any part of the program.
 
 6. How do you change the value of a variable in Python?
 Ans: You can change the value of a variable in Python by simply assigning a new value to it using the assignment operator (=). 
 For example: ‘x = 20’ will change the value of x to 20.

 7. Can you reassign a variable to a different data type in Python?
 Ans: Yes, Python allows you to reassign a variable to a different data type. 
 For example, you can assign an integer to a variable and later assign a string to the same variable.

 8. What happens if you try to access a variable that has not been defined?
 Ans: If you try to access a variable that has not been defined (i.e., not declared or initialized), 
 Python will raise a `NameError` indicating that the variable is not defined.

 9. What is the purpose of the id() function in Python?
 Ans: The id() function in Python is used to get the identity of an object.This identity is a unique integer that represents the object. 
 The id() function returns the memory address of the object in Python, the default implementation of Python.

 10. What is dynamic typing?
Ans: Dynamic typing is a feature of Python where the type of a variable is determined at runtime,
and you can change the type of a variable by assigning a new value of a different type to it.
"""
