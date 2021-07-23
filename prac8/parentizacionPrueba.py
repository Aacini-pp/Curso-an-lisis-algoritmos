



def ImprimeParentesisOptimos(s,i,j):
    if i==j:
        print("A_"+str(i) ,end="")
    else:
        print("(",end="")
        ImprimeParentesisOptimos(s,i,s[i-1][j-1])
        ImprimeParentesisOptimos(s,s[i-1][j-1]+1,j)
        print(")",end="")


def crearMatriz(n):
    A=[]
    for i in range(0,n):
        A.append([""]*n)
    return A


#m=[]

#n =[]

def secuenciaDeMatrices (P):

    n = len(P)-1
    m=crearMatriz(n)
    s=crearMatriz(n)
    
   

    for i in range(0,n):
        m[i][i] = 0
    for  l in range(1,n):    
        for i in range(0,n-l):
            j=i+l#j=i+l-1    

            
            m[i][j]=99999
            for k in range(i,j):
                q= m[i][k]+m[k+1][j]+P[i]*P[k+1]*P[j+1]   
                if( q < m[i][j]):
                    m[i][j] =q
                    s[i][j]=k+1

    return m,s

   
    return m,s

#P=[30,35,15,5,10,20,25]   
#P=[10,100,5,50,10]
P=[5,10,100,5,100]

#10,100,5,50,10 /.  5,10,100,5,100

#P=[3, 5, 2, 2]

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


m,s=secuenciaDeMatrices(P) 
ImprimeParentesisOptimos(s,1,len(P)-1 )