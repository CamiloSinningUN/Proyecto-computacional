
def sin_repetidos(a, b):
    lista = []
    cont = 0

    # Se recorren numeros entre a y b
    for i in range(a, b+1):
        cont1 = 1  # Contador dígito
        sw = True
        i = str(i)

        # Se recorre el numero dígito a dígito
        for j in i:
            # Verifica si el dígito j esta contenido en i (Sin tener en cuenta j)
            if(j in i[cont1:]):
                sw = False
                continue
            cont1 += 1

        # Si sw es verdadero significa que el numero no tiene dígitos repetidos
        if sw:
            lista.append(i)
            cont += 1

    # Se devuelve la tupla requerida
    tupla = (cont, lista)
    return tupla


def sin_ceros(a, b):
    lista = []
    cont = 0

    # Se recorren numeros entre a y b
    for i in range(a, b+1):
        sw = True
        i = str(i)
        # Verifica si numero contiene el numero cero
        if("0" in i):
            sw = False
            continue

        # Si sw es verdadero significa que el numero no contiene al cero
        if sw == True:
            lista.append(i)
            cont += 1

    tupla = (cont, lista)
    return tupla


def ascendentes(a, b):
    lista = []
    cont = 0

    # Se recorren numeros entre a y b
    for i in range(a, b+1):
        cont1 = 1
        i = str(i)
        sw = True

        # Se recorre el numero dígito a dígito
        for j in i:

            # Se valida que cont1 esta en el rango de i
            if cont1 < len(i) and int(j) >= int(i[cont1]):
                # Si el dígito j es mayor que j+1 entonces no se cumple la condición
                sw = False
                continue
            cont1 += 1

        # Si sw es verdadero significa que el numero es ascendente
        if sw:
            lista.append(int(i))
            cont += 1
    tupla = (cont, lista)
    return tupla


def conjuntos_sin_consecutivos(a, b, k):
    arr = list(range(a, b+1))
    lista = []
    #Vector temporal que va guardando cada combinación una por una
    data = [0]*k; 

    # Halla todas las combinaciones
    combinacion(arr, data, 0, len(arr)-1, 0, k, lista)
    tupla = (len(lista),lista)
    return tupla
     
def combinacion(arr, data, start, end, index, k, lista):   
    if (index == k): 
      if no_tiene_consecutivos(data):
        lista.append(data[:])
      return

    # Remplaza el indice con todos los posibles elementos.
    i = start
    while(i <= end and end - i + 1 >= k - index): 
        data[index] = arr[i]
        combinacion(arr, data, i + 1, end, index + 1, k, lista)
        i += 1

def no_tiene_consecutivos(ar):
  for i in ar:
    for j in ar:
      if i==j-1 or i==j+1:
        return False
  return True

switch = int(input("Digite el numero correspondiente al metodo que desea usar:\n + sin_repetidos (1) \n + sin_ceros (2) \n + ascendentes (3) \n + conjuntos_sin_consecutivos (4) \n >"))
if 1 <= switch <= 4:
    a = int(input(" Ingrese a: "))
    b = int(input(" Ingrese b: "))
    r = "El resultado es: "
    if switch == 1:
        print(r, sin_repetidos(a, b))
    elif switch == 2:
        print(r, sin_ceros(a, b))
    elif switch == 3:
        print(r, ascendentes(a, b))
    elif switch == 4:
        k = int(input(" Ingrese k: "))    
        print(r, conjuntos_sin_consecutivos(a, b, k))
