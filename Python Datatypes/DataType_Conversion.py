################################# Data Type Conversion ###################################')

####################### Integer Datatypes #####################

#  Int to float #

print("="*40)

i=230
f=float(i)
print(f,type(f))

print("="*40)

#  Int to string #

i1=230
S=str(i1)
print(S,type(S)) # 230 <class 'str'>

print("="*40)

# int to list # Conversion is not possible
# int to dict # Conversion is not possible
# int to set  # Conversion is not possible
'''
i1=230
L=list(i1)
print(L,type(L))

# Type error- Int object is not iterable

'''

print("="*40)


# int to complex
i2=569

c=complex(i2)

print(c,type(c)) # (569+0j) <class 'complex'>

print("="*40)

# Default imaginary value will be zero.

# Integer to boolean #

a=0
a1=1
a2=256525
a3=2658

B=bool(a)
B1=bool(a1)
B2=bool(a2)
B3=bool(a3)

print(B, type(B))  # False <class 'bool'>
print(B1, type(B1))# True <class 'bool'>
print(B2, type(B2))# True <class 'bool'>
print(B3, type(B3))# True <class 'bool'>
print("="*40)

# 0 -> False
# 1 to infinity all others number is true.

################### Float Data Types #################

# Float to integer

F=12.25
I=int(F)
print(I,type(F)) # 12 <class 'float'>
print("="*40)

# Float to string
F1=235.365
S=str(F1)
print(S,type(S))  # 235.365 <class 'str'>
print("="*40)

# Indexing

# 2 3 5.  3 6 5
#-7-6-5-4-3-2-1

print(S[-7]) # Indexing 2
print("="*40)
print(S[-6:-2]) # 35.3
print("="*40)

# Float to complex

F2=3.25
C=complex(F2)
print(C,type(C)) # (3.25+0j) <class 'complex'>

print("="*40)

# Float to list # Conversion is not possible.
# Float to dict # Conversion is not possible.
# Float to set  # Conversion is not possible.
# Float to tupple # Conversion is not possible.

# Float to boolean.
F3=0.0
B=bool(F3)
print(B,type(B)) # False <class 'bool'>
print("="*40)

F4=5.56
B1=bool(F4)
print(B1,type(B1)) # True <class 'bool'>
print("="*40)

#################### String Datatype Conversion ###################

# String to integer->
'''
Str="Krishna"
I=int(Str)
print(I,type(I))

    I=int(Str)
ValueError: invalid literal for int() with base 10: 'Krishna'

'''
# If string only contains number than string to int conversion is possible
print("="*40)

Str1="1234"
I1=int(Str1)
print(I1,type(I1)) # 1234 <class 'int'>

print("="*40)

Str2="12346"
I2=int(Str2)
print(I2,type(I2)) # 12346 <class 'int'>



#Multiply with 5 converted string
print("="*40)

print("Multiply with 5:",i1*5)

print("="*40)

# String to float 

# Note:- If string only contains float vlaue than string to float conversion is possible

Str3="12346.52"
I3=float(Str2)
print(I3,type(I3)) # 12346.52 <class 'float'>

print("="*40)

Str4="12346"
I4=float(Str4)
print(I4,type(I4)) # 12346.00 <class 'float'>

print("="*40)

# String to complex

Str5="52"
C=complex(Str5)
print(C,type(C)) # (52+0j) <class 'complex'>

print("="*40)

Str6="52+5J"
C1=complex(Str6)
print(C1,type(C1)) # (52+5j) <class 'complex'>

print("="*40)

Str7="52j"
C2=complex(Str7)
print(C2,type(C2)) # 52j <class 'complex'>

# To find the real number and imaginary number

print("Real number is :",C2.real) #  0.0

print("="*40)

print("Real number is :",C2.imag) # 52.0

print("="*40)

# String to list

Str8="krishna 123456"

L=list(Str8)
print(L,type(L),L[5]) # ['k', 'r', 'i', 's', 'h', 'n', 'a', ' ', '1', '2', '3', '4', '5', '6'] <class 'str'> n

print("="*40)

# String to tuple

Str9="123.45 1234 krishna"

T=tuple(Str9)
print(T,type(T),T[5]) # ('1', '2', '3', '.', '4', '5', ' ', '1', '2', '3', '4', ' ', 'k', 'r', 'i', 's', 'h', 'n', 'a') <class 'tuple'> 5

print("="*40)

# String to dictionary
'''
Str10="123.45 1234 krishna"

D=dict(Str10)
print(D,type(D),D[5]) #

 D=dict(Str10)
ValueError: dictionary update sequence element #0 has length 1; 2 is required

'''
# Note:-
# Import the JSON Module: Start by importing the json module to access the loads() function.
# Define Your JSON String: Ensure your string is properly formatted as JSON. 
# This means using double quotes for keys and string values, and correct syntax for objects and arrays.
# Use json.loads(): Pass your JSON string to json.loads(), which will parse it into a Python dictionary.

import json
Str11='{"A":123,"B":564,"C":456}'

D1=json.loads(Str11)
print(D1,type(D1)) # {'A': 123, 'B': 564, 'C': 456} <class 'dict'>
print("="*40)

print(D1["B"]) # 564

print("="*40)

# String to 




