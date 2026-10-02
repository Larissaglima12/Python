# Lê os dois valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Usa uma variável auxiliar para não perder o valor durante a troca
auxiliar = A
A = B
B = auxiliar

# Mostra os valores depois da troca
print("Valor de A:", A)
print("Valor de B:", B)