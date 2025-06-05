# 16. WAp to find the area of cylinder.

# Formula= 2*PI*r*h + 2*PI*r*r

R=int(input("Enter the Radius of cylinder:"))
H=int(input("Enter the Height of cylinder:"))
PI=3.14
Area=2*PI*R*H + 2*PI*R**2
print("Area of Cylinder:",Area)
