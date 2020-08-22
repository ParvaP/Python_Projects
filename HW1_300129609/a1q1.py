import math
def pythagorean_pair(a,b):
    c = math.sqrt(a*a+b*b)
    return c%1 == 0


A = int(input("Enter a vaule for a: "))
B = int(input("Enter a value for b: "))

print(str(pythagorean_pair(A,B)))