# diccionario de listas prar representar una
#matriz de adyacencia

grafo ={
    #    A,B,C,D 
    "A":[0,1,1,0],
    "B":[1,0,1,2],
    "C":[1,1,0,1],
    "D":[0,2,1,0]
}

camino=["A","B","D","C","A"]



ListaNodosVisitados=[]

Nodos = grafo.values()

for i in range( len(camino)-1 ):
    
    NodoActual =camino[i]

    
     
    
    if(  ( NodoActual in ListaNodosVisitados)      )
            return False

    ListaNodosVisitados.append( NodoActual ) 


    print(   camino[i]   )


"""

    graph = { 1: [ 2, 4, 8 ], 2: [ 7, 3, 1 ], 3: [ 2, 6, 4 ],
              4: [ 1, 3, 5 ], 5: [ 4, 8, 6 ], 6: [ 5, 3, 7 ],
              7: [ 6, 2, 8 ], 8: [ 7, 5, 1 ] }
    certificate = [ 1, 2, 3, 4, 5, 6, 7, 7, 1 ]

 """   