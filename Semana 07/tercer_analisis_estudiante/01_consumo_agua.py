"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.

consumo_total = sum(consumos_litros)
promedio = consumo_total / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
ahorro = consumos_litros[0] - consumos_litros[4]

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
porcentaje = (ahorro/consumos_litros[0])

if porcentaje >=15:
    clasificacion = "Reduccion alta"
    
elif porcentaje >0:
    clasificacion = "Reduccion moderada"
    
else:
    clasificacion = "Sin reduccion"

# TODO: Muestre los cinco resultados.
print("-" * 60, "\n")
print("\t\tCONSUMO DIARIO DE AGUA")
print("-" * 60, "\n")
print("Consumo total: ", consumo_total, "L")
print("Promedio diario: ", promedio, "L")
print("Litros ahorrados: ", ahorro, "L")
print("Porcentaje de reduccion: ", porcentaje, "%")
print("Clasificacion: ", clasificacion, "\n")

print("-" * 60, "\n")
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
