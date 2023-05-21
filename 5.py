print("Cadastro de Clientes ")
print("0 - Fim")
print("1 - Inclui")
print("2 - Altera")
print("3 - Exclui")
print("4 - Consulta")

op = int(input("Escolha uma opção: "))

if op == 0: 
    print("Fim")
elif op == 1:
    print("Inclui")
elif op == 2:
    print("Altera")
elif op == 3:
    print("Exclui")
elif op == 4:
    print("Consulta")
else:
    print("Erro")