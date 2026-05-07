# 1. Definimos una lista vacía para guardar los gastos
gastos = []

def agregar_gasto():
    print("--- Registro de Gasto ---")
    nombre = input("¿En qué gastaste? ")
    monto = float(input("¿Cuánto costó? ")) # Convertimos el texto a número decimal
    
    # Guardamos un "diccionario" dentro de la lista
    gastos.append({"item": nombre, "monto": monto})
    print(f"¡Listo! Gastaste {monto} en {nombre}.\n")

def mostrar_total():
    total = sum(gasto["monto"] for gasto in gastos)
    print(f"--- TOTAL ACUMULADO: ${total} ---")
    if total > 5000:
        print("Cuidado: Estás gastando mucho.\n")

# Bucle principal para que el programa no se cierre
while True:
    accion = input("¿Qué querés hacer? (1: Agregar / 2: Ver Total / 3: Salir): ")
    if accion == "1":
        agregar_gasto()
    elif accion == "2":
        mostrar_total()
    elif accion == "3":
        break