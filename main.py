
def marcar_pares(numero):
    for i in range(numero + 1):
        if i % 2 == 0:
            print(i, "par")
        else:
            print(i)

# Ejemplo de uso
num = int(input("Ingresá un número entero positivo: "))
marcar_pares(num)
