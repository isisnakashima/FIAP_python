nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doencaInfectoContagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
while doencaInfectoContagiosa != "SIM" and doencaInfectoContagiosa != "NAO":
    print("Digite sim ou nao")
    doencaInfectoContagiosa = input("Suspeits de doença infecto-contagiosa?").upper()

if doencaInfectoContagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA")
else:
    print("Encaminhe o paciente para a sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ").upper()
    if genero =="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
