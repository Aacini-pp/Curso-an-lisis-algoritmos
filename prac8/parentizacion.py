#
#
#
#
#
#


def ImprimeParentesisOptimos(s,i,j):
    if i==j:
        print("A_"+str(i) ,end="")
    else:
        print("(",end="")
        ImprimeParentesisOptimos(s,i,s[i][j])
        ImprimeParentesisOptimos(s,s[i][j]+1,j)
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
    m=crearMatriz(n+1)
    s=crearMatriz(n+1)
    
   
    for i in range(1,n+1):
        m[i][i] = 0
    for  l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1    
            

            m[i][j]=99999
            for k in range(i,j):
                q= m[i][k]+m[k+1][j]+P[i-1]*P[k]*P[j]   
                if( q < m[i][j]):
                    m[i][j] =q
                    s[i][j]=k

    return m,s


P=[30,35,15,5,10,20,25]  
#P=[3, 5, 2, 2]
m,s=secuenciaDeMatrices(P) 
ImprimeParentesisOptimos(s,1,6)

s