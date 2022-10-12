from matrix import construir_matrix

matrix = construir_matrix()
K1 = ["Santiago", "Recoleta", "Estación Central","Ñuñoa", "Macul", "Peñalolén","La Florida", "La Pintana", "El bosque","Providencia","San Bernardo","La Granja","San Miguel", "Cerrillos","Independencia"]
Q_fjk = dict()
matrix.pop(0)
familia = 1
comuna = 1
for fila in matrix:
    cont2 = 0
    fila.pop(0)
    for k in K1:
        for i in range(1,4):
            add = {(familia,i,k): fila[cont2]}
            Q_fjk.update(add)
            cont2 += 1
    familia += 1


def obtener_valor(familia, caja, comuna):
    return Q_fjk[(familia,caja,comuna)]
