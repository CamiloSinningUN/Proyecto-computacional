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


switch = int(input("Digite el numero correspondiente al metodo que desea usar:\n + sin_repetidos (1) \n + sin_ceros (2)\n >"))
if switch == 1:
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    print("El resultado es: ",sin_repetidos(a,b))
elif switch == 2:
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    print("El resultado es: ",sin_ceros(a,b))
