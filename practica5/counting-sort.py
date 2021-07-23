# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
    25-09-2019

Versión:
    1.5
    
Descripción:

    Calcular la complejidad del algoritmo de ordenamiento countigsort, mediante el método 
    de línea por línea.
"""

import math 
import numpy as np
from matplotlib import pyplot as plt


def countingSort(A,pos):
    #encontrar el mayor y menor
    y[pos]+=2
    minimo=400000000000000
    maximo=-400000000000000
    for i in range(len(A)):
        y[pos]+=2
        if (A[i] > maximo ):
            y[pos]+=1
            maximo =A[i]
        if (A[i]< minimo):
            y[pos]+=1
            minimo = A[i]
    y[pos]+=1
    aux=np.zeros(maximo+1, dtype = int)
    for i in range( len(A) ):
         y[pos]+=1
         aux[ A[i] ] +=1
    Aordenado=np.array([])
    for i in range( len(aux) ):  
        y[pos]+=1
        if (aux[i] > 0 ):
                y[pos]+=2
                num2Conc = np.linspace(i, i, aux[i], dtype = int )
                Aordenado = np.concatenate((Aordenado, num2Conc), axis=0)
    j=0
    """
    #pasar de auxiliar a el array original
    for i in Aordenado:
       y[pos]+=2 
       A[j]=int(i)
       j+=1
    """   
    return Aordenado

A = [4,2,6,2,2,2,1,7,6,5,4,3,6,9,0,7,3,3,3]  
print(A)
print("Array ordenado ") 


x=range( len(A)-1 )  # valores de n a probar
y=[]
y2=[]  #a qui guardaremso el resultado de la  funcion g(n) 
        #evaluado en los valores en el arreglo x


def c1g(x):   #funcion propuesta
    a=6*x+8
    return a


  



for i in range(1,  len(A) ):
    y.append(0);   
    #print(x[:i])
    print(countingSort(  A[:i],i-1 ))
    y2.append(c1g(x[i-1]))  #agregamos el resultado de la evaluacion en
                            #la funcion propuesta 


print(x)
print(y)

plt.ion()
plt.plot(x,y,'b.',x,y2)   #graficamos

  