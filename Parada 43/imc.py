altura = float(input("Digite sua altura em CM: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura*altura)

if imc < 18.5:
    print("MAGREZA")

elif imc >= 18.5 and imc <= 24.9:
    print("NORMAL")

elif imc >= 25 and imc <= 29.9:
    print("SOBREPESO")

elif imc >= 30 and imc <= 39.9:
    print("OBESIDADE")

else:
    print("OBESIDADE")