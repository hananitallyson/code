nota1 = float(input("Digite a nota 1: "))
while nota1 > 10:
    print("A nota não pode ser maior que 10.")
    nota1 = float(input("Digite a nota 1: "))

nota2 = float(input("Digita a nota 2: "))
while nota2 > 10:
    print("A nota não pode ser maior que 10.")
    nota2 = float(input("Digite a nota 1: "))

nota3 = float(input("Digite a nota 3: "))
while nota3 > 10:
    print("A nota não pode ser maior que 10.")
    nota3 = float(input("Digite a nota 1: "))

nota_final = (nota1 + nota2 + nota3) / 3

print("\nSua nota final é: ", round(nota_final, 2))

if nota_final >= 7:
    print("Aprovado!\n")
else:
    print("Reprovado!\n")
