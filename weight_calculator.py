altura = int(input("Digite sua altura em cm: "))

peso_homem = (altura - 100) - ((altura - 150) / 4)
peso_mulher = (altura - 100) - ((altura - 150) / 2)

print("Se for homem:", peso_homem, "kg")
print("Se for mulher:", peso_mulher, "kg")

