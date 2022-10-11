from archivos import tablaNA, tablaNC, tablaCD
from archivos import NutrienteCaja, NutrienteAlimento, CostoDespacho
from gurobipy import Model, GRB, quicksum
from archivos import obtener_nutriente_por_alimento as A_an, obtener_nutrientes_por_caja as R_nj, masa_alimento as M_a, obtener_precio_por_alimentos as P_am, obtener_costo_despacho_por_super as C_mi, stock_alimentos as N_ma
from random import randint
from archivos import metros_utiles as H_k, precio_arriendo as F_i, distancias as D_ik, minimo


modelo = Model("Grupo 69")
# modelo.setParam("TimeLimit", 1800)

# Agregar Conjuntos #

J = ["1", "2", "3"]
M = ["Lider", "Tottus", "Unimarc", "Acuenta"]
A = ["Aceite de maravilla", "Arroz", "Avena", "Azúcar", "Crema de Leche", "Espirales", "Harina", "Jugo en Polvo",
     "Jurel", "Leche entera en polvo", "Leche entera líquida", "Lentejas", "Sal", "Salsa de tomate", "Sucedaneo de cafe", "Te para preparar"]
N = ["Magnesio", "Calcio", "Fosforo", "Sodio", "Potasio", "Hierro", "Zinc", "Yodo"]
I = ["Santa Rosa", "San Diego", "Sierra Bella","Club Hípico", "Fantasilandia", "Bulnes","Metro Los Orientales", "Las Dalias", "Estadio Manquehue","Macul"]
K = ["Santiago", "Recoleta", "Estación Central","Ñuñoa", "Macul", "Peñalolén","La Florida", "La Pintana", "El bosque","Providencia","San Bernardo","La Granja","San Miguel", "Cerrillos","Independencia"]
B = ["1", "2", "3","4", "5"]
E = ["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12","13", "14", "15"]
T = ["1", "2", "3","4", "5"]
F = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Agregar Parametros #


##  D_ik LISTO  ##
C_max = 7000
H = 25000
U = 220.45
##  F_i LISTO  ##
##  H_k LISTO  ##
# R_nj = "LISTO"  ##
# A_an = "LISTO"  ##
E_t = 300
##   M_a LISTO  ## 
L = 1200
Pre = 85000000000
##  N_ma LISTO  ## 
##  P_am LISTO  ##
##  C_mi LISTO  ##

Q_fjk = None


# Agregar Variables #
 
# Cantidad de cajas “j” asignadas en un lugar de acopio “k”.#
x_jk = modelo.addVars(J, K, vtype=GRB.INTEGER, name="x_jk")

#Cantidad de alimento “a” enviado a “i” que es comprado a proveedor “m”.#
y_aim = modelo.addVars(A, I, M, vtype=GRB.INTEGER, name="y_aim")

# 1 si se esta utilizando la bodega "i" #
z_i = modelo.addVars(I, vtype=GRB.BINARY, name="z_i")

# 1 si se compra al proveedor “m” y hace envío a bodega “i” # 
v_mi = modelo.addVars(M, I, vtype=GRB.BINARY, name="v_mi")

# 1 si el camión “b” tiene asignado un lugar de acopio “k” #
phi_bki = modelo.addVars(B, K, I, vtype=GRB.BINARY, name="phi_bk")

#cantidad de unidades de alimento “a” en la caja de tipo “j”
o_aj = modelo.addVars(A, J, vtype=GRB.INTEGER, name="o_aj")

# 1 si familia “i” vive cercano a centro de entrega “k” y se le entrega una caja tipo “j” #
u_fjk = modelo.addVars(F, J, K, vtype=GRB.BINARY, name="u_fjk")





# VARIABLES EN REVISIÓN #
#1 si el camión “b” está siendo utilizado por un transportista “t”# EN REVISION
w_bt = modelo.addVars(B, T, vtype=GRB.BINARY, name="w_bt")

# 1 si el trabajador “e” ya está en una bodega “i” #
g_ei = modelo.addVars(E, I, vtype=GRB.BINARY, name="g_ei")

