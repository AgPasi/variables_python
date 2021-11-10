# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!\n')


n1 = float(input("Introduce tu primer número: "))
n2 = float(input("Introduce tu segundo número: "))

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    1) Suma
    2) Resta
    3) Multiplicacion
    4) División
    5) Exponente/Potencia
    6) Salir
    """)
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de", n1, "+", n2, "es igual a", n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de", n1, "-", n2, "es igual a", n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: De la multiplicacion", n1, "*", n2, "es igual a", n1*n2)
    elif opcion == 4:
        print(" ")
        print("RESULTADO: DE LA DIVISION ES:", n1, "/", n2, "es igual a", n1/n2 )
    elif opcion == 5:
        print(" ")
        print("RESULTADO: De ", n1, "**", n2, "es igual a", n1**n2 )
    elif opcion == 6:
        break
    else:
        print("Opción incorrecta")

print("El programa ha terminado!!")


# Empezar aquí la resolución del ejercicio
