senha = input("Digite a senha: ")
usuario = input("Digite o nome do usuario: ")

if senha != "fiap" or usuario != "admin":
    print("Senha ou usuario incorretos")
else:
    print("Acesso permitido")
#OU

if senha == "fiap" and usuario == "admin":
    print("Acesso permitido")
else:
    print("Senha ou usuario incorretos")


    #Operadores de comparação:
    # > Maior que
    # < Menor que
    # >= Maior ou igual
    # <= Menor ou igual
    # == Igualdade
    # != Diferença
