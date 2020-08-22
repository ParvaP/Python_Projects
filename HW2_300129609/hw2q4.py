import random

def doTest(operation): 
    ## complete your work here ##
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    if operation == 0:
            print(n1, "+", n2, "=", end = " ")
            ans = int(input())
            if ans == (n1 + n2):
                return True
            else:
                print("The correct answer is",(n1+n2))
                return False
    elif operation == 1:
            print(n1, "x", n2, "=", end = " ")
            ans = int(input())
            if ans == (n1 * n2):
                return True
            else:
                print("The correct answer is",(n1*n2))
                return False
    # return True for now
    
responsesCorrect = 0
print("The software will process a test with 10 questions …… ")
for compteur in range (10):
    operation = random.randint(0,1)
    if doTest(operation) == True:
         responsesCorrect += 1
print(responsesCorrect, "Correct responses")         
if responsesCorrect  <= 6 :
  print("Ask some help from your instructor.")
else:
  print("Congratulations!")
