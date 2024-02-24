def recogerDatos():

    terminar = False
    temporal = 0
    numeros = []

    while not terminar:
        temporal = input('Digite un numero ó digite T para terminar \n')
        try:
            temporal = int(temporal)
        except:
            if temporal == "t" or temporal == "T":
                print("Terminando la recolección de datos")
            else:  
                print("Solo se aceptan valores decimales, por favor intentelo de nuevo")

        if type(temporal) == int:
            numeros.append(temporal)
            temporal = 0
        
        elif temporal == "t" or temporal == "T":
            terminar = True
    
    return numeros

    
        
        

