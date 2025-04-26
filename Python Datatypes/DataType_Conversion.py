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

# Float to list # Conversion is not possible
# Float to dict # Conversion is not possible
# Float to set  # Conversion is not possible




