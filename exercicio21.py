num1 = float(input("Nota1: "))
num2 = float(input("Nota2: "))

media = (num1 + num2) / 2
print(f"Media é: {media}")
if media >= 7.0:
    print("você foi aprovado")
else:
    print("você não foi aprovado")