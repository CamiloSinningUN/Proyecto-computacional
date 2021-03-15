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

switch = int(input("Digite el numero correspondiente al metodo que desea usar:\n + sin_repetidos (1) \n >"))
if switch == 1:
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    print("El resultado es: ",sin_repetidos(a,b))