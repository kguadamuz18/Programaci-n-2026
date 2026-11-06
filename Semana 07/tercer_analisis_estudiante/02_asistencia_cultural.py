"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

total = 0
bloques = 0

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
for asistencia in asistencias: 
    total =+ asistencia
    
    if asistencia > (capacidad * 0.70):
        bloques =+ 1

# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total / len(asistencias)
porcentaje = (promedio / capacidad) * 100

# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje >= 80: 
    estado = "Ocupacion alta"
    
elif porcentaje >= 50:
    estado = "Ocupacion media"
    
else: 
    estado = "Ocupacion baja"

# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
print("-" * 60, "\n")
print("\t\tANALISIS DE ASISTENCIA")
print("-" * 60, "\n")

print(f"Total de asistentes: {total}")
print(f"Promedio de asistencia: {promedio:.2f}")
print(f"Porcentaje de ocupacion: {porcentaje:.2f} %")
print(f"Bloques que superan el 70%: {bloques}")
print(f"Estado de ocupacion: {estado} \n")

print("-" * 60, "\n")