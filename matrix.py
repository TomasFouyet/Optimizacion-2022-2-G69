
def construir_matrix():
    matrix = []
    with open ("./BDD/DisponibilidadFamilias.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            matrix.append(linea)
    return(matrix)

construir_matrix()


