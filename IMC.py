peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)
print("Seu Imc é: ", (round(imc,1)))

if imc >16:
    print("Magreze grave")
elif imc >=16.1 and imc <=17:
    print("Magreza moderada")
elif imc >=17.1 and imc <=18.5:
    print("Magreza leve")
elif imc >=18.6 and imc <=25:
    print("Saudável")
elif imc >=25.1 and imc <=30:
    print("Sobre peso")
elif imc >=30.1 and imc <=35:
    print("Obesidade grau I")
elif imc >=35.1 and imc <=40:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
