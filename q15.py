maior_idade = 0
contador_mulheres = 0
num_habitantes = int(input("Informe o número de habitantes: "))

for i in range(num_habitantes):
   print(f"\nHabitante {i + 1}:")
   sexo = input("Sexo (masculino/feminino): ")
   cor_olhos = input("Cor dos olhos (azuis/verdes/castanhos): ")
   cor_cabelos = input("Cor dos cabelos (louros/castanhos/pretos): ")
   idade = int(input("Idade: "))


if(
       sexo == "feminino"
       and 18 <= idade <= 45
       and cor_olhos == "verdes"
       and cor_cabelos == "louros"
       
):     contador_mulheres += 1


if idade > maior_idade:
    maior_idade = idade
print("\nResultados:")
print("Maior idade dos habitantes:", maior_idade)
print("Quantidade de mulheres com olhos verdes, cabelos louros e idade entre 18 e 45 anos:", contador_mulheres)    