#1 si la caja de tipo “j” está asociada a un camión “b”#
lambda_jb = modelo.addVars(J, B, vtype=GRB.BINARY, name="lambda_jb")

# Si la caja de tipo “j” se encuentra en la bodega “i” y 0 e.c.o.c #
y_ji = modelo.addVars(E, I, vtype=GRB.BINARY, name="y_ji")


modelo.update()


# Agregar Restricciones #

modelo.addConstrs((quicksum(u_fjk[f,j,k] for f in F) == x_jk[j, k] for j in J for k in K), name = "R1")

modelo.addConstrs((u_fjk[f,j,k] >= u_fjk[f+1,j,k] for f in range(1,len(F)-1) for j in J for k in K), name = "R2")

# modelo.addConstrs((Q_fjk[f,j,k] >= u_fjk[f,j,k] for f in F for j in J for k in K), name = "R3")

# Restricción 4 implicita #

print(o_aj.keys())
#for a in A:
#     for n in N:
#          print(A_an(a, n))

for j in J:
     for n in N:
          # modelo.addConstrs((quicksum(A_an(a, n) * o_aj[a, int(j)] for a in A) <= R_nj(j, n)), name = "R5")
          modelo.addConstr(((quicksum(int(A_an(a, n)) * o_aj[a, j] for a in A)) <= int(R_nj(j, n))), name = "R5")


modelo.addConstrs((o_aj[a,j] <= 3 for a in A for j in J), name = "R6")

modelo.addConstrs((o_aj[a,j] >= 1 for a in A for j in J), name = "R7")

# Restricción 8 #

modelo.addConstrs(((quicksum(phi_bki[b, k, i] for k in K for i in I)) <= 1 for b in B), name = "R8")

# Restricción 9 #

modelo.addConstrs(((quicksum(phi_bki[b, k, i] for b in B)) * C_max <= quicksum(x_jk[j ,k] * float(M_a(a)) * o_aj[a,j] for j in J for a in A) for k in K for i in I), name = "R9")

# Restricción 10 #

for k in K:
     for i in I:
          for b in B:
               if D_ik(k,i) != minimo(k):
                    modelo.addConstr((D_ik(k, i) -(minimo(k))>=(1-(phi_bki[b,k,i])) ), name = "R10")


# Restricción 11 #

modelo.addConstrs(((quicksum(F_i(i) for i in I) * z_i[i] + quicksum(phi_bki[b,k,i] for b in B for k in K for i in I) * (H + D_ik * (L + U)) + quicksum(x_jk[j, k] for j in J for k in K) * E_t + quicksum(y_aim[a,i,m] for a in A for i in I for m in M) * P_am(a, m) + quicksum(C_mi[m,i]*v_mi[m,i] for m in M for i in I)) <= Pre for a in A for m in M), name = "R11")

# Restricción 12 #

Big_M = 10^10
modelo.addConstrs((Big_M * z_i[i] >= quicksum(y_aim[a,i,m] for a in A for m in M) for i in I), name = "R12.1")
modelo.addConstrs((z_i[i] * 4 >= quicksum(v_mi[m,i] for m in M) for i in I), name = "R12.2")
modelo.addConstrs(((quicksum(y_aim[a, i, m] for a in A)) <= v_mi[m,i] for m in M for i in I), name = "R12.3")

# Restricción 13 #

modelo.addConstrs((quicksum(phi_bki[b,k,i] for b in B for k in K) >= z_i[i] for i in I), name = "R13")

# Restricción 14 #

modelo.addConstrs((quicksum(y_aim[a, i, m] for a in A for i in I for m in M)) == quicksum(x_jk[j ,k] for j in J for k in K) * quicksum(o_aj[a, j] for a in A for j in J), name = "R14")

modelo.addConstrs((quicksum(y_aim[a,i,m] for i in I) <= N_ma for m in M for a in A), name = "R15")

modelo.addConstrs((quicksum(x_jk[j, k] for j in J) <= H_k(k) for k in K), name = "R16")


modelo.update()


funcion_objetivo = quicksum(x_jk[j, k] for j in J for k in K)
modelo.setObjective(funcion_objetivo, GRB.MAXIMIZE)
modelo.optimize()