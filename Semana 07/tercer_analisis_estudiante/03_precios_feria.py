"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo 

# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0 
precios_superiores = 0

while indice < len(precios):
    if precios[indice] > promedio:
        precios_superiores = precios_superiores + 1
        
    indice = indice + 1 

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >=300:
    variacion = "Variacion alta"
    
elif rango >= 150:
    variacion = "Variacion moderada"
    
else: 
    variacion = "Variacion baja"
    
print("\n", "-" * 60)
print("\t\tCOMPARACION DE PRECIOS")
print("-" * 60, "\n")

print("Producto: ", producto)

print(f"\nPromedio de precios: ₡{promedio:.2f}")
print(f"Precio minimo: ₡{minimo}")
print(f"Precio maximo: ₡{maximo}")
print(f"Rango de precios: ₡{rango}")
print(f"Precios superiores al promedio: {precios_superiores}")
print(f"Clasificacion: {variacion}")



# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
print 