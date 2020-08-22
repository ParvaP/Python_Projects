def add (li):
    for row in range(len(li)):
        for col in range(len(li[row])):
            li[row][col]=li[row][col]+1
    return li

def add_v2(li):
    li2 = []
    for row in range(len(li)):
        li2.append([])
        for col in range(len(li[row])):
             li2[row].append(li[row][col]+1)
    return li2

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of cols: "))
matrix = []
i=0
while (i < m):
    j= 0
    matrix.append([])
    while j < n:
        v = int(input("matrix["+str(i)+","+str(j) +"]= "))
        matrix[i].append(v)
        j =j+ 1
    i= i+ 1

print("The array is:\n",matrix)
print("After executing the function add, the array is:\n",add(matrix))
print("A new array created with add_V2\n",add_v2(matrix))
print("After executing the function add_V2, the initial array is:\n",matrix)