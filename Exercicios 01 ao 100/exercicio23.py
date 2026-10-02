num = int(input("digite sua idade: "))
if num <16:
    print("você não pode votar")
elif num >=16 and num <=17:
    print("voto opcinal")
elif num >70:
    print("voto opcinal")
else:
    print("voto obrigatorio")