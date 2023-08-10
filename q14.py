boi_mais_gordo= {"numero": 0, "peso": 0}
boi_mais_magro= {"numero": 0, "peso": float("inf")}

for i in range (1,91):
    numero = int(input(f"Digite o número de identificação do boi {i}: "))
    peso= float(input("Digite o peso do boi {i} (em kg): "))
    
    if peso > boi_mais_gordo["peso"]:
        boi_mais_gordo["numero"] = numero
        boi_mais_gordo["peso"] = peso
    
    if peso > boi_mais_magro["peso"]:
        boi_mais_magro["numero"] = numero
        boi_mais_magro["peso"] = peso
        
print(f"O boi mais gordo é o número {boi_mais_gordo['numero']} com o peso de {boi_mais_gordo['peso']} kg.")
print(f"O boi mais magro é o número {boi_mais_magro['numero']} com o peso de {boi_mais_magro['peso']} kg.")
