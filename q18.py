nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

mediaFinal = (nota1 + nota2 + nota3 + nota4)/4
print(mediaFinal)

maior_nota = max(nota1, nota2, nota3, nota4)
menor_nota = min(nota1, nota2, nota3, nota4)

print("A maior nota foi: " ,maior_nota)
print("A menor nota foi: " ,menor_nota)
