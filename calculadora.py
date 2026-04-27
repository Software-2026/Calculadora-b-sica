# Calculadora básica

print("=== CALCULADORA BÁSICA ===")

# Entrada de datos con validación
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Seleccione la operación:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    opcion = input("Ingrese una opción (1/2/3/4): ")

    # Proceso y salida
    if opcion == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif opcion == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcion == "3":
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)

    else:
        print("Opción no válida")

except ValueError:
    print("Error: debe ingresar solo números válidos, no letras ni símbolos.")