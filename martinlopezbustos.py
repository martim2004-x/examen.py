import random
import csv

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", 
                "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", 
                "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

sueldos = []


def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("sueldos aleatorios")


def clasificar_sueldos():
    global sueldos
    sueldos.sort()
    
    sueldos_menores = []
    sueldos_intermedios = []
    sueldos_mayores = []
    
    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            sueldos_menores.append((trabajadores[i], sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            sueldos_intermedios.append((trabajadores[i], sueldo))
        else:
            sueldos_mayores.append((trabajadores[i], sueldo))
    
    print("\nSueldos menores a $800,000")
    print(f"TOTAL: {len(sueldos_menores)}")
    print("Nombre Empleado     Sueldo")
    for nombre, sueldo in sueldos_menores:
        print(f"{nombre} {sueldo}")
    
    print("\nSueldos entre $800,000 y $2,000,000")
    print(f"TOTAL: {len(sueldos_intermedios)}")
    print("Nombre Empleado     Sueldo")
    for nombre, sueldo in sueldos_intermedios:
        print(f"{nombre} {sueldo}")
    
    print("\nSueldos mayores a $2,000,000")
    print(f"TOTAL: {len(sueldos_mayores)}")
    print("Nombre Empleado     Sueldo")
    for nombre, sueldo in sueldos_mayores:
        print(f"{nombre} {sueldo}")
    
    total_sueldos = sum(sueldos)
    print(f"\nTOTAL SUELDOS: {total_sueldos}")


def ver_estadisticas():
    global sueldos
    if not sueldos:
        print("No hay sueldos asignados")
        return
    
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    
    media_geometrica = 1
    for sueldo in sueldos:
        media_geometrica *= sueldo
    media_geometrica = media_geometrica ** (1 / len(sueldos))
    
    print("\nEstadssticas de sueldos:")
    print(f"- sueldo mas alto: {sueldo_maximo}")
    print(f"- sueldo mas bajo: {sueldo_minimo}")
    print(f"- promedio de sueldos: {promedio_sueldos}")
    print(f"- media geometrica de sueldos: {media_geometrica}")


def generar_reporte():
    global trabajadores, sueldos
    if not sueldos:
        print("No hay sueldos asignados")
        return
    
    descuento_salud = 0.07
    descuento_afp = 0.12
    
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        
        for i, trabajador in enumerate(trabajadores):
            sueldo_base = sueldos[i]
            desc_salud = sueldo_base * descuento_salud
            desc_afp = sueldo_base * descuento_afp
            sueldo_liquido = sueldo_base - desc_salud - desc_afp
            
            writer.writerow([trabajador, sueldo_base, desc_salud, desc_afp, sueldo_liquido])
            
            print(f"{trabajador}: ${sueldo_base} - Descuento Salud: ${desc_salud:.2f} - Descuento AFP: ${desc_afp:.2f} - Sueldo Liquido: ${sueldo_liquido:.2f}")


def main():
    while True:
        print("\nMenu de la aplicacion:")
        print("1. asignar sueldos aleatorios")
        print("2. clasificar sueldos")
        print("3. ver estadisticas")
        print("4. generar reporte de sueldos")
        print("5. salir del programa")
        
        opcion = input("selecciona una opcion: ")

        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            generar_reporte()
        elif opcion == '5':
            print("saliendo del programa")
            break
        else:
            print("opcion incorrecta")


if __name__ == "__main__":
    main()
