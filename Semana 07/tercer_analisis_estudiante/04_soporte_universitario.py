"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).
total_minutos = 0 
conteo_categorias = {
    "Acceso": 0, 
    "Equipo": 0,
    "Red": 0 
}
pendientes = 0 
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = ("", 0)

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.


# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
for incidencia in incidencias: 
    
    total_minutos = total_minutos + incidencia["minutos_atencion"]
    
    categoria = incidencia["categoria"]
    conteo_categorias[categoria] = conteo_categorias[categoria] + 1

# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
    if incidencia["resuelto"] == False:
        pendientes = pendientes + 1
    
        provincias_pendientes.add(incidencia["provincia"])
    
        if incidencia["minutos_atencion"] >= 60: 
            casos_urgentes.append(
                (incidencia["id"], incidencia["minutos_atencion"])
            )
    if incidencia["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (
            incidencia["id"],
            incidencia["minutos_atencion"]
        )

# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
promedio = total_minutos / len(incidencias)

sj_pendientes = "San Jose" in provincias_pendientes 

print("\n", "-" * 60)
print("\t\tANALISIS DE SOPORTE UNIVERSITARIO")
print("-" * 60, "\n")

print("\t\tResultados generales: \n")

print(f"Total de casos: {len(incidencias)}")
print(f"Total de minutos de atencion: {total_minutos}")
print(f"Promedio de minutos: {promedio:.2f}")

print("\n\t\tCasos por categoria:\n")

print(f"Acceso: {conteo_categorias['Acceso']}")
print(f"Equipo: {conteo_categorias['Equipo']}")
print(f"Red: {conteo_categorias['Red']}")

print("\n\t\tCasos pendientes:\n")

print(f"Cantidad de pendientes: {pendientes}")
print(f"Provincias con pendientes: {provincias_pendientes}")

print("\n\t\tCasos urgentes:\n")

print(casos_urgentes)

print("\n\t\tCasos con mas minutos de atencion:\n")

print(f"ID: {caso_mas_largo[0]}")
print(f"Minutos: {caso_mas_largo[1]}")

print("\n¿Hay pendientes en San Jose?: ", sj_pendientes, "\n")