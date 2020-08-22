owe = float(input ("How much money are you owed (in dollars): "))

owe = int(owe*100)

num_q = owe//25
owe = owe - num_q*25
#print(owe)
num_d = owe//10
owe = owe - num_d*10
#print(owe)
num_n = owe//5
owe = owe - num_n*5
#print(owe)
num_p = owe/1
owe = owe - num_p*1
#print(owe)
num_q = int(num_q)
num_d = int(num_d)
num_n = int(num_n)
num_p = int(num_p)

coin_total = num_q + num_d + num_n + num_p

print ("The minimum number of coins is",str(coin_total))

#print ("The minimum number of coins is",str(coin_total),"(in particular",str(num_q),"quarters",str(num_d),"dimes",str(num_n),"nickles",str(num_p),"pennies).")