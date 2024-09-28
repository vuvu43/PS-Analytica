valor = float(input(""))

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("NOTAS:")
for n in notas:
    qnt_notas = int(valor // n)
    print(f"{qnt_notas} nota(s) de R$ {n}.00")
    valor = valor - qnt_notas * n

print()
print("MOEDAS:")
for m in moedas:
    qnt_moedas = int(valor // m)
    print(f"{qnt_moedas} moeda(s) de R$ {m}")
    valor = valor - qnt_moedas * m
