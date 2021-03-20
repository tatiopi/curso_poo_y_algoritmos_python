# asumimos que esta ordenada la lista
import random

def busqueda_binaria(lista,comienzo,final,objetivo , contador):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    if comienzo>final:
        return False
    
    medio = (comienzo + final) // 2 

    if lista[medio] == objetivo:
        print(f'numero de iteraciones {contador}')
        return True
    elif lista[medio] < objetivo:
        contador= contador +1 
        return busqueda_binaria(lista , medio+1 ,final ,objetivo,contador )
    else:
        contador = contador +1 
        return busqueda_binaria(lista ,comienzo , medio-1 ,objetivo , contador)

if __name__ == '__main__':
    contador = 0 
    tamano_de_lista = int(input('Tamano de la lista : '))
    objetivo = int(input('Que numero quieres encontrar?'))

    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista,0 , len(lista) , objetivo , contador )
    
    encontrado = False

    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
