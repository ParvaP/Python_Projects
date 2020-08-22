def vote_percentage(s):
    y = 0
    n = 0
    for i in s:
        if i == "yes":
            y = y + 1
        elif i == "no":
            n = n + 1
    return y/(y+n)


s = input("Input the votes (yes, no, or abstention) seperated by spaces, then push enter: ").strip().split()
percentage = vote_percentage(s)
if percentage == 1:
    print("unanimous")
elif percentage >= 2/3:
    print("clear majority")
elif percentage >= 1/2:
    print("simple majority")
else:
    print("motion failed")
