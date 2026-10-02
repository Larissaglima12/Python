n1, n2, n3 = eval (input("Valores:"))

menor = min (n1, n2, n3)
maior = max (n1, n2, n3)

meio = (n1 + n2 + n3) - (menor + maior)
print (f"ordem crescente: {menor}, {meio}, {maior}")


