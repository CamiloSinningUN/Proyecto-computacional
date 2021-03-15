#Comprobar si estan de menor a mayor
def ordenar(i):
    lista = []
    for j in str(i):
        lista.append(j)
    lista.sort(reverse=False) 

    numero = 0
    u = len(lista)-1  
    for j in lista:
        numero = numero + int(j)*10**u 
        u = u-1 
    
    if numero == i:
        sw = True
    else:
        sw = False

    return sw