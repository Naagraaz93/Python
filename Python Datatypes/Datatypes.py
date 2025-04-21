
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

########################################### List Data Types ###########################

print("##################################### List Datatype ###############################")
# What is List?
# -> List is a datatype which is used to store multiple values in a single variable. It can be of any datatype.
# -> List is a mutable datatype. It can be modified.
# -> List is defined by using square brackets [].
# -> List can contain any datatype. It can be of any type.
# -> List can contain duplicate values.

List=[12,1,23.4,'krishna',.025,00,-65,-.025]

print(List) # [12,1,23.4,'krishna',.025,00,-65,-.025]
print("="*30)

List1=['krishna',100,20.50,.25,5000,bool,"Murari"]

print(List1)
print("="*30)

# To add another value in list1
# Append method is use to add value in exixting list

List1.append(500)
print(List1)
print("="*30)

# To know all types are method in python
print(dir(list))

'''
# These are method 

 ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__
 __doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__
 '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__
 '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__
 '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear
 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
print("="*30)

# Indexing
List2=[(10.20,30),23.45,67,(123,345,'Krishna'),"murari"]

[(10.20,30),23.45,67,(123,345,'Krishna'),"murari"]
#   0         1   2         3               4 = Positive
#   -5       -4  -3         -2             -1 = Negative

# Get (123,345,'Krishna') from list
print(List2[3])
print("="*30)

# Get murari from list
print(List2[-1])
print("="*30)

# Get 23.45,67 from list
print(List2[1],List2[2])
print("="*30)

# Get (10.20,30) and murari from list
print(List2[-5],List2[-1]) # (10.2, 30) murari
print("="*30)

# Get 30 from list
print(List2[-5][1]) # 30
print("="*30)

# Get 30 from list
print(List2[0][1]) # 30
print("="*30)

List3=[('Krishna','Rajeev','Shubham'),('Murari','Pandey',"Kumar")]

# Get 'Krishna Murari' Rajeev Pandey' 'Shubham Kumar' from list3
print(List3)
print(List3[0][0],List3[1][0]) # Krishna Murari
print(List3[0][1],List3[1][1]) # Rajeev Pandey
print(List3[0][2],List3[1][2]) # Shubham Kumar
print("="*30)

############################### Tupple Data type #####################################

print("############################### Tupple Datatype #####################################")

Tup1=(5,56,25,65,24,36,'Krishna',566.25,True,[6,9,0],(2,6))

print(Tup1)
print("="*30)

'''
Properties:

1. Tupple is immutable data types, its once defined we can not change.
2. Tupple can contain all types of datatype.
3. Tupple follow positive and negative indexing
4. Tupple defined with round bracket ().

'''


# Dir return list of methods belongs to specific class

print(dir(Tup1)) # 
print('='*40)

print("#"*20," Indexing ","#"*20)

# Tup1=    (5,56,25,65,24,36,'Krishna',566.25,True,[6,9,0],(2,6))
# Positive= 0 1  2  3  4  5       6      7     8      9      10
# Negative -11-10 -9 -8  -7 -6   -5    -4     -3      -2   -1 

# Get [6,9,0] from tuppl1
print(Tup1[9]) # [6, 9, 0]
print("="*40)

# Get 9 from tupple1.
print(Tup1[9][1]) # 9
print("="*40)

# Get 'Krishna from tupple1.
print(Tup1[-5]) # Krishna
print("="*40)

# Get 5,56,25,65,24,36 from tupple1.
print(Tup1[0:6]) # 5,56,25,65,24,36
print("="*40)

print("#"*20," ","Count", "#"*20)

Tup2=(25,65,25,95,35,25,65,25,98,100,58,25,100,658,100)

print(Tup2)
print("="*40)

# Count= This method is use to how many times same number in Tup2

# How many times 25 in Tup2
print(Tup2.count(25)) # 5
print("="*40)

# How many times 100 in Tup2
print(Tup2.count(100)) # 3

############################ Dictionary Data Types #######################################

print("#"*20,"  Dictionary Datatypes ","#"*20)

Dic1={'A':200,'B':300,'C':500}
print(Dic1)
print(Dic1,type(Dic1)) # Dict
print('='*40)

'''
Properties :

1. Dictionary data type is mutable we can modify and update.
2. Dictionary only contains unique key, Duplicate key are not allowed
3. Dictionarystore data in key value format
4. Dictionary only contain imuutable data type as key int, float, string, tuple, boolean,
list, dict, set only key in dict. 
5. Dictionary contains all diffrent data types as value
6. Dictionary does not follow indexing
7. Dictionary follow LIFO ( Last in First Out)

'''
Dict={'Name':'Krishna','Age':30,'City':'Noida','Email':'Krishna@gmail.com'}
print(Dict['Name'])
print('='*40)
print(Dict['Age'])
print('='*40)
print(Dict['City'])
print('='*40)
print(Dict['Email'])
print('='*40)

# Add New data in Dict
Dict['Mobile']=99256254285
print(Dict)
print('='*40)
print(Dict['Mobile'])
print('='*40)

# Popitem is use to remove the latest data
Dict.popitem()
print(Dict)
print('='*40)

# Remove specific data from Dictionary

Dict.pop('City')
print(Dict)
print('='*40)

Emp_Data={'Emp_name':'Krishna','Emp_sal':50000,'Emp_City':'Noida'}
V=800

Dict1={
    123:3.5,
    3.5:123,
    23:'Python',
    'Hello':(12,13,25,36,58),
    (4,5,3):{'a':1234,'b':569},
    V:'Program',
'Emp_Details':'Emp_Data'
}
print(Dict1)

