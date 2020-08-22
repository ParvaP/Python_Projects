def in_out(xs,ys,side):
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))
    checker = x >= xs and x <= xs + side and y > ys and y <= ys+side
    return checker

xss = float(input("Enter and x value for the bottom left of a square: "))
yss = float(input("Enter and y value for the bottom left of a square: "))
sides = float(input("Enter a side length for the square: "))
print (str(in_out(xss,yss,sides)))
