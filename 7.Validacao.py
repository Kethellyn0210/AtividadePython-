digitado = float(input("Digite sua senha: "))
senha = "1234"

while True:
    if senha == digitado:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
