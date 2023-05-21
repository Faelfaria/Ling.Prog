altura = float(input("Digite a altura da pessoa em metros: "))
sexo = int(input("Digite o sexo da pessoa (1 para feminino, 2 para masculino): "))

if sexo == 1:
    peso_ideal = 62.1 * altura - 44.7
    print("O peso ideal para umka mulher com a altura", altura, "é:", peso_ideal, "k.")
elif sexo == 2:
    peso_ideal = 72.7 * altura - 58
    print("O peso ideal para um homem com altura", altura, "é:", peso_ideal, "kg.")
else: 
    print("Opção inválida para o sexo.")