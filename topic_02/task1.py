def findD(a, b, c):
    D = b**2 - 4 * a * c
    return D

def FindRoots(a, b, c):
    D = findD(a, b, c)
    
    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        return x1, x2
    elif D == 0:
        x1 = -b / (2 * a)
        return x1,
    else:
        return None

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

roots = FindRoots(a, b, c)

if roots:
    if len(roots) == 1:
        print(f"The equation has one real root: {roots[0]}")
    else:
        print(f"The equation has two real roots: {roots[0]} and {roots[1]}")
else:
    print("The equation has no real roots.")
