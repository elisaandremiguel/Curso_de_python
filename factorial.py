numero = int(input('Factorial de: '))

if (numero == 0):
    print(f"{numero}! =", 1)
else:
    if numero < 0:
        print("Não existe fatorial de \
            números negativos")
    else:
        fatorial = 1
        numero1 = numero
        while numero1 >= 1:
            fatorial = fatorial * numero1
            numero1 -= 1
    print(f'{numero}! =', fatorial)
