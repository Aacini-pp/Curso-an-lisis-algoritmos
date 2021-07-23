
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


#lee la tabla  de codificacion apartir de un archivo y crea un array asosiativo
#donde la clave es el codigo  y el valor la letra que le corresponde

def construirDiccionario(txtDiccionario,diccionario):
    #si encuentra doble salto de linea remplazar por un salto de linea y un comidin
    txtDiccionario= txtDiccionario.replace('\n\n','\n$replace enter$')
    arryDicc = txtDiccionario.split('\n') #dividir conforme a saltos de linea en un un array
    
    for  i in range(len(arryDicc)-1):  #para    cada item del array
        linea = arryDicc[i]  
        if( linea.find("$replace enter$")!=-1 ): #si contiene el caracter comodin
            linea = linea.replace('$replace enter$','\n')    #reemplazarlo
        carac= linea[0:1] #el caracter sera el primer  item de la linea
        cod = linea[1:] #el resto sera la codificacion
        diccionario[cod]=carac #agregar al diccionario


#Abrimos el texto de la tabla de la codificacion
txtDiccionario =FiletoString('Codificacion.txt')
diccionario = {}
construirDiccionario(txtDiccionario,diccionario) #creamos el diccionario

#abrimos el comprimido
Archivo="Archivo comprimido.txt"
textoCom =FiletoString(Archivo)



#leer y quitar el ultimo carater
noBitsSob = textoCom[( len(textoCom)-1 ):( len(textoCom) )]  #numero de bits que sobran , se anadieron para completar el octeto
textoComp = textoCom[:( len(textoCom)-1 )] 
#print(textoComp )
#print(len( textoCom)*8)
textoBin=""  #creamos un string donde se guardara el texto binario
#paara cara caracter del textoComprimido
for carc in textoComp:
    #print (  str(bin( ord("=") ))  )
    #print (  str(bin( ord("=") ))[2:]  )
    caracBin = str(bin( ord( carc) ))[2:]  #pasarlo el caracter a decimal y luego a binario, quitandole los primeros dos caracteres
    #print(caracBin)
    
    while( len(caracBin)< 8 ): #si el numero es menor a 8 
         caracBin="0"+caracBin #juntarle  `0` a la derecha que se perdieron en el cast
    #print(caracBin)         
    textoBin+=caracBin #el caracter resultante sumarlo a textoBinario




lentexto=len(textoBin) #tamanio del textoBInario
textodecodificado="" #loq ue llevamos decodificado
lim_inf=0 #la posicion inferior
lim_sup=1 #la posicion superir

#mientras el  el limite superior no lelge al ultimo caracter de textoBinario
while lentexto > lim_sup-1:
    aux=textoBin[lim_inf:lim_sup] #el texto a probar ser  el marcado por los indices superior e inferior
    if aux in diccionario:   #si el codigo esta  en el dicionario
        textodecodificado+=diccionario[aux] #pasamos el caracter a texto decodificado  
        lim_inf=lim_sup # ponemos el indice  inferior en la posicion de la superior
    lim_sup+=1 #pasamos el superior  arriba del ultimo probado


print(textodecodificado)
