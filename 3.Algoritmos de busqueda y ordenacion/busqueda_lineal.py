import random

def busqueda_lineal(lista,objetivo):
    contador = 0
    match = False 
    for elemento in lista: # 0(n)
        if elemento == objetivo:
            match = True
            print(f'contador {contador}')
            break
        contador+=1
    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('de que tamano sera la lista :'))    
    objetivo = int(input('¿Que numero quieres encontrare? '))

    lista = [random.randint(1,100) for i in range(tamano_de_lista)]
    
    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    # esto es una expresion ternaria
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
