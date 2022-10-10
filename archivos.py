from cmath import cos
import csv
from prettytable import PrettyTable

NutrienteAlimento = []
with open("./BDD/NutrienteAlimento.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        NutrienteAlimento.append(row)
tablaNA = PrettyTable()
tablaNA.field_names = NutrienteAlimento[0]
for i in range(1, len(NutrienteAlimento)):
    tablaNA.add_row(NutrienteAlimento[i])

NutrienteCaja = []
with open("./BDD/NutrientesCaja.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        NutrienteCaja.append(row)
tablaNC = PrettyTable()
tablaNC.field_names = NutrienteCaja[0]
for i in range(1, len(NutrienteCaja)):
    tablaNC.add_row(NutrienteCaja[i])

CostoDespacho = []
with open("./BDD/CostoDespacho.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        CostoDespacho.append(row)
tablaCD = PrettyTable()
tablaCD.field_names = CostoDespacho[0]
for i in range(1, len(CostoDespacho)):
    tablaCD.add_row(CostoDespacho[i])

PrecioAlimento = []
with open("./BDD/PrecioAlimento.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        PrecioAlimento.append(row)
tablaPA = PrettyTable()
tablaPA.field_names = PrecioAlimento[0]
for i in range(1, len(PrecioAlimento)):
    tablaPA.add_row(PrecioAlimento[i])

StockAlimentos = []
with open("./BDD/StockAlimentos.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        StockAlimentos.append(row)
tablaSA = PrettyTable()
tablaSA.field_names = StockAlimentos[0]
for i in range(1, len(StockAlimentos)):
    tablaSA.add_row(StockAlimentos[i])

LugaresAcopio = []
with open("./BDD/LugaresAcopio.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        LugaresAcopio.append(row)
tablaLA = PrettyTable()
tablaLA.field_names = LugaresAcopio[0]
for i in range(1, len(LugaresAcopio)):
    tablaLA.add_row(LugaresAcopio[i])

print(tablaLA)

# Conjunto Nutrientes por Alimento #

Nutrientes_Alimento = dict()

for i in range(1, len(NutrienteAlimento)):
    add = {NutrienteAlimento[i][0]: {"Unidad x Kg": NutrienteAlimento[i][1], 
                                    "Magnesio": NutrienteAlimento[i][2],
                                    "Calcio": NutrienteAlimento[i][3],
                                    "Fosforo":  NutrienteAlimento[i][4],
                                    "Sodio": NutrienteAlimento[i][5],
                                    "Potasio": NutrienteAlimento[i][6],
                                    "Hierro": NutrienteAlimento[i][7],
                                    "Zinc": NutrienteAlimento[i][8],
                                    "Yodo": NutrienteAlimento[i][9]}}
    Nutrientes_Alimento.update(add)

# Conjunto Costo Despacho Por Supermercado a bodega i # 

Costos_Despacho = dict()
for i in range(1, len(CostoDespacho)):
    add = {CostoDespacho[i][0]: {1: CostoDespacho[i][1],
                                 2: CostoDespacho[i][2],
                                 3: CostoDespacho[i][3],
                                 4: CostoDespacho[i][4],
                                 5: CostoDespacho[i][5],
                                 6: CostoDespacho[i][6],
                                 7: CostoDespacho[i][7],
                                 8: CostoDespacho[i][8],
                                 9: CostoDespacho[i][9]}}
    Costos_Despacho.update(add)

# Conjunto cantidad de nutriente por tipo de caja # 

Nutrientes_Caja = dict()
for i in range(1, len(NutrienteCaja)):
    add = {NutrienteCaja[i][0]: {"Magnesio": NutrienteCaja[i][1],
                                 "Calcio": NutrienteCaja[i][2],
                                 "Fosforo":  NutrienteCaja[i][3],
                                 "Sodio": NutrienteCaja[i][4],
                                 "Potasio": NutrienteCaja[i][5],
                                 "Hierro": NutrienteCaja[i][6],
                                 "Zinc": NutrienteCaja[i][7],
                                 "Yodo": NutrienteCaja[i][8]}}
    Nutrientes_Caja.update(add)

Precio_Alimentos = dict()
for i in range(1, len(PrecioAlimento)):
    add = {PrecioAlimento[i][0]: {"Lider": PrecioAlimento[i][1],
                                  "Tottus": PrecioAlimento[i][2],
                                  "Unimcarc": PrecioAlimento[i][3],
                                  "Acuenta": PrecioAlimento[i][4]}}
    Precio_Alimentos.update(add)


Stock_Alimentos = dict()
for i in range(1, len(StockAlimentos)):
    add = {StockAlimentos[i][0]: {"Lider": StockAlimentos[i][1],
                                  "Tottus": StockAlimentos[i][2],
                                  "Unimcarc": StockAlimentos[i][3],
                                  "Acuenta": StockAlimentos[i][4]}}
    Stock_Alimentos.update(add)


Lugares_Acopio = dict()
for i in range(1, len(LugaresAcopio)):
    add = {LugaresAcopio[i][0]: {"m2 utiles": LugaresAcopio[i][1],
                                  "precio": LugaresAcopio[i][2]}}
    Lugares_Acopio.update(add)


def obtener_nutriente_por_alimento(alimento, nutriente):
    return Nutrientes_Alimento[alimento][nutriente]

def obtener_costo_despacho_por_super(super, bodega):
    return Costos_Despacho[super][bodega]

def obtener_nutrientes_por_caja(caja, nutriente):
    print("entra aqui")
    return Nutrientes_Caja[caja][nutriente]

def masa_alimento(alimento):
    return Nutrientes_Alimento[alimento]["Unidad x Kg"]

def obtener_precio_por_alimentos(alimento, super):
    return Precio_Alimentos[alimento][super]

def stock_alimentos(alimento, super):
    return Stock_Alimentos[alimento][super]

def metros_utiles(comuna):
    return Lugares_Acopio[comuna]["m2 utiles"] # como comuna recibe un numero

def precio_arriendo(comuna):
    return Lugares_Acopio[comuna]["precio"]