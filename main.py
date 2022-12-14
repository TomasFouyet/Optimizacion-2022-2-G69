from gurobipy import Model, GRB, quicksum
from lectura_archivos import obtener_precio_por_alimentos as P_am, obtener_costo_despacho_por_super as C_mi, stock_alimentos as N_ma
from random import randint
from lectura_archivos import precio_arriendo as F_i, distancias as D_ik
from lectura_archivos import alimentos_por_caja as O_aj
from prueba import obtener_valor as Q_fjk


modelo = Model("Grupo 69")
modelo.setParam("TimeLimit", 300)

# Agregar Conjuntos #

J = ["1", "2", "3"]
M = ["Lider", "Tottus", "Unimarc", "Acuenta"]
A = ["Aceite de maravilla", "Arroz", "Avena", "Azúcar", "Crema de Leche", "Espirales", "Harina", "Jugo en Polvo",
     "Jurel", "Leche entera en polvo", "Leche entera líquida", "Lentejas", "Sal", "Salsa de tomate", "Sucedaneo de cafe", "Te para preparar"]
N = ["Magnesio", "Calcio", "Fosforo", "Sodio", "Potasio", "Hierro", "Zinc", "Yodo"]
I = ["Santa Rosa", "San Diego", "Sierra Bella","Club Hípico", "Fantasilandia", "Bulnes","Metro Los Orientales", "Las Dalias", "Estadio Manquehue","Macul"]
K = ["Santiago", "Recoleta", "Estación Central","Ñuñoa", "Macul", "Peñalolén","La Florida", "La Pintana", "El bosque","Providencia","San Bernardo","La Granja","San Miguel", "Cerrillos","Independencia"]
B = ["1", "2", "3","4", "5", "6", "7", "8", "9", "10", "11", "12", "13","14", "15", "16"]
#E = ["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12","13", "14", "15"]
#T = ["1", "2", "3","4", "5"]
F = ["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12","13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31","32", "33", "34","35", "36", "37","38", "39", "40", "41", "42", "43", "44", "45"]

F_num = range (1, 361)
F =[]
for f in F_num:
     f = str(f)
     F.append(f)
# Agregar Parametros #


##  D_ik LISTO  ##
C_max = 700000
H = 25000
#25000
U = 220.45
##  F_i LISTO  ##
##  H_k LISTO  ##
# R_nj = "LISTO"  ##
# A_an = "LISTO"  ##
E_t = 200
##   M_a LISTO  ## 

L = 1200

Pre = 350457261
#85000000000
Big_M = 10^10000

##  N_ma LISTO  ## 
##  P_am LISTO  ##
##  C_mi LISTO  ##


##  O_aj  LISTO  ##
##  Q_fjk LISTO  ##


# Agregar Variables #
 
# Cantidad de cajas “j” asignadas en un lugar de acopio “k”#
x_jk = modelo.addVars(J, K, vtype=GRB.INTEGER, name="x_jk")

#Cantidad de alimento “a” enviado a “i” que es comprado a proveedor “m”.#
y_aim = modelo.addVars(A, I, M, vtype=GRB.INTEGER, name="y_aim")

# 1 si se esta utilizando la bodega "i" #
z_i = modelo.addVars(I, vtype=GRB.BINARY, name="z_i")

# 1 si se compra al proveedor “m” y hace envío a bodega “i” # 
v_mi = modelo.addVars(M, I, vtype=GRB.BINARY, name="v_mi")

# 1 si el camión “b” tiene asignado un lugar de acopio “k” desde la bodega i#
phi_bki = modelo.addVars(B, K, I, vtype=GRB.BINARY, name="phi_bk")

# 1 si familia “i” vive cercano a centro de entrega “k” y se le entrega una caja tipo “j” #
u_fjk = modelo.addVars(F, J, K, vtype=GRB.BINARY, name="u_fjk")

modelo.update()


# Agregar Restricciones #


modelo.addConstrs((quicksum(u_fjk[f,j,k] for f in F) == x_jk[j, k] for j in J for k in K), name = "R1")

modelo.addConstrs((int(Q_fjk(f,j,k)) >= u_fjk[f,j,k] for f in F for j in J for k in K), name = "R2")

modelo.addConstrs(((quicksum(phi_bki[b, k, i] for k in K for i in I)) <= 1 for b in B), name = "R3")

modelo.addConstrs(((quicksum(float(F_i(i)) * z_i[i] for i in I) + quicksum(phi_bki[b,k,i] * (H + float(D_ik(k, i)) * (L + U)) for b in B for k in K for i in I) + quicksum(x_jk[j, k] for j in J for k in K) * E_t + quicksum(y_aim[a,i,m] for a in A for i in I for m in M) * int(P_am(a, m)) + quicksum(int(C_mi(m,i))*v_mi[m,i] for m in M for i in I)) <= Pre for a in A for m in M), name = "R4")

modelo.addConstrs((Big_M * z_i[i] >= quicksum(y_aim[a,i,m] for a in A for m in M) for i in I), name = "R5")

modelo.addConstrs((z_i[i] * len(M) >= quicksum(v_mi[m,i] for m in M) for i in I), name = "R6")

