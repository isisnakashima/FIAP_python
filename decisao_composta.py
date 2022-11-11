nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
if idade >= 65:
    print("o paciente " + nome + " possui atendimento preferencial!")
else:
    print("O paciente " + nome + " não possui atendimento preferencial!")
