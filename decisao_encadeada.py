nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
doencaInfectoContagiosa = input("Suspeita de doença infectocontagiosa? ").upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doencaInfectoContagiosa == "SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doencaInfectoContagiosa == "NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doencaInfectoContagiosa == "SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doencaInfectoContagiosa == "NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
