import random
juego = []

numTablero = int(input("ingrese el tamaño del tablero:  "))
cantidadManzanas = 1
cantidadOstaculos = 3

for f in range(numTablero):
 juego.append([''] * numTablero ) #espacios en blanco
             
if numTablero <= 4:
 print("El minino de juego debe de ser 4 filas y 4 columnas")


        #repeticion aleatoria
x = 0
while  x < cantidadOstaculos:
  fila = random.randint(0, numTablero - 1)
  columna = random.randint(0, numTablero - 1)
  juego[fila][columna] = 'X' 
  x = x + 1


b = 0
while  b < cantidadManzanas:
  fila = random.randint(0, numTablero - 1)
  columna = random.randint(0, numTablero - 1)
  juego[fila][columna] = 'O' 
  b = b + 1

  

   # imprimir juego
print("  +++" + numTablero * " +++" )
for fila in juego:
 print(" | " + " ".join(f"{x:3} " for x in fila) + ' |')

print ("  +++ " + numTablero * " +++" )


