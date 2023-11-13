# GlobalMutantes
### Nombre: Juan Cruz Vargas
### Legajo: 51657

## Descripción
Este es el examen/proyecto global de Programación 1 

## Realización/Funcionamiento
Primero se cargan las secuencias de letras y luego pasan a la función donde se evaluan si hay secuencias de 4 letras iguales. Cada tipo de secuencia (horizontal, vertical, diagonal), se evalua en bucles distintos y al final muestra si es *mutante* o no.

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