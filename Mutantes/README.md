# GlobalMutantes
### Nombre: Juan Cruz Vargas
### Legajo: 51657
### Email: juancruzvargas67@gmail.com

## Descripción
Este es el examen/proyecto global de Programación 1. Se trata de un codigo que a partir de una serie de letras dadas (representando una secuencia de ADN) indica si pertenece a un mutante o no.

## Realización/Funcionamiento
* Primero: Se cargan las secuencias de letras. 
* Segundo: Pasan a la función donde se evaluan si hay secuencias de 4 letras iguales. Cada tipo de secuencia (horizontal, vertical, diagonal), se evalua en bucles distintos.
* Por último muestra si es *mutante* o no.

## Observaciones
En el fragmento de codigo:
```python
for i in range(1,6):
    if((dna[i-1])[i-1] == (dna[i])[i]):
        contDiag += 1
        if(contDiag >= 3):
            contSecu += 1
            print("SI DIAGONAL")
            contDiag = 0
            break
    elif((dna[i-1])[i-1 != (dna[i])[i]]):
        contDiag = 0
```
Se evalua si hay una secuencia en la *Diagonal Principal*