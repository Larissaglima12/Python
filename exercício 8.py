# Lê o preço do produto
preco = float(input("Digite o preço do produto: "))

# Calcula 10% de desconto
desconto = preco * 0.10

# Preço final é o preço menos o desconto
preco_final = preco - desconto

# Mostra os resultados
print("Valor do desconto:", desconto)
print("Preço final:", preco_final)