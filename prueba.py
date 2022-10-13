import numpy as np



matriz = np.identity(45)
matriz2 = np.identity(45)


matriz = matriz.tolist()
matriz2 = matriz2.tolist()

matrices = []

matrices.append(matriz)
matrices.append(matriz2)





K1 = ["Santiago", "Recoleta", "Estación Central","Ñuñoa", "Macul", "Peñalolén","La Florida", "La Pintana", "El bosque","Providencia","San Bernardo","La Granja","San Miguel", "Cerrillos","Independencia"]
Q_fjk = dict()
familia = 1
comuna = 1
diccionarios = dict()
for matriz in matrices:
    for fila in matriz:
        cont2 = 0    
        # print(fila[cont2])
        # print(fila)
        for k in K1:
            for i in range(1,4):
                #if familia == 46:
                    # print({(str(familia),str(i),k): fila[cont2]})
                    # print(cont2)
                add = {(str(familia),str(i),k): fila[cont2]}
                Q_fjk.update(add)
                cont2 += 1
        familia += 1


    # print(Q_fjk)
    diccionarios.update(Q_fjk)


def obtener_valor(familia, caja, comuna):
    return Q_fjk[(familia,caja,comuna)]