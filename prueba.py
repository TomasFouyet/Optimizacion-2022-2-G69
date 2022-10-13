import numpy as np



matriz = np.identity(45)
matriz2 = np.identity(45)
matriz3 = np.identity(45)
matriz4 = np.identity(45)
matriz5 = np.identity(45)
matriz6 = np.identity(45)
matriz7 = np.identity(45)
matriz8 = np.identity(45)


matriz = matriz.tolist()
matriz2 = matriz2.tolist()
matriz3 = matriz3.tolist()
matriz4 = matriz4.tolist()
matriz5 = matriz5.tolist()
matriz6 = matriz6.tolist()
matriz7 = matriz7.tolist()
matriz8 = matriz8.tolist()


matrices = []

matrices.append(matriz)
matrices.append(matriz2)
matrices.append(matriz3)
matrices.append(matriz4)
matrices.append(matriz5)
matrices.append(matriz6)
matrices.append(matriz7)
matrices.append(matriz8)





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
