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

# String to  set
Str12="krishna 123456"
Set=set(Str12)
print(Set,type(Set)) # {'1', 'k', 'h', 'n', 'a', ' ', 'r', '3', '6', '5', '2'} <class 'set'>
print("="*40)

# String to boolean
Str13="krishna" 
Bool=bool(Str13)
print(Bool,type(Bool)) # True <class 'bool'>
print("="*40)

Str14=""
Bool1=bool(Str14)   
print(Bool1,type(Bool1)) # False <class 'bool'>
print("="*40)

Str15="0"
Bool2=bool(Str15)   
print(Bool2,type(Bool2)) # True <class 'bool'>
print("="*40)   

Str16="1"
Bool3=bool(Str16)   
print(Bool3,type(Bool3)) # True <class 'bool'>
print("="*40)

Str17="0.0"
Bool4=bool(Str17)
print(Bool4,type(Bool4)) # True <class 'bool'>
print("="*40)

Str18="0.0000"
Bool5=bool(Str18)
print(Bool5,type(Bool5)) # True <class 'bool'>
print("="*40)

# String to bytes
Str19="krishna"
B=bytes(Str19,encoding="utf-8")
print(B,type(B)) # b'krishna' <class 'bytes'>
print("="*40)

# String to bytearray
Str20="krishna" 
Bt=bytearray(Str20,encoding="utf-8")
print(Bt,type(Bt)) # bytearray(b'krishna') <class 'bytearray'>  
print("="*40)

####################### List Datatypes Conversion #######################
# List to int-> Conversion is not possible.

# List to float-> Conversion is not possible.

# List to string
List=["krishna",123,456,789]
Str= str(List)
print(Str,type(Str)) # ['krishna', 123, 456, 789] <class 'str'>
print("="*40)

# Indexing
print(Str[0],Str[5],Str[4],Str[-1]) # [ s i ]
print("="*40)

# List to tuple
List1=[1,2,3,4,5,(12,25,65,25),{"krishna":123,"ram":456}]
T=tuple(List1)  
print(T,type(T)) # (1, 2, 3, 4, 5) <class 'tuple'>
print("="*40)

# indexing
print(T[0],T[1],T[2],T[3],T[-1]) # 1 2 3 4 {'krishna': 123, 'ram': 456}

print("="*40)

# List to dictionary-> Dirct Conversion is not possible.
# but we can convert list to dictionary using zip() function.
# Note:- The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.  
# The returned object is a zip object, which is an iterator of tuples.
# The list should be in pair.
# Example:
List1=[1,2,3,4,5,(12,25,65,25),{"krishna":123,"ram":456}]
List2=["krishna","ram","sita","gita"]
D=dict(zip(List1,List2))  
print(D,type(D)) # {1: 'krishna', 2: 'ram', 3: 'sita', 4: 'gita'} <class 'dict'>
print("="*40)

# List to set
List3=[1,2,3,4,5,]
Set=set(List3)
print(Set,type(Set)) # {1, 2, 3, 4, 5} <class 'set'>
print("="*40)

# List to boolean
List4=[1,2,3,4,5]
Bool=bool(List4)    
print(Bool,type(Bool)) # True <class 'bool'>
print("="*40)

List5=[]
Bool1=bool(List5)   
print(Bool1,type(Bool1)) # False <class 'bool'>
print("="*40)

List6=[0,0,0,0,0]
Bool2=bool(List6)
print(Bool2,type(Bool2)) # True <class 'bool'>
print("="*40)

############################### Tuple Datatypes Conversion ###############################
# Tuple to int-> Conversion is not possible.
# Tuple to float-> Conversion is not possible.
# Tuple to complex-> Conversion is not possible.
# Tuple to string
t=(1,2,3,4,5,6,7,8,9)
Str=str(t)  
print(Str,type(Str)) # (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'str'>
print("="*40)   

# Indexing
print(Str[0],Str[1],Str[2],Str[3],Str[-1]) # ( 1 ,   )
print("="*40)

# Tuple to list
t1=(1,2,3,4,5,6,7,8,9)
L=list(t1)
print(L,type(L)) # [1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>
print("="*40)

# Tuple to dictionary-> Dirct Conversion is not possible.
# but we can convert tuple to dictionary using zip() function.
# Note:- The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
# The returned object is a zip object, which is an iterator of tuples.
# The tuple should be in pair.
# Example:
t1=(1,2,3,4,5,6,7,8,9)
t2=("krishna","ram","sita","gita")
D=dict(zip(t1,t2))
print(D,type(D)) # {1: 'krishna', 2: 'ram', 3: 'sita', 4: 'gita'} <class 'dict'>
print("="*40)

