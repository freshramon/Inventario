# app.py
from servicios import *
from archivos import *

menu()
inventario = []
star = 1

while star != 0:
    try:
        menu()
        opcion = int(input("Marque aqui la opción que desea ejecutar: "))

        if opcion == 1:
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nombre = input("Buscar: ")
            print(buscar_producto(inventario, nombre))

        elif opcion == 4:
            nombre = input("Producto: ")
            precio = input("Nuevo precio (enter para omitir): ")
            cantidad = input("Nueva cantidad (enter para omitir): ")

            actualizar_producto(
                inventario,
                nombre,
                float(precio) if precio else None,
                int(cantidad) if cantidad else None
            )

        elif opcion == 5:
            nombre = input("Eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == 6:
            stats = calcular_estadisticas(inventario)
            if stats:
                print("\n--- ESTADÍSTICAS ---")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total: {stats['valor_total']}")
                print(f"Más caro: {stats['producto_mas_caro']}")
                print(f"Mayor stock: {stats['producto_mayor_stock']}")

        elif opcion == 7:
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                decision = input("¿Sobrescribir inventario? (S/N): ").lower()

                if decision == "s":
                    inventario = nuevos
                else:
                    # Fusión
                    for nuevo in nuevos:
                        existente = buscar_producto(inventario, nuevo["nombre"])

                        if existente:
                            existente["cantidad"] += nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            inventario.append(nuevo)

        elif opcion == 9:
            star = 1
            print("Saliendo es saliendo...")
            break

        else:
            print("Opción inválida")

    except ValueError:
        print("Entrada inválida, intenta de nuevo")
    except Exception as e:
        print(f"Error inesperado: {e}")

