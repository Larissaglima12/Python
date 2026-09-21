salario = float(input("Salário atual: R$ "))

if salario <= 1500.00:
    percentual = 15
elif salario <= 3000.00:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Percentual: {percentual}%")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")