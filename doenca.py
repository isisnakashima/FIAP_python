nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doencaInfectoContagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
if idade >= 65:
    print("O paciente " + nome + " possui atendimento prioritário!")
elif doencaInfectoContagiosa == "SIM":
    print("O paciente " + nome + " deve ser redirecionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")
