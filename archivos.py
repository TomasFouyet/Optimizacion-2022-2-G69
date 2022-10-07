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