# Tuple to set
t2=(1,2,3,4,5,6,7,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15)
Set=set(t2)
print(Set,type(Set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15} <class 'set'>
print("="*40)

# Tuple to boolean
t3=(1,2,3,4,5)
Bool=bool(t3)   
print(Bool,type(Bool)) # True <class 'bool'>
print("="*40)

t4=()
Bool1=bool(t4)  
print(Bool1,type(Bool1)) # False <class 'bool'>
print("="*40)

t5=(0,0,0,0,0)
Bool2=bool(t5)
print(Bool2,type(Bool2)) # True <class 'bool'>
print("="*40)


############################## Dictionary Datatype conversion ##############################

# Dictionary to integer -> Conversion is not possible
# Dictionary to float -> Conversion is not possible
# Dictionary to Complex -> Conversion is not possible

# Dictionary to string
Dic={'A':125,'B':258,'C':156}
Str=str(Dic)
print(Str,type(Str)) # {'A': 125, 'B': 258, 'C': 156} <class 'str'>

print("="*40)

print("################  Indexing    ######################")

print(Str[6],Str[-6])

print("="*40)

# Dictionary to list

Dic={'A':125,'B':258,'C':156}
List=list(Dic)
print(List,type(List)) # ['A', 'B', 'C'] <class 'list'>

print("="*40)

print("################  Indexing    ######################")

print(List[2],List[-2]) # C B

print("="*40)

# Dictionary to tuple

Dic={'A':125,'B':258,'C':156}
Tup=tuple(Dic)
print(Tup,type(Tup)) # ('A', 'B', 'C') <class 'tuple'>

print("="*40)

print("################  Indexing    ######################")

print(Tup[2],Tup[-2]) # C B

print("="*40)

# Dictionary to set

Dic={'A':125,'B':258,'C':156}
Set=set(Dic)
print(Set,type(Set)) # {'A', 'C', 'B'} <class 'set'>

print("="*40)

print("################  Indexing    ######################")

# print(Set[2],Set[-2]) # C B

print("="*40)

# Dictionary to boolean

Dic={'A':125,'B':258,'C':156}
Bool=bool(Dic)
print(Bool,type(Bool)) # True <class 'bool'>
print("="*50)

Dic={}
Bool1=bool(Dic)
print(Bool1,type(Bool1)) # False <class 'bool'>
print("="*50)

############ Set Datatype Conversion ################

# Set to integer -> Conversion is not possible
# Set to float -> Conversion is not possible
# Set to Complex -> Conversion is not possible
# Set to dictionary conversion is not possible.

# Set to string
Set={25,65,.35,36,(2,5,.36,3.5),"Krishna"}
Str=str(Set)
print(Str,type(Str)) # {0.35, 65, (2, 5, 0.36, 3.5), 'Krishna', 36, 25} <class 'str'>

print("="*40)

print("################  Indexing    ######################")

print(Str[5],Str[-6]) # , s

print("="*40)

# Set to list

Set={25,65,.35,36,(2,5,.36,3.5),"Krishna"}
List=list(Set)
print(List,type(List)) # [0.35, 65, (2, 5, 0.36, 3.5), 36, 'Krishna', 25] <class 'list'>

print("="*40)

print("################  Indexing    ######################")

print(List[5],List[-6]) # 25 0.35

print("="*40)

# Set to tuple

Set={25,65,.35,36,(2,5,.36,3.5),"Krishna"}
Tup=tuple(Set)
print(Tup,type(Tup)) # (0.35, 65, (2, 5, 0.36, 3.5), 36, 'Krishna', 25) <class 'tuple'>

print("="*40)

print("################  Indexing    ######################")

print(Tup[5],Tup[-6]) # 25 0.35

print("="*40)

# Set to boolean 
Set={25,65,.35,36,(2,5,.36,3.5),"Krishna"}
Bool=bool(Set)
print(Bool,type(Bool)) # True <class 'bool'>

print("="*40)

Set={}
Bool=bool(Set)
print(Bool,type(Bool)) # False <class 'bool'>

print("="*40)

# Boolean datatype conversion

# Boolean to list -> Conversion is not possible
# Boolean to tuple -> Conversion is not possible
# Boolean to dictionary -> Conversion is not possible
# Boolean to set-> conversion is not possible.

# Boolean to int
Bool=True
Int=int(Bool)
print(Int,type(Int)) # 1 <class 'int'>
print("="*40)

Bool=False
Int=int(Bool)
print(Int,type(Int)) # 0 <class 'int'>
print("="*40)

# Boolean to float
Bool=True
Float=float(Bool)
print(Float,type(Float)) # 1.0 <class 'float'>
print("="*40)

Bool=False
Float=float(Bool)
print(Float,type(Float)) # 0.0 <class 'float'>
print("="*40)

# Boolean to complex

Bool=True
Com=complex(Bool)
print(Com,type(Com)) # (1+0j) <class 'complex'>
print("="*40)

Bool=False
Com=complex(Bool)
print(Com,type(Com)) # 0j <class 'complex'>
print("="*40)

# Boolean to string

Bool=True
Str=str(Bool)
print(Str,type(Str)) # True <class 'str'>
print(Str[3],Str[-2]) # Indexing   (e u)
print("="*40)

Bool=False
Str=str(Bool)
print(Str,type(Str)) # False <class 'str'>
print(Str[3],Str[-2]) # indexing (s s)
print("="*40)














