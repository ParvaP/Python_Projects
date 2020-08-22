def longest_run(li):
    max = 0
    count = 1
    for i in range(0,len(li)):
        li[i] = float(li[i])
    for i in range(0,len(li)-1):
        if li[i] == li[i+1]:
            count = count + 1
        if count > max:
            max = count
        if li[i] != li[i+1]:
            count = 1
    return max

li = input("Please input a list of numbers seperated by space: ").strip().split()
print(longest_run(li))
