# -*- coding: utf-8 -*-
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
    05-09-2019

Versión:
    1.5
    
Descripción:
    DIseñar y programar un algoritmo para obtener una configuración de parentecis para n matrices
    tal que el número de productos escalares sea mínimo; mediante la técnica de programación
    dinámica.
"""

"""

def ImprimeParentesisOptimos(s,i,j):
    if i==j:
        print("A_"+str(i) ,end="")
    else:
        print("(",end="")
        ImprimeParentesisOptimos(s,i,s[i-1][j-1])
        ImprimeParentesisOptimos(s,s[i-1][j-1]+1,j)
        print(")",end="")
"""
#funcion para imprimir el orden de los parentesis calculados en s[][]
def ImprimeParentesisOptimos(s,i,j):
    if i==j:
        print("A_"+str(i) ,end="")
    else:
        print("(",end="")
        ImprimeParentesisOptimos(s,i,s[i-1][j-1])
        ImprimeParentesisOptimos(s,s[i-1][j-1]+1,j)
        print(")",end="")


#Funcion para declarar una matriz de dimension nxn
def crearMatriz(n):
    A=[]
    for i in range(0,n):
        A.append([""]*n)
        
    #Retornar la matriz A de dimension nxn
    return A

#Funcion para construir la solución óptima con la información en s
def secuenciaDeMatrices (P):

    #Igualar n al numero de matices
    n = len(P)-1
    #Declarar la matriz m de longitud nxn  para almacenar los costos mínimos para cada división optima
    m=crearMatriz(n)
    #Declarar la matriz s de longitud nxn para almacenar las divisiones óptimas, índice de k
    #Para construir la solución óptima 
    s=crearMatriz(n)
    
   
    #Llenar de ceros las diagonales de la matriz m
    for i in range(0,n):
        m[i][i] = 0


    for  l in range(1,n):    
        for i in range(0,n-l):
            j=i+l
            #Igualar m[i][j] al número mas grande aceptado por el tipo de dato
            m[i][j]=99999999
            #asumimos una división óptima entre A_k y A_k+1 (i ≤k<j)
            #m[i,j] = costo de calcular A _i..k + costo de calcular A _k+1..j + costo de calcular A_i..k A _k+1..j
            #Sin embargo, no conocemos el valor de k e intentaremos todas las j-i posibilidades
            
            #Obtener las j-i combinaciones
            for k in range(i,j):
                
                q= m[i][k]+m[k+1][j]+P[i]*P[k+1]*P[j+1]   
                
                #Escoger la combinación cuyo número de productos escalares es más pequeño
                if( q < m[i][j]):
                    m[i][j] =q
                    s[i][j]=k+1

    return m,s

    
#Instancia corespondiente a las dimensiones de 6 matrices.
#P=[30,35,15,5,10,20,25]   
P=[3, 5, 2, 2]


#P=[10,100,5,50,10]
#P=[5,10,100,5,100]
m,s=secuenciaDeMatrices(P) 


def imprMatrices(P):
    con=1
    for i in range( 1,len(P) ):
        print("A"+str(con)+"(",end="")
        print(str(P[i-1])+",",end="")
        
        print(str(P[i])+")",end="")
        con+=1
        if(i!= len(P)-1 ):
            print("x",end="")
      
        
        

#A1 (10,50)xA2 (50,150)x
print("Para la multiplicacion de  matrices")

imprMatrices(P)
print()
print("La configuracion optima es :")




#Imprimir la configuración óptima para 
ImprimeParentesisOptimos(s,1,len(P)-1 )