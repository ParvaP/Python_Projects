def double (s):
    ss = []
    for i in reversed(range(0,len(s))):
        ss.append(s[i])
        ss.append(s[i])
    return ''.join(ss)


s = input("Please enter a chain of characters: ")
print(double(s))