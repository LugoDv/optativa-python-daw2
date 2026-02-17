CATALOGO = {
"A001": {"nombre": "Teclado Mecánico", "precio": 49.99, "stock": 10, "peso_kg": 0.9},
"A002": {"nombre": "Ratón Gaming", "precio": 25.50, "stock": 5, "peso_kg": 0.2},
"A003": {"nombre": "Monitor 24", "precio": 149.00, "stock": 3, "peso_kg": 3.5},
"A004": {"nombre": "Auriculares", "precio": 35.99, "stock": 0, "peso_kg": 0.4},
"A005": {"nombre": "Webcam HD", "precio": 39.90, "stock": 7, "peso_kg": 0.3},
}

CODIGOS_PROMO = {
"ENVIOFREE": {"tipo": "envio", "descuento": 1.0},
"DESC10": {"tipo": "total", "descuento": 0.10},
}

# Carrito de compras actual y registro de pedidos realizados
CARRITO = {}
PEDIDOS={}
print("Parte 1 – Menú interactivo (while)")

def main():
    option=""

    # Bucle principal del menú hasta que el usuario seleccione salir (0)
    while(option!='0'):
        print("1. Ver catálogo\n2. Añadir producto al carrito\n3. Quitar producto del carrito\n4. Ver carrito\n5. Confirmar pedido\n0. Salir\n")
    
        option = input("Ingrese una opcion: ")

        # Opción 1: Mostrar todos los productos disponibles
        if option == '1':
            mostrar_catalogo(CATALOGO)

        # Opción 2: Añadir producto al carrito
        if option == '2':
            code = input("Codigo del producto: ")
            cantidad = int(input("cantidad: "))
            result = validar_codigo_producto(CATALOGO,code)
            if(result):
                agregar_al_carrito(CARRITO,CATALOGO,code,cantidad)
                print(f"el producto {code} se  ha agregado ")
            else:
                print("El producto no existe")

        # Opción 3: Eliminar producto del carrito
        if option == '3':
            mostrar_carrito(CARRITO)
            codigo = input("codigo a eliminar: ")
            eliminar_del_carrito(codigo,CARRITO)

        # Opción 4: Ver contenido del carrito
        if option == '4':
            mostrar_carrito(CARRITO)

        # Opción 5: Confirmar pedido (solo si hay productos en el carrito)
        if option == '5' and CARRITO:
            # Calcular totales (subtotal, IVA, peso)
            totales= calcular_totales(CARRITO,CATALOGO)

            # Solicitar códigos promocionales al usuario
            codigos_descunto = input("ingrese sus codigos de descuentos separados por ,")
            total_envio = calcular_envio(totales['peso_total'])

            # Separar códigos y aplicar descuentos
            codigos = codigos_descunto.split(',')
            precios_final = aplicar_promos(totales["total_sin_envio"],total_envio,*codigos)


            
            print("Detalles de compra")
            print(f"subtotal (sin IVA)->{totales['subtotal']}\niva->{totales['iva']}\npeso total->{totales['peso_total']}\ntotal con descuentos->{precios_final['total']:.2f}\nenvio->{precios_final['total_envio']:.2f}\n_______________________\nTOTAL FINAL->{precios_final['total']+precios_final['total_envio']}")
            
            confirmar = int(input("1 para confirmar\n0 cancelar"))

            if confirmar:
                # Verificar que hay stock suficiente para todos los productos
                mensaje_stock=validar_stock(CARRITO,CATALOGO)

                if mensaje_stock:
                    print("No se pudo completar la compra por los siguientes motivos:")
                    print(mensaje_stock)
                else:
                    # Descontar stock del catálogo
                    for codigo, details in CARRITO.items():
                        CATALOGO[codigo]['stock'] -= details['cantidad']

                    # Guardar pedido confirmado y vaciar carrito
                    PEDIDOS[len(PEDIDOS)+1]={'estado':'confirmado',
                                             'detalle':CARRITO.copy()}
                    CARRITO.clear()
                    print("pedido confirmado")
                    
            else:
                # Guardar pedido cancelado y vaciar carrito
                print("pedido cancelado")
                PEDIDOS[len(PEDIDOS)+1]={'estado':'cancelado',
                                         'detalle':CARRITO.copy()}
                CARRITO.clear()

        else:
            if option == '5':
                print("el carrito esta vacio")

    # Al salir del bucle, mostrar estadísticas de ventas
    else:
        if not PEDIDOS:
            print("No hubo ventas realizadas")
        else:
            mostrar_pedidos(PEDIDOS)
            producto=producto_mas_vendido(PEDIDOS)
            print("Producto mas vendido:")
            print(f"Codigo:{producto['codigo']}\nNombre:{producto['nombre']}  \nCantidad vendida:{producto['cantidad']} ")
            
            
        

