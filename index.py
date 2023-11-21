# Menú de operaciones
menu = """
Bienvenido/a a la práctica 5. 
Seleccione la operación que deseas ejecutar:
1. Suma
2. Producto
3. Division
4. Factorial
5. Tablas de multiplicar
6. Calculo de cuadrado y cubo
7. Promedio
8. Maximo y minimo

"""
print(menu)

# Solicitar al usuario la elección
opcion = int(input("Ingrese el número de la operación deseada: "))

# Realizar la operación seleccionada
if opcion == 1:
    # Código para la suma
    def suma(a, b):
        resultado = a + b
        return resultado

    # Solicitar al usuario que ingrese dos números
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    # Llamar a la función suma y mostrar el resultado
    resultado = suma(a, b)
    print(f"La suma de {a} y {b} es: {resultado}")

elif opcion == 2:
    # Código para la multiplicación
    def multiplicacion(a, b):
        resultado = a * b
        return resultado

    # Solicitar al usuario que ingrese dos números
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    # Llamar a la función suma y mostrar el resultado
    resultado = multiplicacion(a, b)
    print(f"La multiplicación de {a} y {b} es: {resultado}")
elif opcion == 3:
    # Código para la división
    N = int(input("Ingresa el dividendo: "))
    A = int(input("Ingresa el divisor: "))
    div = N / A
    print("La división es: ", div)

elif opcion == 4:
    # Código para el factorial
    N = int(input("Ingresa el número: "))
    F = 1
    x = 1
    while (x <= N):
        F = F * x
        x = x + 1
    print ("El factorial de ", N," es ", F)
elif opcion == 5:
    # Código para las tablas de multiplicar
    numero_tabla = int(input("Ingrese el número de tabla que desea imprimir: "))
    for i in range(1, 11):
        resultado = numero_tabla * i
        print(f"{numero_tabla} x {i} = {resultado}")
elif opcion == 6:
    # Código para el cálculo de cuadrado y cubo
    N=int(input("\nIntroduzca un número: "))
    N2=N**2
    N3=N**3
    print(N, " al cuadrado es: ", N2)
    print(N, " al  cubo es: ", N3)
elif opcion == 7:
    # Código para el promedio
    s = 0 # Asignamos el valor 0 al contador s
    x = int(input("Número de elementos en la serie: "))

    if x > 0:
       for n in range(x):
           numbers = float(input("Ingresa el número (-1 para detener): "))
           if numbers == -1:
               break  # Sale del bucle si se ingresa -1
           s += numbers
           media = s / (n + 1)  # Calcula la media hasta el número actual
        
       print("El promedio es: ", media)
    else:
       print("Error en la secuencia")
       exit()
       
elif opcion == 8:
    # Código para máximo y mínimo
    cantidad_numeros = int(input("Ingrese la cantidad de números enteros que desea introducir: "))
    
    if cantidad_numeros <= 0:
        print("Ingrese un número mayor que cero.")
    else:
        numeros = [int(input(f"Ingrese el número {i + 1}: ")) for i in range(cantidad_numeros)]
        maximo = max(numeros)
        minimo = min(numeros)

        print(f"\nValores ingresados: {numeros}")
        print(f"Total de valores: {cantidad_numeros}")
        print(f"Valor máximo: {maximo}")
        print(f"Valor mínimo: {minimo}")
else:
    print("Opción no válida. Por favor, elija una opción del 1 al 8.")


