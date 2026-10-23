#Análisis de promoción de ventas.

producto = ["Cafe", 5000, 20]

porcentaje_aumento = 20

# Calcular el descuento y el precio promocional.
descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento

# Calcular el ingreso actual.
ingreso_actual = producto[1] * producto[2]

# Calcular el aumento de unidades y las unidades proyectadas.
aumento_unidades = producto[2] * porcentaje_aumento / 100
unidades_proyectadas = producto[2] + aumento_unidades

# Calcular el ingreso con promoción y la diferencia.
ingreso_promocion = precio_promocional * unidades_proyectadas
diferencia = ingreso_promocion - ingreso_actual

# Decidir si conviene lanzar la promoción.
if diferencia > 0:
    recomendacion = "Lanzar"
else:
    recomendacion = "No lanzar"
    
#Reporte.
print("\t\tANALISIS DE PROMOCION")
print("-" * 50, "\n")

print(f"Producto: {producto[0]}")
print(f"Precio actual: ₡{producto[1]:,.0f}")
print(f"Unidades actuales: {producto[2]}")
print(f"Ingreso actual: ₡{ingreso_actual:,.0f}")

print("-" * 50, "\n")

print(f"Descuento: ₡{descuento:,.0f}")
print(f"Precio promocional: ₡{precio_promocional:,.0f}")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%")
print(f"Unidades proyectadas: {unidades_proyectadas:,.0f}")

print("-" * 50, "\n")

print(f"Ingreso con promocion: ₡{ingreso_promocion:,.0f}")
print(f"Diferencia: ₡{diferencia:,.0f}")
print(f"RECOMENDACION: {recomendacion}")
