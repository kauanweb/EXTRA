
def eh_par_inverso(palavra1, palavra2):
    return palavra1 == palavra2[::-1]

def encontrar_pares_inversos(lista_palavras):
    pares_inversos = []
    
    for i in range(len(lista_palavras)):
        for j in range(i+1, len(lista_palavras)):
            if eh_par_inverso(lista_palavras[i], lista_palavras[j]):
                pares_inversos.append((lista_palavras[i], lista_palavras[j]))
    
    return pares_inversos

lista_palavras = ["ana", "roma", "ovo", "mar", "amor"]

pares_encontrados = encontrar_pares_inversos(lista_palavras)
print("Pares inversos encontrados:", pares_encontrados)