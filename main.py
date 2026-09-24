def mostrar_menu():
    """Muestra el menú principal."""
    print("\n---- SISTEMA DE PEDIDOS ----")
    print("1. Registrar pedido")
    print("2. Salir")


def validar_texto(texto):
    """Valida que el texto no esté vacío."""
    return texto.strip() != ""


def validar_codigo(codigo):
    """Valida que el código del pedido tenga al menos 5 caracteres."""
    return codigo.strip() != "" and len(codigo) >= 5


def validar_tipo(tipo):
    """Valida el tipo de pedido."""

    tipos_validos = [
        "delivery",
        "recojo",
        "reserva",
        "reclamo",
        "otro"
    ]

    return tipo.lower() in tipos_validos


def asignar_prioridad(tipo):
    """Asigna prioridad según el tipo de pedido."""

    tipo = tipo.lower()

    if tipo == "reclamo":
        return "ALTA"

    elif tipo == "delivery":
        return "MEDIA"

    else:
        return "BAJA"


def mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad):
    """Muestra el resumen del pedido."""

    print("\n---- RESUMEN DEL PEDIDO ----")
    print("Código       :", codigo)
    print("Cliente      :", nombre)
    print("Tipo         :", tipo)
    print("Descripción  :", descripcion)
    print("Prioridad    :", prioridad)
    print("-" * 35)


def registrar_pedido():

    # Validar código
    while True:
        codigo = input("Código del pedido: ")

        if validar_codigo(codigo):
            break

        print("Error: el código debe tener mínimo 5 caracteres.")

    # Validar nombre
    while True:
        nombre = input("Nombre del cliente: ")

        if validar_texto(nombre):
            break

        print("Error: el nombre es obligatorio.")

    # Validar tipo
    while True:
        tipo = input(
            "Tipo de pedido "
            "(delivery, recojo, reserva, reclamo, otro): "
        )

        if validar_tipo(tipo):
            break

        print("Error: tipo de pedido no válido.")

    # Validar descripción
    while True:
        descripcion = input("Descripción del pedido: ")

        if validar_texto(descripcion):
            break

        print("Error: la descripción es obligatoria.")

    # Asignar prioridad
    prioridad = asignar_prioridad(tipo)

    # Mostrar resumen
    mostrar_resumen(
        codigo,
        nombre,
        tipo,
        descripcion,
        prioridad
    )


# Programa principal
while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        print("\nRegistro de 3 pedidos")

        for i in range(1, 4):
            print(f"\n--- Pedido {i} ---")
            registrar_pedido()

    elif opcion == "2":

        print("Programa finalizado.")
        break

    else:

        print("Opción inválida.")
        
