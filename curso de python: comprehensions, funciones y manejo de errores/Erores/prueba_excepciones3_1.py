import math

def calculaRaiz(num1):
  if num1 < 0:
    raise ValueError("El número no puede ser negativo")
  else:
    return math.sqrt(num1)

while True:  
  try:
    op1 = int(input("Introduce un número: "))
    break
    
  except ValueError:
    print("Error: ingrese de nuevo el número") 

try:
  print(calculaRaiz(op1))
  
except ValueError as ErrorDeNumeroNegativo:
  print(ErrorDeNumeroNegativo)

print("Programa terminado")