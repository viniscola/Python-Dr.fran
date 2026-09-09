nome = input("Qual o seu nome: ")
qtdprod = int(input("Quantos produtos deseja comprar: "))
vendas = float(input("Digite o valor das vendas: "))
salariobase = 1800
comprod = 150*qtdprod

salariofinal = salariobase + comprod + (vendas *0.03)
#print(salariofinal)
print(f'{nome}, voce vendeu: {qtdprod}, e seu salário final ficou:  {salariofinal}')