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