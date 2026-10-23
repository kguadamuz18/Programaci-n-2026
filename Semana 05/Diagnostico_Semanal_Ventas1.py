ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)

menor_centro = min(ventas_centro) #Venta minima
mayor_centro = max(ventas_centro) #Venta maxima
promedio_centro = total_centro / cantidad_centro

porcentaje_centro = (total_centro * 100) / meta_centro

#print(porcentaje_centro)

# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)

menor_norte = min(ventas_norte) #Venta minima
mayor_norte = max(ventas_norte) #Venta maxima
promedio_norte = total_norte / cantidad_norte

porcentaje_norte = (total_norte * 100) / meta_norte

#print(porcentaje_norte)

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = "Meta superada"
    
elif total_centro ==meta_centro:
    estado_centro = "Meta lograda"
    
else:
    estado_centro = "Meta no alcanzada"
    
if total_norte > meta_norte:
    estado_norte = "Meta superada"
    
elif total_norte ==meta_centro:
    estado_norte = "Meta lograda"
    
else:
    estado_norte = "Meta no alcanzada"
    

#print(estado_norte)
#print(estado_centro)

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_gano = "Tienda Centro"
    
elif total_norte > total_centro:
    tienda_gano = "Tienda del norte"
    
else:
    tienda_gano = "Ambas tiendas tienen el mismo total" 
# TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.
print("\t\tCOMPARACION SEMANAL DE TIENDAS")
print("-" * 60, "\n")
print(f"Tienda Centro | Total ${total_centro:,.2f} | Meta centro ${meta_centro:,.2f} | Cumplimiento {porcentaje_centro:.0f}% ")
print(f"Centro logro: {estado_centro}")

print("-" * 60, "\n")
print(f"Tienda Norte | Total ${total_norte:,.2f} | Meta centro ${meta_norte:,.2f} | Cumplimiento {porcentaje_norte:.0f}% ")
print(f"Norte logro: {estado_norte}")

print("-" * 60, "\n")
print(f"Tienda con mayor ventas: {tienda_gano}")