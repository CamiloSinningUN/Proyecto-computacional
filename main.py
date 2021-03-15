
def sin_repetidos(a, b):
    #Inicializar variables
    lista = []
    cont = 0

    #Se generan lo numeros desde A a B
    for i in range(a,b+1):

        cont1 = 1 #Posición en la que vamos del numero (numero de digito de izquierda a derecha)
        sw = True
        i = str(i) # Se convierte el numero a string

        #Se recorre el numero dígito a dígito
        for j in i:
            if(j in i[cont1:]): #Si el dígito esta contenido en una posición luego de su posición en el numero (No sé si se entiende, escribe en el chat si es claro)
                sw = False
                continue # es como el break de java
            cont1+=1

        # Si un dígito no se encontro repetido en el numero entonces se incluye en la lista y se suma el contador   
        if sw:
            lista.append(i)
            cont+=1

    # Se devuelve la tupla       
    tupla = (cont,lista)
    return tupla

def sin_ceros(a, b):
    lista = []
    cont = 0
    for i in range(a,b+1):   
        sw = True
        i = str(i)
        for j in i:
            if("0" in i):
                sw = False
                continue
        if sw:
            lista.append(i)
            cont+=1
    tupla = (cont,lista)
    return tupla

def ascendentes(a,b):
    lista = []
    cont = 0
    for i in range(a,b+1):  
        cont1 = 1  
        i = str(i)
        sw = True
        for j in i:
            if cont1 < len(i):
                if int(j) >= int(i[cont1]) :
                    sw = False
                    continue
            cont1+=1
        if sw:
            lista.append(int(i))
            cont+=1
    tupla = (cont,lista)
    return tupla

def conjuntos_sin_consecutivos(a, b, k):
    pass

switch = int(input("Digite el numero correspondiente al metodo que desea usar:\n + sin_repetidos (1) \n + sin_ceros (2) \n + ascendentes (3) \n + conjuntos_sin_consecutivos (4) \n >"))
if 1 <= switch <= 4:
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    if switch == 1:     
        print("El resultado es: ",sin_repetidos(a,b))
    elif switch == 2:
        print("El resultado es: ",sin_ceros(a,b))
    elif switch == 3:
        print("El resultado es: ",ascendentes(a,b))
    elif switch == 4:
        k = int(input("Ingrese k: "))
        print("El resultado es: ",conjuntos_sin_consecutivos(a, b, k))
