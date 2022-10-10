from archivos import tablaNA, tablaNC, tablaCD
from archivos import NutrienteCaja, NutrienteAlimento, CostoDespacho
from gurobipy import Model, GRB, quicksum
from archivos import obtener_nutriente_por_alimento as A_an, obtener_nutrientes_por_caja as R_nj, masa_alimento as M_a, obtener_precio_por_alimentos as P_am, obtener_costo_despacho_por_super as C_mi


modelo = Model("Grupo 69")
modelo.setParam("TimeLimit", 1800)

# Agregar Conjuntos #

J = {1, 2, 3}
M = {"Lider", "Tottus", "Unimarc", "Acuenta"}
A = {"Aceite de maravilla", "Arroz", "Avena", "Azúcar", "Crema de LEche", "Espirales", "Harina", "Jugo en Polvo",
     "Jurel", "Leche entera en polvo", "Leche entera líquida", "Lentejas", "Sal", "Salsa de tomate", "Sucedaneo de cafe", "Té para preparar"}
N = {"Magnesio", "Calcio", "Fósforo", "Sodio", "Potasio", "Hierro", "Zinc", "Yodo"}
I = {1, 2, 3, 4, 5}
K = {}
B = {}
E = {}
T = {}
F = {}

# Agregar Parametros #

D_ik = None
C_max = 7000
H = 25000
U = 220.45
F_i = None
H_k = None
# R_nj = "LISTO"  ##
# A_an = "LISTO"  ##
E = 300
##   M_a LISTO  ## 
L = 1200
Pre = 85000000000
##  P_am LISTO  ##
##  C_mi LISTO  ##

Nma = None
Qfjk = None


# Agregar Variables #
 
# Cantidad de cajas “j” asignadas en un lugar de acopio “k”.#
x_jk = modelo.addVars(J, K, GRB.INTEGER, name="x_jk")

#Cantidad de alimento “a” enviado a “i” que es comprado a proveedor “m”.#
y_aim = modelo.addVars(A, I, m. GRB.INTEGER, name="y_aim")

# 1 si se esta utilizando la bodega "i" #
z_i = modelo.addVars(I, GRB.BINARY, name="z_i")

# 1 si se compra al proveedor “m” y hace envío a bodega “i” # 
v_mi = modelo.addVars(M, I, GRB.BINARY, name="v_mi")

# 1 si el camión “b” tiene asignado un lugar de acopio “k” #
phi_bki = modelo.addVars(B, K, I, GRB.BINARY, name="phi_bk")

#cantidad de unidades de alimento “a” en la caja de tipo “j”
o_aj = modelo.addVars(A, J, GRB.BINARY, name="o_aj")

# 1 si familia “i” vive cercano a centro de entrega “k” y se le entrega una caja tipo “j” #
u_fjk = modelo.addVars(F, J, K, GRB.BINARY, name="u_fjk")





# VARIABLES EN REVISIÓN #
#1 si el camión “b” está siendo utilizado por un transportista “t”# EN REVISION
w_bt = modelo.addVars(B, T, GRB.BINARY, name="w_bt")

# 1 si el trabajador “e” ya está en una bodega “i” #
g_ei = modelo.addVars(E, I, GRB.BINARY, name="g_ei")

#1 si la caja de tipo “j” está asociada a un camión “b”#
lambda_jb = modelo.addVars(J, B, GRB.BINARY, name="lambda_jb")

# Si la caja de tipo “j” se encuentra en la bodega “i” y 0 e.c.o.c #
y_ji = modelo.addVars(E, I, GRB.BINARY, name="y_ji")


modelo.update()


# Agregar Restricciones #

modelo.addConstrs((quicksum(u_fjk[f,j,k] for f in F) == x_jk for j in J for k in K), name = "R1")

modelo.addConstrs((u_fjk[f,j,k] >= u_fjk[f+1,j,k] for f in F for j in J for k in K), name = "R2")

modelo.addConstrs((Qfjk[f,j,k] >= u_fjk[f,j,k] for f in F for j in J for k in K), name = "R3")

# Restriccioón 4 implicita #

modelo.addConstrs((quicksum(A_an[a, n] * o_aj for a in A) == R_nj for j in J for n in N), name = "R5")

modelo.addConstrs((o_aj[a,j] <= 3 for a in A for j in J), name = "R6")

modelo.addConstrs((o_aj[a,j] >= 1 for a in A for j in J), name = "R6")

# Restricción 8 #

# Restricción 9 #

# Restricción 10 #

# Restricción 11 #

# Restricción 12 #

# Restricción 13 #

# Restricción 14 #

modelo.addConstrs((quicksum(y_aim[a,i,m] for i in I) <= Nma for m in M for a in A), name = "R15")

modelo.addConstrs((quicksum(x_jk[j, k] for j in J) <= H_k for k in K), name = "R16")






