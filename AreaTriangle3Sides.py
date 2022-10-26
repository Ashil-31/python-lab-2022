#Area of Triangle with 3 sides
import math
a=int(input("Enter Side 1:"))
b=int(input("Enter Side 2:"))
c=int(input("Enter Side 3:"))
s=(a+b+c)/2
print(s)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area",area)

      