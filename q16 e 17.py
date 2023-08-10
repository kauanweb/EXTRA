cand1= 0
cand2 = 0
cand3 = 0
nulo = 0
branco = 0
eleitores = int(input("número de eleitores"))
for n in range(eleitores):
    voto = int(input("vote em 1, 2, 3, 4 ou 5:"))
if  (voto == 1):
    cand1 = cand1 + 1
elif (voto == 2):
    cand2 = cand2 + 1
elif (voto == 3):
    cand3 = cand3 + 1
elif (voto == 4):
    nulo = nulo + 1
elif (voto == 5):
    branco = branco + 1

else:
    print("voto inválido")
    print("candidato 1:", cand1)
    print("candidato 2:", cand2)
    print("candidato 3:", cand3)
    print("nulos:", nulo)
    print("brancos:", branco)