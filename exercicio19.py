num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
if num >= num2 and num >= num3:
    print("O maior número é:", num)
elif num2 >= num and num2 >= num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)
if num <= num2 and num <= num3:
    print("O menor número é:", num)
elif num2 <= num and num2 <= num3:
    print("O menor número é:", num2)
else:
    print("O menor número é:", num3)