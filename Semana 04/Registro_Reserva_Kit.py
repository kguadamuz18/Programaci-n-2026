# TODO: solicita los datos.
# TODO: limpia los textos.
# TODO: convierte los números con try.
# TODO: valida las entradas.
# TODO: aplica las reglas.
# TODO: muestra el resultado.

nombre = input("Nombre: ").upper().strip()
kit = input('Tipo de kit: ')
autorizacion = input("Tiene autorizacion (si/no)?").lower().strip() == 'si'

try: 
    cantidad = int(input("Cantidad de kits?: "))
    if cantidad < 1:
        print("Error: la cantidad minima es 1")
except ValueError:
    print("Cantidad de kits invalida, digite del 1 al 100")
    cantidad = -1
    
try: 
    dias = int(input("Días de préstamo: "))
except ValueError:
    print("Cantidad de días invalido, digite del 1 al 100")
    dias = -1

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "registro rechazado: revise los datos ingresados!"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kits de {kit}"
    
else:
    resultado = "Solicitud enviada a revision"


print("-" * 60,'\n')
print(resultado)