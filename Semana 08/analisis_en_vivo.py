"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")


# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
equivalencias = {
    "acetaminofen" : "acetaminofén",
    "paracetamol" : "acetaminofén",
    "antiacido" : "antíacido",
    "losartán" : "losartan"
}

conteo_medicamentos = {}
total_medicamentos = 0 

print("\nANALISIS FASE #1 MUESTRA")
for indice in range (3):
    registro = registros[indice]
    print("\n\t\tINFORMACION DEL PACIENTE\n")
    print("Nombre paciente: ", registro['paciente_nombre'])
    print("Cedula: ", registro['paciente_cedula'])
    print("Diagnostico: ", registro['diagnostico'])
    print("Medicamentos: ", registro['medicamentos'])
    print(type(registro['medicamentos']))
    
    for medicamento in registro['medicamentos']:
        #limpieza
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias: 
            medicamento = equivalencias[medicamento]
        
        #contar medicamentos 
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else: 
            conteo_medicamentos[medicamento] = 1
            
print("Total de medicamentos recetados: ", total_medicamentos)   
print(conteo_medicamentos)
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
conteo_medicamentos = {}
total_medicamentos = 0 

print("\n ANALISIS FASE #2 MEDICAMENTOS Y ATENCIONES")
for registro in registros:
    for medicamento in registro['medicamentos']:
            #limpieza
            medicamento = medicamento.strip().lower()
            if medicamento in equivalencias: 
                medicamento = equivalencias[medicamento]
            
            #contar medicamentos 
            total_medicamentos += 1
            if medicamento in conteo_medicamentos:
                conteo_medicamentos[medicamento] += 1
            else: 
                conteo_medicamentos[medicamento] = 1
print("\nTotal de medicamentos recetados: ", total_medicamentos)   
for medicamento, cantidad in conteo_medicamentos.items(): 
    
    print(f"- {medicamento}: {cantidad}")

# FASE 3: CONTAR ATENCIONES POR HOSPITAL
print("\n ANALISIS FASE #3 ATENCIONES POR HOSPITAL")

conteo_hospital = {}
total_paciente = 0 

for registro in registros:
    for hospitales in registro['hospital']:
        total_paciente += 1
        
        if hospitales in conteo_hospital: 
            conteo_hospital[hospitales] += 1
        else: 
            conteo_hospital[hospitales] = 1
for hospitales, cantidad in conteo_hospital.items(): 
    
    print(f"- {hospitales}: {cantidad}")
# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA

