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

    Calcular la complejidad del algoritmo de ordenamiento radixsort, mediante el método 
    de línea por línea.
"""


import math 
import numpy as np
from matplotlib import pyplot as plt


def radixsort( A ,pos):
    #encontrar el mayor numero
    y[pos]+=1
    maximo=-400000000000000
    for i in range(len(A)):
        y[pos]+=1
        if (A[i] > maximo ):
            y[pos]+=1
            maximo =A[i]
    y[pos]+=3        
    # el numero de iteraciones sera el numero de digitos que tenga ese numero
    numeroMaxDigitos= len(str(maximo))
    #crear los bunquers  donde se  alamcenaran los numeros 
    buncker={} # que sera un diccionario
    for i in range(10):
        y[pos]+=1
        buncker[i]=[] #cada diccionario  tendra una lista donde se guardaran los numeros
       
    y[pos]+=1
    digTurno=0  #empesamos con el digito 0 
    
    
    while(numeroMaxDigitos > digTurno):  #repetir hasta que el digito enturno sea igual al numeroMaximo 
        y[pos]+=1
        for i in range(len(A)):  #para cada elemento en A
            y[pos]+=1
            if((len(str(int(A[i]) ))-1)< digTurno ):  #si el tamanio del numero es menor al indice 
                y[pos]+=1
                noBunker=0  #agregar al bunquer 0
            else:   # de lo contrario sera el digito en la posicion acual
                 y[pos]+=3
                 numStr=   str(int(A[i]) )   
                 noBunker= int(   ( numStr)[ len(str( int(A[i]) ))-1-  digTurno])
            y[pos]+=1     
            buncker[ noBunker ].append(int(A[i]))
        #pasar todos los numeros del bunquer a A 
        y[pos]+=1
        A=[]   #limpiar a A   
        for i in buncker:  #recorrer los bunckers
            y[pos]+=2
            A = np.concatenate((A, buncker[i]), axis=0)   #concatenar  lo que tiene a con el bunquer actual
            buncker[i]=[]  #limpiar el bunker actual
        y[pos]+=2    
        A=list(A) #convertir a lista
        digTurno+=1 #aumentar el contador 
    #pasar los digitos a enteros  por que  concatenate los pone en decimales  
    y[pos]+=1  
    for i in range(len(A)):
        y[pos]+=1
        A[i]=int(A[i]) 
    return A
    
A = [9999,234,14,22,0,99913,3,1,200000000,5000000000000,2,3,111]  

#print(radixsort(A))


print(A)
print("Array ordenado ") 


x=range( len(A)-1 )  # valores de n a probar
y=[]
y2=[]  #a qui guardaremso el resultado de la  funcion g(n) 
        #evaluado en los valores en el arreglo x


def c1g(x):   #funcion propuesta
    a=10*x*x+100
    return a


  



for i in range(1,  len(A) ):
    y.append(0);   
    #print(x[:i])
    print(radixsort(  A[:i],i-1 ))
    y2.append(c1g(x[i-1]))  #agregamos el resultado de la evaluacion en
                            #la funcion propuesta 


print(x)
print(y)

plt.ion()
plt.plot(x,y,'b.',x,y2)   #graficamos





