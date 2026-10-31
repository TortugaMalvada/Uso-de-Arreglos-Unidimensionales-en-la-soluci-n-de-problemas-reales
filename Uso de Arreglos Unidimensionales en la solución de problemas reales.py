# Sistema Básico de Gestión de Inventario
# Basado en Arreglos Unidimensionales (Listas Paralelas)

def mostrar_menu():
    """Muestra el menú principal de opciones del sistema."""
    print("    SISTEMA DE GESTIÓN DE INVENTARIO      ")
    print("1. Registrar nuevo producto o pedido")
    print("2. Mostrar listado actual")
    print("3. Editar producto o pedido existente")
    print("4. Eliminar producto o pedido")
    print("5. Salir")


def registrar_producto(nombres, cantidades, precios):
    """Registra un nuevo elemento utilizando arreglos unidimensionales paralelos."""
    print("\n--- REGISTRAR NUEVO ELEMENTO ---")
    nombre = input("Ingrese el nombre del producto o pedido: ").strip()
    
    if not nombre:
        print(" Error: El nombre no puede estar vacío.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad < 0:
            print(" Error: La cantidad no puede ser negativa.")
            return
            
        precio = float(input("Ingrese el precio unitario ($): "))
        if precio < 0:
            print(" Error: El precio no puede ser negativo.")
            return
            
        # Almacenamiento en los arreglos unidimensionales
        nombres.append(nombre)
        cantidades.append(cantidad)
        precios.append(precio)
        print(f"¡Éxito! '{nombre}' ha sido registrado correctamente.")
        
    except ValueError:
        print(" Error: Debe ingresar valores numéricos válidos para la cantidad y el precio.")


def mostrar_inventario(nombres, cantidades, precios):
    """Recorre e imprime el listado de elementos almacenados (Iteración y Lectura)."""
    print("\n--- LISTADO ACTUAL DE INVENTARIO Y PEDIDOS ---")
    
    if len(nombres) == 0:
        print("El sistema se encuentra vacío actualmente.")
        return

    # Encabezado de tabla formateada
    print(f"{'Índice':<8} | {'Nombre / Descripción':<25} | {'Cantidad':<10} | {'Precio ($)':<10}")
    print("-" * 60)
    
    # Iteración sobre los arreglos unidimensionales
    for i in range(len(nombres)):
        print(f"{i:<8} | {nombres[i]:<25} | {cantidades[i]:<10} | {precios[i]:<10.2f}")


def editar_producto(nombres, cantidades, precios):
    """Modifica los datos de un elemento existente seleccionándolo por su índice."""
    print("\n--- EDITAR ELEMENTO ---")
    
    if len(nombres) == 0:
        print("No hay elementos registrados para editar.")
        return

    mostrar_inventario(nombres, cantidades, precios)
    
    try:
        indice = int(input("\nIngrese el índice del elemento que desea editar: "))
        
        if indice < 0 or indice >= len(nombres):
            print(" Error: El índice ingresado está fuera de rango.")
            return

        print(f"Editando elemento seleccionado: {nombres[indice]}")
        
        # Actualización de Nombre
        nuevo_nombre = input(f"Nuevo nombre [Actual: {nombres[indice]}]: ").strip()
        if nuevo_nombre:
            nombres[indice] = nuevo_nombre

        # Actualización de Cantidad
        nueva_cantidad_str = input(f"Nueva cantidad [Actual: {cantidades[indice]}]: ").strip()
        if nueva_cantidad_str:
            nueva_cantidad = int(nueva_cantidad_str)
            if nueva_cantidad >= 0:
                cantidades[indice] = nueva_cantidad
            else:
                print(" Cantidad inválida, se conservará la anterior.")

        # Actualización de Precio
        nuevo_precio_str = input(f"Nuevo precio [Actual: {precios[indice]}]: ").strip()
        if nuevo_precio_str:
            nuevo_precio = float(nuevo_precio_str)
            if nuevo_precio >= 0:
                precios[indice] = nuevo_precio
            else:
                print("Precio inválido, se conservará el anterior.")

        print("¡Elemento actualizado exitosamente!")
        
    except ValueError:
        print(" Error: Entrada no válida. Asegúrese de ingresar números correctos.")


def eliminar_producto(nombres, cantidades, precios):
    """Elimina un elemento del sistema manteniendo la consistencia de los arreglos."""
    print("\n--- ELIMINAR ELEMENTO ---")
    
    if len(nombres) == 0:
        print("No hay elementos registrados para eliminar.")
        return

    mostrar_inventario(nombres, cantidades, precios)

    try:
        indice = int(input("\nIngrese el índice del elemento que desea eliminar: "))
        
        if indice < 0 or indice >= len(nombres):
            print(" Error: El índice ingresado está fuera de rango.")
            return

        # Eliminación simultánea en todos los arreglos usando pop()
        nombre_eliminado = nombres.pop(indice)
        cantidades.pop(indice)
        precios.pop(indice)
        
        print(f"¡Éxito! El elemento '{nombre_eliminado}' ha sido eliminado del sistema.")
        
    except ValueError:
        print(" Error: Debe ingresar un valor numérico entero para el índice.")


def principal():
    """Función principal que controla el flujo y el ciclo de ejecución del programa."""
    # Declaración de arreglos unidimensionales (listas paralelas)
    nombres = []
    cantidades = []
    precios = []

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ").strip()

        if opcion == '1':
            registrar_producto(nombres, cantidades, precios)
        elif opcion == '2':
            mostrar_inventario(nombres, cantidades, precios)
        elif opcion == '3':
            editar_producto(nombres, cantidades, precios)
        elif opcion == '4':
            eliminar_producto(nombres, cantidades, precios)
        elif opcion == '5':
            print("\n¡Gracias por utilizar el sistema de gestión! Saliendo...")
            break
        else:
            print("\n Opción no válida. Por favor, seleccione un número entre 1 y 5.")


# Punto de entrada del programa
if __name__ == "__main__":
    principal()
