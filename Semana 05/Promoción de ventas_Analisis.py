producto = ["Cafe", 5000, 20]

porcentaje_aumento = 20

descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento

ingreso_actual = producto[1] * producto[2]

aumento_unidades = producto[2] * porcentaje_aumento / 100
unidades_proyectadas = producto[2] + aumento_unidades

ingreso_promocion = precio_promocional * unidades_proyectadas
diferencia = ingreso_promocion - ingreso_actual

print("-" * 60, "\n")
print("ANÁLISIS DE PROMOCIÓN")
print()
print(f"Producto: {producto[0]}")
print(f"Precio actual: ₡{producto[1]:.0f}")
print(f"Unidades actuales: {producto[2]}")
print(f"Ingreso actual: ₡{ingreso_actual:.0f}")
print(f"Descuento: ₡{descuento:.0f}")
print(f"Precio promocional: ₡{precio_promocional:.0f}")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%")
print(f"Unidades proyectadas: {unidades_proyectadas:.0f}")
print(f"Ingreso con promoción: ₡{ingreso_promocion:.0f}")
print(f"Diferencia: ₡{diferencia:.0f}")
print()

if diferencia > 0:
    print("RECOMENDACIÓN: lanzar.")