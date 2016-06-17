def ingresar(M,f,C):
  for i in range(f):
    for j in range(C):
      M[i][j]=int(input("valor?: "))

def mostrar(M,f,C):
    for f in range(f):
        for c in range(C):
            print(M[f][c],end="   ")
        print()
def intercambiar(M,c,x,y):
    for i in range(c):
      aux=M[x][i]
      M[x][i]=M[y][i]
      M[y][i]=aux
def mostrar(M,f,C):
  for i in range(f):
    for j in range(C):
          if j==0 or j==C-1 or i==j:
              print(M[i][j],end="\t")
          else:
              print(" ",end="\t")
    print()
def contorno(M,f,C):
  for i in range(f):
    for j in range(C):
          if i==0 or i==f-1 or j==0 or j==C-1:
              print(M[i][j],end="\t")
          else:
              print(" ",end="\t")
    print()
  
def sumaDP(M,n):
  s=0
  for i in range(n):
    for j in range(n):
      if i==j:
        s=s+M[i][j]
  return s

def sumaDS(M,n):
  s=0
  j=n-1
  for i in range(n):
      s=s+M[i][j]
      j=j-1
  return s


def sumar(M,f,c):
  s=0
  for i in range(f):
    for j in range(c):
      s=s+M[i][j]
    return s

def sumadefilas(M,f,c):
  for i in range(f):
    s=0
    for j in range(c):
      s=s+M[i][j]
    print("sumafila",i,"es",s)
def diferentes(M,f,C):
  for i in range(f):
    for j in range(C):
      var=M[i][j]
      for k in range(f):
        for l in range(C):
          var==M[k][i] and i!=k and j!=l
          return False
  return True 
  if comparar(M,f,C):
    print("elementos diferentes")
    
M=[]
f=int(input("cantidad de filas"))
C=int(input("cantidad de columnas"))
for i in range(f):
  M.append([0]*C)
intercambiarM,c,x,y)
ingresar(M,C,f)
mostrar(M,C,f)
if f==C:
  print("suma de la diagonal secundaria", sumaDS(M,C))
else:
  print("no existe daigonal secundaria")



  """suma de matrices""" 




def ingresar_elem_matrices(M,F,C):
    for f in range(F):
        for c in range(C):
            M[f][c]=int(input("El elemento (%d,%d) es :" % (f+1,c+1)))
def mostrar(M,F,C):
    for f in range(F):
        for c in range(C):
            print(M[f][c],end="   ")
        print()
def suma_matrices(M1,M2,M3,F,C):
    for f in range(F):
        for c in range(C):
            M3[f][c]=M1[f][c]+M2[f][c]
                            
filas=int(input("la cantidad  de filas es: "))
columnas=int(input("la cantidad de columnas es: "))
sep="*"*80
print(sep)
M1=[]
for e in range(filas):
    M1.append([0]*columnas)
    
M2=[]
for e in range(filas):
    M2.append([0]*columnas)
    
M3=[]
for e in range(filas):
    M3.append([0]*columnas)

print("ingresaremos los elementos de la 1ra matriz ")   
ingresar_elem_matrices(M1,filas,columnas)
sep="*"*80
print(sep)
print("ingresaremos los elementos de la 2da matriz ")
ingresar_elem_matrices(M2,filas,columnas)
sep="*"*80
print(sep)

print("tu matriz 1 es: ")
mostrar(M1,filas,columnas)
sep="*"*80
print(sep)

print("tu matriz 2 es: ")
mostrar(M2,filas,columnas)
sep="*"*80
print(sep)
suma_matrices(M1,M2,M3,filas,columnas)
print("la suma de las matrices 1 y 2 es : ")
mostrar(M3,filas,columnas)  




