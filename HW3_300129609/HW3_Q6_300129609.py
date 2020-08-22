def roman_v1(li):
    return li.count("M")*1000+li.count("D")*500+li.count("C")*100+li.count("X")*10+li.count("V")*5+li.count("I")

def roman_v2(li):
    total = 0
    for i in li:
        if i == "M":
            total = total + 1000
        elif i == "D":
            total = total + 500
        elif i == "C":
            total = total + 100
        elif i == "X":
            total = total + 10
        elif i == "V":
            total = total + 5
        elif i == "I":
            total = total + 1
    return total


num = input ("Input a roman number using the letters M, D, C, X, V, and I: ")

print (roman_v1(num))
print (roman_v2(num))