from archivos import tablaNA, tablaNC, tablaCD
from archivos import NutrienteCaja, NutrienteAlimento, CostoDespacho
from gurobipy import Model, GRB, quicksum


modelo = Model("Grupo 69")
modelo.setParam("TimeLimit", 60)

# Agregar Parametros #

tipo_caja = {1, 2, 3}


# Agregar Variables #
 
# Cantidad de cajas “j” asignadas en un lugar de acopio “k”.#
X_jk = modelo.addVars(j, k, GRB.INTEGER, name="X_jk")

#Cantidad de alimento “a” enviado a “i” que es comprado a proveedor “m”.#
Y_aim = modelo.addVars(a, i, m. GRB.INTEGER, name="Y_aim")

#1 si el camión “b” está siendo utilizado por un transportista “t”#
W_bt = modelo.addVars(b, t, GRB.BINARY, name="W_bt")

# 1 si se esta utilizando la bodega "i" #
Z_i = modelo.addVars(i, GRB.BINARY, name="Z_i")

# 1 si el trabajador “e” ya está en una bodega “i” #
G_ei = modelo.addVars(e, i, GRB.BINARY, name="G_ei")

# 1 si se compra al proveedor “m” y hace envío a bodega “i” # 
V_mi = modelo.addVars(m, i, GRB.BINARY, name="V_mi")