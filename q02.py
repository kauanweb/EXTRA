numero = float(input('Digite um número: '))
quintaPart = numero * (1/5) 
print('A quinta parte de {:.2f} é {:.2f}'.format(numero, quintaPart))

numero = float(input("Digite um número qualquer: "))
if numero < 0:
    print("O número é negativo")
elif numero > 0:
   print("O número é positivo")
else:
    print("O número é nulo")