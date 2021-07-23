def mmult(A,B,productosEscl):
    AB = [[0 for k in range(len(B[0]))] for j in range(len(A))]
    for i,row in enumerate(A):
        for j,col in enumerate([list(c) for c in zip(*B)]):
            elem =[a*b   for a,b in zip(row,col)]
            AB[i][j] = sum(elem)
            productosEscl+=1*len(elem)
    return AB,productosEscl
 
productosEscl=0
A = [[1,2],[3,4]]
B = [[1,2,4],[3,4,6]]
R,productosEscl = mmult(A,B,productosEscl)

print(productosEscl)




