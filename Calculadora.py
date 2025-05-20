from Operaciones import suma, resta, multiplicacion, division, potencia, comparar, mcd, mcm
from Colaboradores import Creador, Colaborador

def calculadora():
    while True:
        print("\n===== Calculadora =====")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Comparar valores")
        print("7. Mínimo Común Múltiplo (MCM)")
        print("8. Máximo Común Divisor (MCD)")
        print("9. Salir")
        print("Creadores: ", Creador)
        print("Colaboradores: ", Colaborador)

        opcion = input("Seleccione una opción (1-9): ")

        if opcion == '9':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        if opcion not in [str(i) for i in range(1, 9)]:
            print("Opción no válida, por favor intente de nuevo.")
            continue

        num1 = input("Ingrese el primer número: ")
        num2 = input("Ingrese el segundo número: ")
        try:
            val1 = float(num1)
            val2 = float(num2)
        except ValueError:
            print("Entrada inválida, asegúrese de ingresar números.")
            continue

        if opcion == '1':
            print("Resultado de la suma:", suma(val1, val2))
        elif opcion == '2':
            print("Resultado de la resta:", resta(val1, val2))
        elif opcion == '3':
            print("Resultado de la multiplicación:", multiplicacion(val1, val2))
        elif opcion == '4':
            resultado = division(val1, val2)
            if resultado is None:
                print("Error: División por cero no permitida.")
            else:
                print("Resultado de la división:", resultado)
        elif opcion == '5':
            print("¿Qué valor usará como base?")
            print("1. Primer número como base")
            print("2. Segundo número como base")
            eleccion = input("Seleccione 1 o 2: ")
            if eleccion == '1':
                print("Resultado de la potencia:", potencia(val1, val2))
            elif eleccion == '2':
                print("Resultado de la potencia:", potencia(val2, val1))
            else:
                print("Selección inválida para la potencia.")
        elif opcion == '6':
            print(comparar(val1, val2))
        elif opcion == '7':
            print("El Mínimo Común Múltiplo es:", mcm(val1, val2))
        elif opcion == '8':
            print("El Máximo Común Divisor es:", mcd(val1, val2))

if __name__ == "__main__":
    calculadora()
