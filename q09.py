def calcular_peso_ideal(altura, sexo):
    if sexo.lower() == "masculino":
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == "feminino":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return "Sexo inválido. Informe 'masculino' ou 'feminino'."
    
    return peso_ideal

altura = float(input("Informe sua altura em metros: "))
sexo = input("Informe seu sexo biológico (masculino/feminino): ")

peso_ideal = calcular_peso_ideal(altura, sexo)
print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
