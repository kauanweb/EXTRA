def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    notas = []
    
    for i in range(4):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    print("Média:", media)
    
    if media >= 7:
        print("APROVADO")
    else:
        nota_final = float(input("Digite a nota da prova final: "))
        notas.append(nota_final)
        
        nova_media = calcular_media(notas)
        print("Nova média:", nova_media)
        
        if nova_media >= 5:
            print("APROVADO")
        else:
            print("REPROVADO")
            
main()