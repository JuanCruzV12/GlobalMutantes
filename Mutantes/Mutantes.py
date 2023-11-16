def isMutant(dna):
    contSecu = 0
    #Identificar secuencias horizontales
    contHor = 0
    for cadena in dna:
        for i in range(1,6):
            if(cadena[i-1] == cadena[i]):
                contHor += 1
                if(contHor >= 3):
                    contSecu += 1
                    print("SI HORIZONTAL")
                    contHor = 0
                    break
            elif(cadena[i-1] != cadena[i]):
                contHor = 0
    #Identificar secuencias verticales
    contVer = 0
    for j in range(0,6):
        for i in range(1,6):
            if((dna[i-1])[j]==(dna[i])[j]):
                contVer += 1
                if(contVer >=3):
                    contSecu += 1
                    print("SI VERTICAL")
                    contVer = 0
                    break
            elif((dna[i-1])[j]!=(dna[i])[j]):
                contVer = 0
    #Identificar secuencias diagonales
    contDiag = 0
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
    #Identificar si es Mutante
    if(contSecu >= 2):
        print("Es mutante")
    elif(contSecu < 2):
        print("No es mutante")


dna = []
for i in range(0,6):
    dna.append(input("Ingrese la secuencia del ADN (6 letras utilizando solo A,T,C,G): "))
for cadena in dna:
    print(f"|"+cadena+ "|")
isMutant(dna)
