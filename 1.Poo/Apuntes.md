# El equivalente de ` de JS en PYTHON

```python
return f'Hola {otra_persona.nombre , me llamo {self.nombre}'
```

# Instancias

Puede tener atributos privados.Por convencion empiezan con _
Saber si instancia es de un objeto print(isinstance(coor_2,Coordenada))

Para indicarle que no tiene ningun valor
self._motor  =  None

So empieza por _ es para indicarle que es privado

# Abstraccion
- Enfocarnos en la informacion relevante

# Decoradores 
Los decoradores son una forma sencilla de llamar funciones de orden mayor, es decir, funciones que toman otra función cómo parámetro y/o retornan otra función como resultado. De esta forma un decorador añade capacidades a una función sin modificarla.

las funciones son objetos de primera-clase, es decir, que pueden ser pasados y utilizados cómo argumentos al igual que cualquier otro objeto (strings, enteros, flotantes, listas, etc.).

* Getters

```python
    @property
    def region(self):
        return self.__region
    @region.setter
    def region(self , region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.pais}')    
```

# Lanzar excepcion
```python
raise ValueError(f'La region {region} no es valida en {self.pais}')
```

# Herencias
```python
# Para heredar de una clase definimos la clase 
# class NombreClase (ClaseDeLaQueDeriva)
class Cuadrado (Rectangulo):
    def __init__(self , lado):
        # llamando al contructor de la clase base
        super().__init__(lado,lado)

rectangulo = Rectangulo(base=3 , altura=4)
print(rectangulo.area())

cuadrado = Cuadrado(lado=2)
print(cuadrado.area())
# instanciando y llamando a los metodos
```
