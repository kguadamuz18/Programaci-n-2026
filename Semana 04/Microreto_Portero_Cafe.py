"""Microreto: el portero del café."""

nombre = input("¿Como te llamas?: ").upper().strip()

energia = int(input("Cuanta energia tiene de 0 a 100?: "))

trae_cafe = input("Traes café (si/no)?): ").lower().strip() == 'si'

if (energia < 50) and (trae_cafe is False):
    mensaje = 'Vaya a descansar'
    
elif (energia > 50) or (trae_cafe):
    mensaje = 'Puede ingresar a la clase'
    
else:
    mensaje = 'Revise sus respuestas'

print(f"{nombre}: {mensaje}")

