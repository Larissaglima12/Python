numero = int(input("Número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Resultado: DIVISÍVEL POR 3 E 5")
elif numero % 3 == 0:
    print("Resultado: DIVISÍVEL APENAS POR 3")
elif numero % 5 == 0:
    print("Resultado: DIVISÍVEL APENAS POR 5")
else:
    print("Resultado: NÃO DIVISÍVEL POR 3 NEM 5")