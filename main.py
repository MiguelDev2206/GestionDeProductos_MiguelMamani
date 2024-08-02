# Diccionarios de productos
Productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

def mostrar_productos():
    print("========================================")
    print("Lista de Productos:")
    print("========================================")
    print(f"{'ID':<4} {'Producto':<15} {'Precio':<10} {'Stock':<10}")
    print("========================================")
    for key in Productos:
        print(f"{key:<4} {Productos[key]:<15} {Precios[key]:<10} {Stock[key]:<10}")
    print("========================================")

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    for key, value in Productos.items():
        if value.lower() == nombre.lower():
            print("El producto ya existe. Se procederá a agregar stock.")
            agregar_stock(key)
            return
    nuevo_id = max(Productos.keys()) + 1
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    Productos[nuevo_id] = nombre
    Precios[nuevo_id] = precio
    Stock[nuevo_id] = stock
    print("Producto agregado exitosamente.")

def agregar_stock(product_id):
    stock = int(input("Ingrese la cantidad de stock a agregar: "))
    Stock[product_id] += stock
    print("Stock actualizado exitosamente.")

def eliminar_producto():
    id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    if id_eliminar in Productos:
        eliminar_stock(id_eliminar)
    else:
        print("ID de producto no encontrado.")

def eliminar_stock(product_id):
    stock = int(input("Ingrese la cantidad de stock a eliminar: "))
    if Stock[product_id] >= stock:
        Stock[product_id] -= stock
        if Stock[product_id] == 0:
            del Productos[product_id]
            del Precios[product_id]
            del Stock[product_id]
            print("Producto eliminado exitosamente.")
        else:
            print("Stock actualizado exitosamente.")
    else:
        print("Cantidad de stock a eliminar excede el stock actual.")

def actualizar_producto():
    id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
    if id_actualizar in Productos:
        nombre = input("Ingrese el nuevo nombre del producto (o presione Enter para mantener el actual): ")
        precio = input("Ingrese el nuevo precio del producto (o presione Enter para mantener el actual): ")
        stock = input("Ingrese el nuevo stock del producto (o presione Enter para mantener el actual): ")
        
        if nombre:
            Productos[id_actualizar] = nombre
        if precio:
            Precios[id_actualizar] = float(precio)
        if stock:
            Stock[id_actualizar] = int(stock)
        print("Producto actualizado exitosamente.")
    else:
        print("ID de producto no encontrado.")

while True:
    mostrar_productos()
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    opcion = input("Elija opción: ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        eliminar_producto()
    elif opcion == '3':
        actualizar_producto()
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
