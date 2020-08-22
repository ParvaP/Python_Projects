def bmi(p, t):
    ## complete your work here ##
    r = p/(t*t)
    ## return something for now
    return r

def print_bmi_level(r):
    ## complete your work here ##
    if r<18.5:
        print ("You are underweight")
    elif r<25:
        print ("You are a normal weight")
    elif r<30:
        print ("You are overweight")
    else:
        print("You are obese")
    return

p = float(input("Enter your weight in kilograms "))
t = float(input("Enter your height in meters "))

r = bmi(p,t)
print("Your BMI is", r)
print_bmi_level(r)
