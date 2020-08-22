import random
def performTest(operation):
    ## complete your work here ##
    correctCounts = 0
    for i in range(10):
        n1 = random.randint(1, 9)
        n2 = random.randint(1, 9)
        if operation == 0:
            print(n1, "+", n2, "=", end = " ")
            ans = int(input())
            if ans == (n1 + n2):
                correctCounts = correctCounts + 1
            else:
                print("The correct answer is",(n1+n2))
        elif operation == 1:
            print(n1, "x", n2, "=", end = " ")
            ans = int(input())
            if ans == (n1 * n2):
                correctCounts = correctCounts + 1
            else:
                print("The correct answer is",(n1*n2))

    print("You got", correctCounts, "right.")
    return correctCounts


print("This software tests you with 10 questions …… ");
operation = int(input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))

correctCounts = performTest(operation)

if correctCounts <= 6:
    print("Please ask your teacher for help.")
else:
    print("Congratulations!")
