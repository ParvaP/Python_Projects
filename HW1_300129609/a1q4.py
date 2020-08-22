def convert_year (num_years):
    return num_years*365.26*24*60*60

def convert_ls (light_sec):
    return light_sec*300000

years = float(input("Input the number of light years: "))
sec = convert_year(years)
print("The number of seconds is", sec)
print("The distance is",convert_ls(sec)," km.")
s1 = float(input("Input the distance to the first star, in light years: "))
s2 = float(input("Input the distance to the second star, in light years: "))
print("The distance between the two stars is ",convert_ls(convert_year(s1+s2))," km")