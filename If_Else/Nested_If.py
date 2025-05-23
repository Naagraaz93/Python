'''
if condition1:
    # Code for condition1 is true
    code_block_1

    if condition2:
        # Code for both condition1 and condition2 are true
        code_block_2

        if condition3:
            # Code for condition1, condition2, and condition3 are true
            code_block_3

        else:
            # Code for condition1 and condition2 are true, but condition3 is false
            code_block_4

    else:
        # Code for condition1 is true, but condition2 is false
        code_block_5

else:
    # Code for when condition1 is false
    code_block_6
'''
# WAP to complete interview process.

Round_1="Pass" 

Round_2="Fail" 

Round_3="Pass"

HR_Round="Fail"

if Round_1=="Pass":
    print("Congrats your first round is cleared:")
    if Round_2=="Pass":
        print("Congrats your first round is cleared:")
        if Round_3=="Pass":
            print("Congrats your third round is cleared:")
            if HR_Round=="Pass":
                print("Congrats You are selected:")
            else:
                print("Sorry: you Failed in HR_Round:")
    else:
        print("You failed in Round_2: Please try again")
else:
    print("You Failed in first round:")

# WAP to check number negative or postive.

Num=int(input("Enter a number:"))

if Num>=0:
    print("This is postive number:")
else:
    print("This is negative number:")

print("="*50)

# WAP check odd and even number.

# Write if condition in single line

# Method 1

Num=int(input("Enter a number:"))

Result= "Even" if Num%2==0 else "Odd"

print("Enterd Number is:",Result)

print("="*50)

# Method 2

Num1=int(input("Enter a number:"))

print("Enterd Number is:","Even" if Num1%2==0 else "Odd")

# WAP to check any person can give vote or not.

Age=int(input("Enter a number:"))

# Method 1

if Age >=18:
    print("You can give vote:")
else:
    print("You can't vote ")
    
# Method 2

print("You can give vote "if Age>=18  else "You can't vote")

# Method 3

Result= "You can give vote " if Age>=18  else "You can't vote"

print(Result)

print('='*50)

# WAP to calculate the bill amount the basic of Electricity consumption.
'''
1 to 100-> 5 rs
100 to 120-> 10 rs/Unit
120 to 150-> 15 rs/Unit
150 to 200-> 20 rs/Unit
More than 200-> 25 rs/Unit
'''



Unit=int(input("Enter Electricity Unit:"))

if Unit<=100:
   EC=Unit*5
   print("Total Electricity consumption is:",EC)
elif Unit>100 and Unit<=120:
      EC=Unit*10
      print("Total Electricity consumption is:",EC)
elif Unit>120 and Unit<=150:
         EC=Unit*15
         print("Total Electricity consumption is:",EC)
elif Unit>150 and Unit<=200:
           EC=Unit*20
           print("Total Electricity consumption is:",EC)
else:
   EC=Unit*25
   print("Total Electricity consumption is:",EC)
print("="*50)

# Method 2

Unit = int(input("Enter Electricity Unit: "))

if Unit <= 100:
    EC = Unit * 5
elif Unit <= 120:
    EC = Unit * 10
elif Unit <= 150:
    EC = Unit * 15
elif Unit <= 200:
    EC = Unit * 20
else:
    EC = Unit * 25

print("Total Electricity consumption is:", EC)

# To check value is available in list or not

# Method 1
List=[20,30,50,40,60,70,80,90,100]
Val = int(input("Enter a value: "))

Result=True if Val in List else False

print("Result:",Result)

# Method 2

if Val in List:
    print("Value is available in list:",Val)
else:
    print("Value is not available in list:",Val)