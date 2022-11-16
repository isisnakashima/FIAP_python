inventario = []
# para criar uma lista é colocar o nome dela e []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    # depois coloca o nome da lista + append
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = (input("Digite 'S' para continuar: ")).upper()

    for elemento in inventario:
        print(elemento)
