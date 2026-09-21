peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura * altura)
print(f"IMC: {imc:.1f}")

if imc < 18.5:
    print("Classificação: ABAIXO DA FAIXA")
elif imc < 25.0:
    print("Classificação: FAIXA NORMAL")
elif imc < 30.0:
    print("Classificação: ACIMA DA FAIXA")
else:
    print("Classificação: FAIXA ELEVADA")