a1 = float(input("Adicione o valor inicial: "))
n = int(input("Adicione o valor de termos: "))
q = float(input("Adicione o valor da razão (deve ser maior ou igual a 2): "))

if q <= 2:
    print("A razão deve ser igual a 2")
else:
    som = a1 * (q**n - 1)  / (q-1)
    print(f"A soma é {som}.")