# Parte 2 – Funciones obligatorias
def mostrar_carrito(carrito):
    if(not carrito):
        print("El carrito está vacío")
        return

    for codigo, details in carrito.items():
        print(f"Codigo:{codigo} Nombre:{details['nombre']}  Precio:{details['precio']}  Cantidad: {details['cantidad']} ")

def mostrar_pedidos(pedidos):
    for pedido_id, pedido in pedidos.items():
        print(f"Pedido ID: {pedido_id} - Estado: {pedido['estado']}")
        for codigo, details in pedido['detalle'].items():
            print(f"  Codigo:{codigo} Nombre:{details['nombre']}  Precio:{details['precio']}  Cantidad: {details['cantidad']} ")

def mostrar_catalogo(catalogo):
    for codigo, details in catalogo.items():
        print(f"Codigo:{codigo}  Nombre:{details['nombre']}  Precio:{details['precio']}  Stock: {details['stock']} peso kg: {details['peso_kg']} ")
        
def validar_codigo_producto(catalogo,codigo):
    return codigo in catalogo

def agregar_al_carrito(carrito,catalogo,codigo,cantidad):
    result = codigo in carrito

    if result:
        # Si el producto ya está en el carrito, incrementar cantidad
        carrito[codigo]['cantidad']+=cantidad
    else:
        # Si es nuevo, añadir con todos sus datos
        carrito[codigo] ={
           'cantidad': cantidad,
           'nombre':catalogo[codigo]['nombre'],
           'precio':catalogo[codigo]['precio'],
           'peso':catalogo[codigo]['peso_kg'],
           }     

def eliminar_del_carrito(codigo,carrito):
    if codigo in carrito:
        del carrito[codigo]
        print("producto eliminado del carrito")
    else:
        print("producto no encontrado")

def calcular_totales(carrito,catalogo,iva=0.21):
    total_sin_iva = 0
    total_peso=0

    # Sumar precios y pesos de todos los productos
    for codigo, details in carrito.items():
        cantidad = details['cantidad']
        peso=details['peso']
        total_sin_iva+= details['precio']*cantidad
        total_peso+=peso*cantidad

    total_iva = total_sin_iva*iva

    return {
        'subtotal':total_sin_iva,
        'iva':total_iva,
        'peso_total':total_peso,
        'total_sin_envio':total_sin_iva+total_iva,
        }

def calcular_envio(peso_total,zona="PENINSULA"):
    precio_kg=1.5
    base=5
    # Envíos fuera de península tienen tarifa base más alta
    if(zona!="PENINSULA"):
        base=10

    return peso_total*precio_kg+base  

def aplicar_promos(total,envio,*codigos):
    for cod in codigos:
        if cod in CODIGOS_PROMO:
            # Descuento en envío o en total según tipo de promoción
            if(CODIGOS_PROMO[cod]['tipo']=="envio"):
                envio = envio - envio*CODIGOS_PROMO[cod]['descuento']
            else:
                total = total - total*CODIGOS_PROMO[cod]['descuento']

    return {"total":total,'total_envio':envio}

def validar_stock(carrito,catalogo):
    message=""

    # Revisar cada producto del carrito contra el stock disponible
    for product, details in carrito.items():
        if catalogo[product]['stock'] < details['cantidad']:
            message += f"Stock insuficiente para el producto {product}\n"

    return message

def producto_mas_vendido(pedidos):
    ventas_por_producto = {}

    # Sumar cantidades vendidas de cada producto en pedidos confirmados
    for pedido_id, pedido in pedidos.items():
        if pedido['estado'] == 'confirmado':
            for codigo, details in pedido['detalle'].items():
                if codigo in ventas_por_producto:
                    ventas_por_producto[codigo] += details['cantidad']
                else:
                    ventas_por_producto[codigo] = details['cantidad']

    # Encontrar el producto con mayor cantidad vendida
    producto_top = max(ventas_por_producto, key=ventas_por_producto.get)

    return {'codigo':producto_top,
            'nombre':CATALOGO[producto_top]['nombre'],
            'cantidad':ventas_por_producto[producto_top]}
        
main()


