
"""
Alumnos:
    Victor Hugo Magaña Bautista
    Alberto Aacini Osornio Zambrano.
Grupo
    3CV2
Materia:
    Análisis de Algoritmos
Maestro:
    Luna Benoso Benjamin
Última modificación: 
    17-10-2019

Versión:
    1.5
    
Descripción:

    Calcular la complejidad del algoritmo de ordenamiento stressen
    de manera experimental
"""

import math 
import numpy as np
from matplotlib import pyplot as plt



#funcion que devuelve una matriz cuadrada (nxn)
def NewMatrizCuadrada(n):
    A=[]
    for i in range(0,n):
        A.append([0]*n)
        y[posGlobal]+=2

    return A


def randomMCuadrada (n):
    c=[]
    aux = []
    cont =0
    
    
    for j in range(n):
        aux = []
        for i in range(n):
            aux.append(cont)
            cont+=1
        c.append(aux[:])
    return c


#funcion para multiplicar una matriz cuadrada 
def MultiplicarMatriz(A,B):
    y[posGlobal]+=2
    n=len(A)
    C=NewMatrizCuadrada(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
                y[posGlobal]+=1             
    return C



#suma de matrices
def suma(A,B):
    y[posGlobal]+=2
    n=len(A)
    C=NewMatrizCuadrada(n)
    for i in range(n):
        for j in range(n):
            y[posGlobal]+=1
            C[i][j] = A[i][j]+B[i][j]
    return C        


#resta de matrices 
def resta(A,B):
    n=len(A)
    C=NewMatrizCuadrada(n)
    y[posGlobal]+=2
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j]-B[i][j]
            y[posGlobal]+=1
    return C  

#dividir una matris en 4 cuadrantes iguales
def cuadrantesMatriz(a):
    y[posGlobal]+=2
    n = len(a)
    m = n // 2#punto medio

    c1 = [[a[i][j] for j in range(m, n)] for i in range(m)]
    c2 = [[a[i][j] for j in range(m)] for i in range(m)]
    c3 = [[a[i][j] for j in range(m)] for i in range(m, n)]  
    c4 = [[a[i][j] for j in range(m, n)] for i in range(m, n)]

    #aumentar la complejidad cuadrada  por los fors 
    for j in range(m, n): 
        for i in range(m):
            y[posGlobal]+=2
    for j in range(m):
     for i in range(m, n):
        y[posGlobal]+=2

    return c2, c1, c3, c4




def strassen(A, B):
    y[posGlobal]+=1
    if len(A) == 2:  # la condicion de frontera es la matriz cuadrada
        y[posGlobal]=+1
        return MultiplicarMatriz(A, B)  #multiplicar de forma convencional
    y[posGlobal]=+2
    a, b, c, d = cuadrantesMatriz(A)  #a las submatrices resultantes acciganles una letra a cada una
    e, f, g, h = cuadrantesMatriz(B)

    y[posGlobal]+=7
    
    #aplicar las formulas de strencen 
    p1 = strassen(a, resta(f, h))
    p2 = strassen(suma(a, b), h)
    p3 = strassen(suma(c, d), e)
    p4 = strassen(d, resta(g, e))
    p5 = strassen(suma(a, d), suma(e, h))
    p6 = strassen(resta(b, d), suma(g, h))
    p7 = strassen(resta(a, c), suma(e, f))

    y[posGlobal]+=4
    #sacar los cuadrantes  de la matriz resultante
    c1 = suma(p1, p2)
    c2 = suma(resta(suma(p5, p4), p2), p6)
    c3 = suma(p3, p4)
    c4 = resta(resta(suma(p1, p5), p3), p7)

    # construir la matriz apartir d elos cuatro  cuadrantes
    C = []
    for i in range(len(c1)):
        y[posGlobal]==1
        C.append(c2[i] + c1[i])
    for i in range(len(c4)):
        y[posGlobal]+=1
        C.append(c3[i] + c4[i])
    return C



A = [
            [10, 9, 4, 3],
            [8, 3, 4, 1],
            [93, 1, 9, 3],
            [2, 2, 7, 6]
        ]

B = [
            [4, 5, 3, 5],
            [4, 1, 2, 1],
            [9, 8, 3, 5],
            [6, 3, 7, 9]
        ]



#print(strassen(A,A))
A=randomMCuadrada( int( math.pow(2,10)) )
print(A)

      


def subM(
    matrix, 
    rowStartIdx, rowEndIdx,
    colStartIdx, colEndIdx):

    result = [
        x[ colStartIdx : colEndIdx ]
        for x in matrix[ rowStartIdx : rowEndIdx ]
    ]

    return result




x=[]  # valores de n a probar
y=[]
y2=[]  #a qui guardaremso el resultado de la  funcion g(n) 
        #evaluado en los valores en el arreglo x
posGlobal =0  

def c1g(x):   #funcion propuesta
    a=math.pow(x,3)
    return a



  
for i in range(1,10):
    posGlobal = i-1

    n=int(math.pow(2,i))
    
    x.append(n)
    y.append(0); 
    
    subA = subM(A,
                    0, n, 
                    0, n)
    print (len(subA))
    print(subA)
    print('resultado multiplicacion')
    #print(subB)
    print(strassen(subA,subA) )
    
    y2.append( c1g(n ))


print(x)
print(y)



plt.ion()
plt.plot(x,y,'b.',x,y2)   #graficamos





#print(suma(A,B))
#print(resta(A,B))



#[[130, 100, 81, 106],
# [86, 78, 49, 72],
# [475, 547, 329, 538],
# [115, 86, 73, 101]]