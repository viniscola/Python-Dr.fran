dia = int(input("Digite o dia da semana: "))

if dia==7 or dia==1:
    print("Final de semana")
elif dia==2 or dia==3 or dia==4 or dia==5 or dia==6:
    print("Dia útil")
else:
    print("Dia inválido")

#OU

if dia==7 or dia==1:
    print("Final de semana")
elif dia>=2 and dia<=6:
    print("Dia útil")
else:
    print("Dia inválido")