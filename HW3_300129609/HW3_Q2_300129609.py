def two_length_run(li):
    for i in range(0,len(li)):
        li[i] = float(li[i])
    for i in range(0,len(li)-1):
        if li[i] == li[i+1]:
            return True
    return False


li = input("Please input a list of numbers separated by space: ").strip().split()
print(two_length_run(li))
