def calcular_digito_verificador(dni):
    ruc_base = "10" + dni

    pesos = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    suma = 0

    for i in range(10):
        suma += int(ruc_base[i]) * pesos[i]

    resto = suma % 11
    digito = 11 - resto

    if digito == 11:
        digito = 1
    elif digito == 10:
        digito = 0

    return digito


# Pedir DNI hasta que sea correcto
while True:
    dni = input("Ingrese su DNI: ")

    if len(dni) == 8 and dni.isdigit():
        break
    else:
        print("DNI inválido. Debe tener exactamente 8 dígitos.")


# Generar RUC
digito = calcular_digito_verificador(dni)
ruc = "10" + dni + str(digito)

print("\n=== CONVERSIÓN DE DNI A RUC ===")
print("DNI:", dni)
print("Dígito verificador:", digito)
print("RUC generado:", ruc)