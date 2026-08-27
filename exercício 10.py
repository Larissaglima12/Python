# Lê o salário fixo e o total vendido no mês
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total vendido no mês: "))

# Calcula 4% de comissão sobre as vendas
comissao = total_vendas * 0.04

# Salário total é o salário fixo mais a comissão
salario_total = salario_fixo + comissao

# Mostra os resultados
print("Valor da comissão:", comissao)
print("Salário total:", salario_total)
