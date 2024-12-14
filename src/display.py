# função para exibir a matriz
def exibir_matriz(matriz):
    for linha in matriz: # percorrendo linha por linha da matriz
        print(f'|{"|".join([f"{letra}" for letra in linha])}|') # printando linha da matriz

# função para exibir as palavras
def exibir_palavras(palavras):
    print(f'{", ".join(palavras)}') # printando a lista de palavras

# função para exibir o caça-palavras
def exibir_cacapalavras(matriz, palavras):
    lista_palavras = list(palavras.keys()) # obtendo a lista de palavras
    print(f'{"-"*(len(matriz)*2+1)} CAÇA-PALAVRAS {"-"*(len(matriz)*2+1)}') # exibindo o título do caça-palavras
    for indice, linha in enumerate(matriz): # percorrendo as linhas da matriz
        print(f'|{"|".join([f"{letra}" for letra in linha])}|{" "*len(" CAÇA-PALAVRAS ")}{lista_palavras[indice] if indice < len(lista_palavras) else ""}') # exibindo as linhas do caça-palavras e as palavras