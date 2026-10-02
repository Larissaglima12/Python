# Lê o preço unitário, a quantidade comprada e o valor do frete
preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade comprada: "))
frete = float(input("Digite o valor do frete: "))

# Subtotal é o preço unitário multiplicado pela quantidade
subtotal = preco_unitario * quantidade

# Valor total é o subtotal mais o frete
total = subtotal + frete

# Mostra os resultados
print("Subtotal:", subtotal)
print("Valor total da compra:", total)
