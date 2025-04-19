
############################################ Python Datatypes ##########################################
# What is Datatype?
# -> Datatype is a classification of data items. It tells the compiler or interpreter what type of value a variable can hold.

# Types of python Datatypes:

# 1 Number
# What is Number?
# -> Number is a datatype which is used to represent numeric values. It can be positive or negative whole numbers or decimal numbers.
# Tpyes of Number:
  #  1) Integer Number # Immutable
  #  2) float Number   # Immutable
  #  3) complex Number # Immutable

################ Integer Number ##################
# What is Integer Number?
# -> Integer is a datatype which is used to represent whole numbers. It can be positive or negative whole numbers.

# type(Variable name): Know the datatypes

print("########### Integer Number ##########")
n1 = 30
print(n1, type(n1))  # Output: 30 <class 'int'>
"""
# Note:-
# Integer is a immutable data type. once it is define cannot change.
# There is no limit for integer data type.
# Integer always consider whole number.
"""
n2=25654585255225856325565255562552552552553255632566355662556
print(n2,type(n2)) # Integer

n3=0
print(n3,type(n3)) # Integer

n4=-52852552
print(n4,type(n4)) # Integer

# When we add two integer value always return integer value

a1=52
a2=45
Sum=a1+a2
print(Sum,type(Sum)) # Integer

print("########### Float Number ##########")
# What is Float Number?
# Float is a datatype which is used to represent decimal numbers. It can be positive or negative decimal numbers.

############################## Float Number #############################
f=12.05
print(f,type(f)) # Float

"""
Notes:
# Float is immutable data type.
# There is no specific limit for float data type.
# All the pointer values will be consider as float.(Both postive and negative)
"""
f1=5522.00
print(f1,type(f1))

f2=.00
print(f2,type(f2))

f3=.256
print(f3,type(f3))

f4=0.0
print(f4,type(f4))

print("####################### Complex Number ################################")

############################## Complex Number ################################
'''
# What is Complex Number?
# Complex number is a datatype which is used to represent complex numbers. It can be positive or negative complex numbers.
# Complex number is represented in the form of a+bj where a is real part and b is imaginary part.
# Complex number is a immutable data type.  
'''
c=20+36j
print(c,type(c))

c1=20+25j+56+34j
print(c1,type(c1))

c2=20+25j-56+34j
print(c2,type(c2))

c3=20+25j*56+34j
print(c3,type(c3))

c4=20.36+25j*56.25+34.25j
print(c4,type(c4))

# Real number and Imaginary number
c6=256+65j
print("Real number is",c6.real)
print("Imaginary number is",c6.imag)

##################################### Sequential Datatypes #############################
# What is Sequential Datatypes?
# Sequential datatypes are those datatypes which are used to store multiple values in a single variable.
'''
# 2 Sequential Datatypes types
  #  A) String # Immutable
  #  B) List   # Mutable
  #  C) Tupple # Immutable

'''

print("############################## String Datatype #################################")

"""
Properties of string:-
-> String is immutable datatype it can not be modifiy.
-> Anything with single/double/tripple qoute will consider as string.
-> String follow +ve and -ve indexing.
   +ve starts from 0
Example:-
+ve indexing
0 1 2 3 4 5 6
K R I S H N A 
-7 -6 -5 -4 -3 -2 -1
-ve indexing
"""
print("="*30)
s=''
s1=" "
s2=('A')
s3=("B")
s4=('Krishna')
s5=("Good Morning Krishna")
print(s,type(s))
print("="*30)
print(s1,type(s1))
print("="*30)
print(s2,type(s2))
print("="*30)
print(s3,type(s3))
print("="*30)
print(s4,type(s4))
print("="*30)
print(s5,type(s5))
print("################### Indexing ############################")
# What is Indexing?
# -> Indexing is used to access the elements of a string. It is done by using the index number of the element.
In="KRISHNA"
print(In)
print("="*30)
print(In[0])
print("="*30)
print(In[-6])
print("="*30)
print(In[2])
print("="*30)
print(In.index('K'))
print("################ Slicing #########################")
print(In[2:4])

print("################### Length of string ############################")
L="KRISHNA Murari"
Len=len(L)
print("Length of String:",Len)

print("##################################### List Datatype ###############################")
# What is List?
# -> List is a datatype which is used to store multiple values in a single variable. It can be of any datatype.
# -> List is a mutable datatype. It can be modified.
# -> List is defined by using square brackets [].
# -> List can contain any datatype. It can be of any type.
# -> List can contain duplicate values.
List=[12,1,23.4,'krishna',.025,00,-65,-.025]



