import math
def findD(a, b, c):
    D = b**2 - 4*a*c
    return D

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

discriminant = findD(a, b, c)

print(f"The discriminant D is: {discriminant}")
