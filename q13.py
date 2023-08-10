alturas = []
for i in range(50):
    altura = int(input(f"Digite a altura da {i+1}º pessoa(em metros) : "))
    alturas.append(altura)

maior_alt = max(alturas)
menor_alt = min(alturas)

print(f"Maior altura: {maior_alt}")
print(f"Menor altura: {menor_alt}")