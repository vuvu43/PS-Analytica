counter = {}

while True:
    entrada = input("")

    if entrada == "f":
        break

    try:
        entrada = int(entrada)
    except:
        continue

    if entrada in counter.keys():
        counter[entrada] += 1
    else:
        counter[entrada] = 1
    

for k, v in counter.items():
    if v == 1:
        print(f"O número {k} apareceu {v} vez")
        continue

    print(f"O número {k} apareceu {v} vezes")

    