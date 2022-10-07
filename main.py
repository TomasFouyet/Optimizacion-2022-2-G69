from archivos import tablaNA, tablaNC, tablaCD
from archivos import NutrienteCaja, NutrienteAlimento, CostoDespacho
from gurobipy import Model, GRB, quicksum
from archivos import obtener_nutriente_por_alimento as A_an, obtener_nutrientes_por_caja as R_nj, masa_alimento as M_a, obtener_precio_por_alimentos as P_am, obtener_costo_despacho_por_super as C_mi


modelo = Model("Grupo 69")
modelo.setParam("TimeLimit", 60)

# Agregar Conjuntos #

j = {1, 2, 3}
m = {"Lider", "Tottus", "Unimarc", "Acuenta"}
a = {"Aceite de maravilla", "Arroz", "Avena", "Azúcar", "Crema de LEche", "Espirales", "Harina", "Jugo en Polvo",
     "Jurel", "Leche entera en polvo", "Leche entera líquida", "Lentejas", "Sal", "Salsa de tomate", "Sucedaneo de cafe", "Té para preparar"}
n = {"Magnesio", "Calcio", "Fósforo", "Sodio", "Potasio", "Hierro", "Zinca", "Yodo"}
i = {1, 2, 3, 4, 5}
k = {}
b = {}
e = {}
t = {}

# Agregar Parametros #

D_ik = None
C_max = 7000
H = 25000
U = 220.45
F_i = None
H_k = None
##  R_nj LISTO  ##
##  A_an LSITO  ##
E = 300
##   M_a LISTO  ## 
L = 1200
Pre = 85000000000
##  P_am LISTO  ##
##  C_mi LISTO  ##


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