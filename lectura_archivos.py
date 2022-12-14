import csv
from prettytable import PrettyTable

CostoDespacho = []
with open("BDD/CostoDespacho.csv", encoding="UTF-8") as file:
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


Distancias = []
with open("./BDD/Distancias.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        Distancias.append(row)
tablaD = PrettyTable()
tablaD.field_names = Distancias[0]
for i in range(1, len(Distancias)):
    tablaD.add_row(Distancias[i])


AlimentosCaja = []
with open("./BDD/AlimentosPorCaja.csv", encoding="UTF-8") as file:
    read = csv.reader(file)
    for row in read:
        AlimentosCaja.append(row)
tablaAD = PrettyTable()
tablaAD.field_names = AlimentosCaja[0]
for i in range(1, len(AlimentosCaja)):
    tablaAD.add_row(AlimentosCaja[i])


# Conjunto Costo Despacho Por Supermercado a bodega i # 

Costos_Despacho = dict()
for i in range(1, len(CostoDespacho)):
    add = {CostoDespacho[i][0]: {"Santa Rosa": CostoDespacho[i][1],
                                 "San Diego": CostoDespacho[i][2],
                                 "Sierra Bella": CostoDespacho[i][3],
                                 "Club H??pico": CostoDespacho[i][4],
                                 "Fantasilandia": CostoDespacho[i][5],
                                 "Bulnes": CostoDespacho[i][6],
                                 "Metro Los Orientales": CostoDespacho[i][7],
                                 "Las Dalias": CostoDespacho[i][8],
                                 "Estadio Manquehue": CostoDespacho[i][9],
                                 "Macul": CostoDespacho[i][10]}}
    Costos_Despacho.update(add)
 

Precio_Alimentos = dict()
for i in range(1, len(PrecioAlimento)):
    add = {PrecioAlimento[i][0]: {"Lider": PrecioAlimento[i][1],
                                  "Tottus": PrecioAlimento[i][2],
                                  "Unimarc": PrecioAlimento[i][3],
                                  "Acuenta": PrecioAlimento[i][4]}}
    Precio_Alimentos.update(add)


Stock_Alimentos = dict()
for i in range(1, len(StockAlimentos)):
    add = {StockAlimentos[i][0]: {"Lider": StockAlimentos[i][1],
                                  "Tottus": StockAlimentos[i][2],
                                  "Unimarc": StockAlimentos[i][3],
                                  "Acuenta": StockAlimentos[i][4]}}
    Stock_Alimentos.update(add)


Lugares_Acopio = dict()
for i in range(1, len(LugaresAcopio)):
    add = {LugaresAcopio[i][0]: {"m2 utiles": LugaresAcopio[i][1],
                                  "precio": LugaresAcopio[i][2]}}
    Lugares_Acopio.update(add)


Distancia = dict()
for i in range(1, len(Distancias)):
    add = {Distancias[i][0]: {"Santa Rosa": Distancias[i][1],
                                  "San Diego": Distancias[i][2],
                                  "Sierra Bella": Distancias[i][3],
                                  "Club H??pico": Distancias[i][4],
                                  "Fantasilandia": Distancias[i][5],
                                  "Bulnes": Distancias[i][6],
                                  "Metro Los Orientales": Distancias[i][7],
                                  "Las Dalias": Distancias[i][8],
                                  "Estadio Manquehue": Distancias[i][9],
                                  "Macul": Distancias[i][10]}}
    Distancia.update(add)
for comuna in Distancia:
    for sector in Distancia[comuna]:
        Distancia[comuna][sector] = float(Distancia[comuna][sector])


ALimentos_Por_Caja = dict()
for i in range(1, len(AlimentosCaja)):
    add = {AlimentosCaja[i][0]: {"1": AlimentosCaja[i][1], "2": AlimentosCaja[i][2], "3": AlimentosCaja[i][3]}}
    ALimentos_Por_Caja.update(add)


def obtener_costo_despacho_por_super(super, bodega):
    return Costos_Despacho[super][bodega]

def obtener_precio_por_alimentos(alimento, super):
    return Precio_Alimentos[alimento][super]

def stock_alimentos(alimento, super):
    return Stock_Alimentos[alimento][super]


def precio_arriendo(comuna):
    return Lugares_Acopio[comuna]["precio"]

def distancias(comuna, sector):
    return Distancia[comuna][sector]


def alimentos_por_caja(alimento, caja):
    return ALimentos_Por_Caja[alimento][caja]