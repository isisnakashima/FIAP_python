nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doencaInfectoContagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO

while doencaInfectoContagiosa == "SIM" and doencaInfectoContagiosa != "NAO":
    print("Digite SIM ou NAO")
    doencaInfectoContagiosa = input("Suspeita de doença infecto-contagiosa? ")

if doencaInfectoContagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA")
else:
    print("Encaminhe o paciente para a sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")

genero = input("Digite o gênero do paciente: ")
gravidez = input("A paciente está grávida? ").upper()

while genero == "FEMININO" and idade > 10 and gravidez == "SIM":
    print("Paciente COM prioridade")

else:
    print("Paciente SEM prioridade")
