def ingresar(M,f,C):
  for i in range(f):
    for j in range(C):
      M[i][j]=int(input("valor?: "))

def mostrar(M,f,C):
    for f in range(f):
        for c in range(C):
            print(M[f][c],end="   ")
        print()
"""def mostrar(M,f,C):
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
    print("elementos diferentes")""" 
    
M=[]
f=int(input("cantidad de filas"))
C=int(input("cantidad de columnas"))
for i in range(f):
  M.append([0]*C)
ingresar(M,C,f)
mostrar(M,C,f)
"""if f==C:
  print("suma de la diagonal secundaria", sumaDS(M,C))
else:
  print("no existe daigonal secundaria")"""
