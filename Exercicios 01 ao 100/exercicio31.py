imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Prazo: "))

prestacao = imovel / (anos * 12)
limite = salario * 0.30

print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite: R$ {limite:.2f}")

if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")