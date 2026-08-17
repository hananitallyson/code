peso = float(input("\nDigite seu peso em kg (ex: 54.20): "))
altura = float(input("Digite sua altura em metros (ex: 1.65): "))

imc = peso / (altura ** 2)

print("Seu IMC é: %.2f"%imc)

if imc <= 18.5:
    print("Você está abaixo do peso.\n")
elif imc > 18.5 and imc < 25:
    print("Você está saudável.\n")
elif imc >= 25 and imc < 30:
    print("Você está em sobrepeso.\n")
elif imc >= 30 and imc < 35:
    print("Você está em obesidade de grau leve.\n")
elif imc >= 35 and imc < 40:
    print("Você está em obesidade de grau severa.\n")
elif imc >= 40:
    print("Você está em obesidade de grau mórbida.\n")
