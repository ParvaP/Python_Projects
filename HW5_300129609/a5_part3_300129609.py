def stars (n):
    print('*'*n)
    if n > 1:
        stars(n-1)
    print('*'*n)
    
n = int(input('Enter the number of stars you want: '))
stars(n)

def sumList_Pos_rec (li,x,total = 0):
    if x > 1:
        if li[0] > 0:
            total = total + li[0]
        del(li[0])
        return sumList_Pos_rec(li,len(li),total)
    else:
        return total

print ('\n\nPart B\n\n')
li = [1,-2,5,0,-5]
print(sumList_Pos_rec(li,len(li)))


