def mi_funcion(cad, v = 2, **algomas):
  print(cad * v)
  
  print(algomas['cadenaextra'])
  print(algomas['cadenademas'])

def mi_funcion2(num1, num2):
  return num1 + num2

def mi_funcion3(cad, v = 2, *algomas):
  print(cad * v)
  
  for cadena in algomas:
    print (cadena * v)
  

resultado = mi_funcion2(3,4)
print(resultado)
mi_funcion('Python ', 5, cadenademas = 'Adios', cadenaextra= 'Hola')
mi_funcion3('Python ', 5, 'Hola ', 'Adios ', 'N ', 'cadenas ' )
