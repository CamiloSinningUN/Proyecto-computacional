from sort import ordenar

def sin_repetidos(a, b):
    lista = []
    cont = 0
    for i in range(a,b+1):
        cont1 = 1
        sw = True
        i = str(i)
        for j in i:
            if(j in i[cont1:]):
                sw = False
                continue
            cont1+=1
        if sw:
            lista.append(i)
            cont+=1
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

def ascendentes(a, b):
    lista = []
    cont = 0
    for i in range(a,b+1):     
        if ordenar(i):
            tupla = sin_repetidos(i,i)
            if tupla[0] > 0:
                cont+=1
                lista.append(i)
    
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
