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
    18-11-2019

Versión:
    1.2
    
Descripción:
    Implementar el algoritmo de la codificacio ́n de Huffman con las siguientes condiciones:
Para la Codificaci ́on.
Entrada: Un archivo de texto con extensio ́n .txt (original.txt) a codificar.
Salida: se generaran tres archivos .txt.
Frecuencias.txt: Mostrara ́ la tabla de frecuencias de los caracteres que
aparecen en el archivo original.txt.
Codificacion.txt: Mostrara ́ los caracteres que aparecen en el archivo
original.txt y la codificacio ́n que le corresponde. Archivo codificado.txt: Mostrar ́a el archivo codificado. Archivo comprimido.txt: Mostrara ́ el archivo comprimido.

"""

import binascii 
#clase  para los nodos del arbol binario de hyffman
class Nodo:
    def __init__ (self,letra= None,peso= None,izq= None,der= None,):
        self.letra=letra
        self.peso=peso
        self.izq=izq
        self.der=der
    def __str__(self):
        return "%s %s (%s , %s) " %(self.letra, self.peso, self.izq,self.der)




#devolvera  un dicionario  donde 
#la clave sera el caracter y el valor sera  un array 
# y  el primer valor sera 
#la frecuencia de de dicho caracter
def  crearTablaHash(txt): 
    hash={}
    for i in txt:
        if (  not (i in hash )   ) :
            hash[i] = [1]
        else:
             hash[i][0] += 1

    return hash

#recorre el arbol para agregar los codigos de cada caracter a 
# a la tablaCaracteres
def  obtenerCodigos(nodo,cadena,tablaCaracteres):
    if(nodo.izq==None and  nodo.der==None ):
        tablaCaracteres[nodo.letra].append(cadena)
        return cadena
    else:
        obtenerCodigos(nodo.izq,cadena+"0",tablaCaracteres) 
        obtenerCodigos(nodo.der,cadena+"1",tablaCaracteres) 





#retorna la posicion de los  nodos con menor frecuencia
def encontrarMenores(lista):
    min1=99999999 #numeros muy grandes para comparar
    min2=99999999
    pos1=-1 #posicion inicial del menor
    pos2=-1
    for i in  range( len(lista) ):  #recorrer la lista 
        if(lista[i].peso < min1 ): #si el numero actual es menor al actual
            min2=min1  #el numero anterior pasarlo la  min2 con su posicion
            pos2=pos1

            min1 = lista[i].peso
            pos1 = i
        elif ( lista[i].peso < min2 ): # si no comprobar si es menor almin2
            min2 = lista[i].peso #cambiar el nuevo valor y su posicion
            pos2 = i
        
    return pos1, pos2



#implementa el algoritmo huffman#para asignarlle un codigo a cada letra 
#devuelve la raiz del arbol
def Huffman(Listanodos):
    while( len(listaNodos)>1  ):
        #encontrar los 2 valores menores
        min1, min2 = encontrarMenores(listaNodos)
        #calcular el tamanio del nuevo nodo
        nuevoTam = listaNodos[min1].peso +listaNodos[min2].peso
        #crear el nodo 
        nodoAux = Nodo( "",nuevoTam )
        #asignarle  los dos  mas pequeños  
        nodoAux.izq = listaNodos[min1] #el mas pequenio izquierda
        nodoAux.der = listaNodos[min2] #el siguiente mas pequenio derecha


        #si el min1 se quita  de la lista antes que 
        # min2 recorrer en 1 min2  para recorrerla
        if(min1 < min2):
            min2-=1

        #quitar los nodos de la lilsta
        listaNodos.pop(min1)
        listaNodos.pop(min2 ) 
        #agregar el nuevo nodo a la lista
        listaNodos.append(nodoAux)

    return listaNodos[0]

#Pasar el contenido de un archivo a un string
def FiletoString(NombreArchivo):
    #Abrir el archivo para lectura
    f = open (NombreArchivo,'r')
    #Pasar el contenido del archivo al string
    mensaje = f.read()
    #Eliminar los espacion en blanco
    #mensaje=mensaje.replace(" ","")
    #Cerrar el archivo
    f.close() 
    
    return mensaje
#guardar codificado codificado
def guardarArchivoCod(nombArch,strPrueba,tablaCaracteres):
    #guardar en archivo
    f = open(nombArch, "w")
    strBin =""
    for i in range( len(strPrueba) ):
        binImp= tablaCaracteres[ strPrueba[i] ][1]
        strBin+=binImp
        f.write(binImp) 
    f.close() 
    return strBin

#guardarTabla
def guardarTabla(nombArch,tablaCaracteres):
    #guardar en archivo
    f = open(nombArch, "w")
    for i in tablaCaracteres :
        binImp= tablaCaracteres[ i ][1]
        f.write(i) 
        f.write(binImp) 
        f.write("\n") 
    f.close() 


#archivo para  pasar testo binario a binario comprimido 
    
def guardarArchivoBin(nombArch,stringBin):
    noOctetos= len(stringBin)//8  #calcual el numero de octetos
    bitsRestantes =  len(stringBin) % 8  #calcula el numero de bits que sobraro
    bitsAdicionales=0 
    
    #agregamos los bits faltantas para acoplentar el ultimo aocteto
    if(bitsRestantes > 0):
        bitsAdicionales = 8-bitsRestantes
        for i in range(bitsAdicionales):  #y agregamos el  numero de 0 para acompletar el octeto
            stringBin+="0"    
   
    #guardar en archivo
    f = open(nombArch, "w")     
    for i in range(noOctetos): #repertir cuantos octetos haya
        bin = stringBin[ (i*8):(i*8)+8 ]  #de de la posicion n-sima hasta n+8 tomamos para convertirlo a caracter
        f.write( str( chr(  int(bin, 2) ) ))  #este numero lo pasamos a enter luego a  caracter y lo guardamos
    f.write(str( bitsAdicionales) )   #añadimos el numero de bits que agregamos
    f.close()
 

#abrimos el archivo orginal y lo guardamos en un string    
Archivo="original.txt"
strPrueba =FiletoString(Archivo)
#calculamos la frecuencia de cada caracter 
tablaCaracteres =crearTablaHash( strPrueba)


#aqui guardaremos los nodos 
listaNodos=[]
#pasamos los caracteres a nodos y los almacenamos en una lista
for  i  in  tablaCaracteres:
    aux = Nodo( i,tablaCaracteres[i][0]   )
    listaNodos.append(aux)
raiz = Huffman(listaNodos) #calculamos el arbol de hufman
obtenerCodigos(raiz,"",tablaCaracteres) #sacamos el codigo para cada caracter y lo cuardamos en la tabla de caracteres
print(tablaCaracteres)
#guardamos el codificado y mantenemos una copia para el comprimido
stringBin= guardarArchivoCod("Archivo codificado.txt",strPrueba,tablaCaracteres)
#guardamos la codificacion
guardarTabla("Codificacion.txt" , tablaCaracteres)   
#le pasamos el string de binario que mismo  y lo guardamos su representacion en caracter
guardarArchivoBin("Archivo comprimido.txt",stringBin)


"""


diccionario={}

print("------------")

for i in   tablaCaracteres:
    diccionario[  tablaCaracteres[i][1]   ]= i
    
print(diccionario)
"""



#print( tablaCaracteres["P"][1] )