modelo.addConstrs(((quicksum(y_aim[a, i, m] for a in A)) >= z_i[i] for m in M for i in I), name = "R7")

modelo.addConstrs(((quicksum(y_aim[a, i, m] for a in A)) <= v_mi[m, i] * Big_M for m in M for i in I), name = "R8")

modelo.addConstrs(((quicksum(phi_bki[b, k, i] for k in K for b in B)) <= z_i[i] * Big_M for i in I), name = "R9")

modelo.addConstrs((quicksum(phi_bki[b,k,i] for b in B for k in K) >= z_i[i] for i in I), name = "R10")

modelo.addConstrs(((quicksum(y_aim[a, i, m] for i in I for m in M)) == quicksum(x_jk[j ,k] for j in J for k in K) * quicksum(int(O_aj(a, j)) for j in J) for a in A), name = "R11")

modelo.addConstrs((quicksum(y_aim[a,i,m] for i in I) <= int(N_ma(a, m)) for m in M for a in A), name = "R12")

modelo.addConstrs((quicksum(x_jk[j,k] for j in J)<= quicksum(phi_bki[b, k, i] * Big_M for b in B for i in I)for k in K), name = "R13")


modelo.update()

funcion_objetivo = quicksum(x_jk[j, k] for j in J for k in K)

modelo.setObjective(funcion_objetivo, GRB.MAXIMIZE)

modelo.optimize()
 
valor_objetivo = modelo.ObjVal
print(f"El valor objetivo es: {valor_objetivo}")

#for constr in modelo.getConstrs():
     #if constr.getAttr("slack") == 0:
          #print("----------------------------------------")
          #print(f"La restricción {constr} está activa")
          #print("----------------------------------------")

print("--------------------- Variable que indica la cantidad de cajas 'j' en la municipalidad 'k'-------------------------")
for j in J:
     for k in K:
          print(f"Hay {x_jk[j,k].x} cajas de tipo {j} en la municipalidad {k}")
print("-------------------------------------------------------------------------------------------------------------------")

print("--------------------- Variable que indica los camiones 'b' en uso y su recorrdio desde 'i' hacia 'k'-------------------------")
for b in B:
     for k in K:
          for i in I:
               var = phi_bki[b,k,i].x
               if var == 1:
                   print(f"El camión {b} esta asignado desde la bodega {i} hacia {k}")
print("-------------------------------------------------------------------------------------------------------------------")

print("--------------------- Variable que indica los camiones 'a' se compra en el proveedor 'm' y su bodega respectiva 'i'-------------------------")
for a in A:
     for m in M:
          for i in I:
               var = y_aim[a,i,m].x
               if var != 0:
                    print(f"Se le compra {var} de {a} al provedor {m}  a un precio unitario de ${P_am(a,m)} y se almacena en la bodega '{i}'")
print("-------------------------------------------------------------------------------------------------------------------")



print("--------------------- Variable que indica si la bodega 'i' esta en uso-------------------------")
for i in I:
     var = z_i[i].x
     if var == 1:
          print(f"La bodega {i} se esta usando y cuesta ${F_i(i)}")
print("-------------------------------------------------------------------------------------------------------------------")

print("--------------------- Variable que indica si la bodega se le compra al proveedor 'm' y cual bodega 'i' se usará para almacenar-------------------------")
for m in M:
     for i in I:
          var = v_mi[m,i].x
          if var == 1:
               print(f"Se le compra a {m} y se guarda en la bodega '{i}' a un costo asociado al despacho de ${C_mi(m,i)}")

print("-------------------------------------------------------------------------------------------------------------------")

print("--------------------- Variable que indica si la bodega se la familia 'f' recibe su caja de tipo 'j' adecuada en la comuna 'k'-------------------------")
for f in F:
     for k in K:
          for j in J:
               if u_fjk[f,j,k].x == 1:
                    print(f"La familia {f} que vive en {k} recibe su caja correspondiente de tipo {j}")
print("-------------------------------------------------------------------------------------------------------------------")


#ESCRIBIR EN EL CSV






# RESTRICCIONES EN REVISIÓN #
#modelo.addConstrs((u_fjk[str(f),j,k] >= u_fjk[str(f+1),j,k] for f in range(1,len(F)-1) for j in J for k in K), name = "R2")


#modelo.addConstrs((quicksum(u_fjk[str(f),j,k] for j in J for k in K) >= quicksum(u_fjk[str(f+1),j,k] for j in J for k in K) for f in range(1,len(F)-1)), name = "R14")
#modelo.addConstrs((quicksum(x_jk[j, k] for j in J) <= H_k(k) for k in K), name = "R16")

#Se necesitará cuando se agrande la matriz
#modelo.addConstrs(((quicksum(phi_bki[b, k, i] for b in B)) * C_max >= quicksum(x_jk[j ,k] * float(M_a(a)) * int(O_aj(a,j)) for j in J for a in A) for k in K for i in I), name = "R9") 

#RESTRICCION TRAYECTO ARREGLAR
#modelo.addConstrs((float(D_ik(i, k) - (minimo(k))) >= 1-(phi_bki[b,k,i]) for b in B for k in K for i in I), name = "R10")
