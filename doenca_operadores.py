nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doencaInfectoContagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
if idade >= 65 and doencaInfectoContagiosa == "SIM":
    print("O paciente será direcionado para a sala AMARELA - COM prioridade")
elif idade < 65 and doencaInfectoContagiosa == "SIM":
    print("O paciente será direcionado para a sala AMARELA - SEM prioridade")
elif idade >= 65 and doencaInfectoContagiosa == "NAO":
    print("O paciente será direcionado para a sala BRANCA - COM prioridade")
elif idade < 65 and doencaInfectoContagiosa == "NAO":
    print("O paciente será direcionado para a sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infecto-contagiosa apenas com SIM ou NAO")
