import random
from input_handlers import solicitar_tamanho_matriz, coletar_palavras
from matrix import gerar_matriz_vazia, preencher_matriz_com_letras_aleatorias
from words import reordenar_palavras, registrar_posicoes_da_palavra
from overlap_validators import verificar_posicoes_com_sobreposicao
from no_overlap_validators import verificar_posicoes_sem_sobreposicao

# função para colocar as palavras na matriz
def inserir_palavra_na_posicao_escolhida(matriz, palavras, palavra, posicao, linha_palavra, coluna_palavra):
    posicao_inicial = (linha_palavra+1, coluna_palavra+1) # definindo a posição inicial da palavra
    for indice, letra in enumerate(palavra): # percorrendo cada letra da palavra
        matriz[linha_palavra][coluna_palavra] = letra # adicionando letra na posição da matriz
        if(indice+1 == len(palavra)): # caso a palavra tenha sido completamente inserida na matriz
            break # finalizando a inserção da palavra na matriz
        match posicao: # verificando a posição da palavra
            case "horizontal": # caso a posição seja horizontal
                coluna_palavra += 1 # incrementando a coluna para a próxima letra da palavra
            case "vertical": # caso a posição seja vertical
                linha_palavra += 1 # incrementando a linha para a próxima letra da palavra
            case "diagonal para direita": # caso a posição seja diagonal para a direita
                linha_palavra += 1 # incrementando a linha para a próxima letra da palavra
                coluna_palavra += 1 # incrementando a coluna para a próxima letra da palavra
            case "diagonal para esquerda": # caso a posição seja diagonal para a esquerda
                linha_palavra += 1 # incrementando a linha para a próxima letra da palavra
                coluna_palavra -= 1 # decrementando a coluna para a próxima letra da palavra
    posicao_final = (linha_palavra+1, coluna_palavra+1) # definindo a posição final da palavra
    if(palavra not in palavras): # caso a palavra não esteja no dicionário de palavras
        palavra = palavra[::-1] # invertendo a palavra
        posicao_inicial, posicao_final = posicao_final, posicao_inicial # invertendo a posição inicial e final da palavra
    palavras = registrar_posicoes_da_palavra(palavras, palavra, posicao_inicial, posicao_final) # registrando as posições da palavra
    return palavras # retornando dicionário de palavras e suas posições

# função para checar sobreposição de palavras na matriz
def verificar_sobreposicao_palavras(palavra, tamanho_palavra, palavra_existente_na_matriz, sobreposicao):
    if(all(letra == "_" for letra in palavra_existente_na_matriz)): # caso a palavra existente na matriz seja composta apenas por vazios
        if not (sobreposicao): # caso não permita sobreposição
            return True # retornando que a palavra pode ser colocada na matriz
        return False # caso permita sobreposição, retornando que a palavra não pode ser colocada na matriz
    if not (sobreposicao): # caso a palavra existente na matriz não seja composta apenas por vazios e não permita sobreposição
        return False # retornando que a palavra não pode ser colocada na matriz
    contador = 0 # criando contador
    for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
        if(palavra_existente_na_matriz[indice] == "_" or palavra_existente_na_matriz[indice] == palavra[indice]): # caso a letra da palavra existente na matriz seja um vazio ou igual a letra da palavra
            contador += 1 # incrementando o contador
        else: # caso a letra da palavra existente na matriz não seja um vazio ou igual a letra da palavra
            contador = 0 # zerando o contador
    if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
        return True # retornando que a palavra pode ser colocada na matriz
    return False # retornando que a palavra não pode ser colocada na matriz

# função para pegar a palavra que já existe na matriz
def obter_palavra_existente_na_matriz(matriz, posicao, tamanho_palavra, linha_palavra, coluna_palavra):
    palavra_existente_na_posicao = [] # criando variável para armazenar a palavra que já existe na posição
    for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
        if(matriz[linha_palavra][coluna_palavra] == ""): # caso a posição da matriz seja um vazio
            palavra_existente_na_posicao.append("_") # adicionando um underline na variável
        else: # caso a posição da matriz não seja um vazio
            palavra_existente_na_posicao.append(matriz[linha_palavra][coluna_palavra]) # adicionando a letra existente na variável
        match posicao: # verificando a posição da palavra
            case "horizontal": # caso a posição seja horizontal
                coluna_palavra += 1 # selecionado próxima coluna para pegar a próxima letra da palavra
            case "vertical": # caso a posição seja vertical
                linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
            case "diagonal para direita": # caso a posição seja diagonal para a direita
                linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
                coluna_palavra += 1 # selecionado próxima coluna para pegar a próxima letra da palavra
            case "diagonal para esquerda": # caso a posição seja diagonal para a esquerda
                linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
                coluna_palavra -= 1 # selecionado próxima coluna para pegar a próxima letra da palavra
    return palavra_existente_na_posicao # retornando a palavra que já existe na posição

# função para verificar se a posição escolhida para a palavra é permitida
def validar_posicao_palavra(matriz, palavras, palavra, linha_palavra, coluna_palavra, sobreposicao):
    if(palavra not in palavras): # caso a palavra não esteja no dicionário de palavras
        palavra = palavra[::-1] # invertendo a palavra
    if(not sobreposicao and matriz[linha_palavra][coluna_palavra] == ""): # caso não permita sobreposição e a posição da matriz seja um vazio
        return True # retornando que a posição escolhida para a palavra é permitida
    if(sobreposicao and (matriz[linha_palavra][coluna_palavra] == "" or matriz[linha_palavra][coluna_palavra] in palavras[palavra]["letras"])): # caso permita sobreposição e a posição da matriz seja um vazio ou contenha uma letra da palavra
        return True # retornando que a posição escolhida para a palavra é permitida
    return False # retornando que a posição escolhida para a palavra não é permitida

# função para escolher posição aleatória para a palavra
def escolher_posicao_palavra(matriz, palavras, palavra, posicao, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra, sobreposicao):
    linha_palavra = 0 # definindo zero como padrão para a linha da palavra
    coluna_palavra = 0 # definindo zero como padrão para a coluna da palavra
    while(True): # caso a posição escolhida para a palavra não seja permitida
        match posicao: # verificando a posição da palavra
            case "horizontal": # caso a posição seja horizontal
                linha_palavra = random.randint(0, tamanho_colunas_matriz-1) # escolhendo linha aleatória para a palavra
                coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra) # escolhendo coluna aleatória para a palavra
            case "vertical": # caso a posição seja vertical
                linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra) # escolhendo linha aleatória para a palavra
                coluna_palavra = random.randint(0, tamanho_linhas_matriz-1) # escolhendo coluna aleatória para a palavra
            case "diagonal para direita": # caso a posição seja diagonal para a direita
                linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra) # escolhendo linha aleatória para a palavra
                coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra) # escolhendo coluna aleatória para a palavra
            case "diagonal para esquerda": # caso a posição seja diagonal para a esquerda
                linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra) # escolhendo linha aleatória para a palavra
                coluna_palavra = random.randint(tamanho_palavra-1, tamanho_linhas_matriz-1) # escolhendo coluna aleatória para a palavra
        if(validar_posicao_palavra(matriz, palavras, palavra, linha_palavra, coluna_palavra, sobreposicao)): # verificar se a posição escolhida é permitida
            break # permitir a escolha da posição para a palavra
    return linha_palavra, coluna_palavra # retornando a linha e a coluna da palavra

# função para colocar as palavras na posição escolhida
def posicionar_palavra_na_matriz(matriz, palavras, palavra, posicao, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao):
    if("invertida" in posicao): # caso a posição seja invertida
        posicao = posicao.replace(" invertida", "") # removendo a palavra invertida da posição
        palavra = palavra[::-1] # invertendo a palavra
    while(True): # caso deva escolher uma nova posição para a palavra
        linha_palavra, coluna_palavra = escolher_posicao_palavra(matriz, palavras, palavra, posicao, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra, sobreposicao) # escolhendo posicao aleatoria para a palavra
        palavra_existente_na_matriz = obter_palavra_existente_na_matriz(matriz, posicao, tamanho_palavra, linha_palavra, coluna_palavra) # checar palavra que já existe nessa posição na matriz
        if(palavra_existente_na_matriz == list(palavra)): # caso a palavra existente na matriz seja igual a palavra
            return False, palavras # retornando que a palavra não pode ser colocada na matriz e o dicionário de palavras
        if(verificar_sobreposicao_palavras(palavra, tamanho_palavra, palavra_existente_na_matriz, sobreposicao)): # checar se a palavra pode ser colocada na matriz
            palavras = inserir_palavra_na_posicao_escolhida(matriz, palavras, palavra, posicao, linha_palavra, coluna_palavra) # colocando a palavra na matriz
            return True, palavras # retornando que a palavra foi colocada na matriz e o dicionário de palavras

# verificando posições permitidas para a palavra
def obter_posicoes_para_palavra(matriz, palavras, palavra, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao):
    posicoes = [] # criando lista de posições
    for indice in range(0, 2): # caso precise mudar o estado da sobreposição
        if(sobreposicao): # caso a palavra possa sobrepor outra palavra
            posicoes.extend(verificar_posicoes_com_sobreposicao(matriz, palavras, palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)) # verificar quais posições pode ocorrer sobreposição
        if not (sobreposicao): # caso a palavra não possa sobrepor outra palavra
            posicoes.extend(verificar_posicoes_sem_sobreposicao(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)) # verificar posições permitidas para a palavra sem sobreposição
        if(posicoes == [] and indice == 0): # caso não haja posições permitidas para a palavra
            sobreposicao = not sobreposicao # inverter estado da sobreposição
        else: # caso haja posições permitidas para a palavra
            return posicoes, sobreposicao # retornando lista de posições e o estado da sobreposição
    return posicoes, sobreposicao # retornando lista de posições e o estado da sobreposição

# função para escolher posição aleatória para a palavra
def escolher_posicao_aleatoria(matriz, palavras, palavra, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao):
    posicoes_permitidas, sobreposicao = obter_posicoes_para_palavra(matriz, palavras, palavra, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao) # posições permitidas para a palavra
    if(posicoes_permitidas == []): # caso não haja posições permitidas para a palavra
        return "", sobreposicao # retornando que a palavra não pode ser colocada em nenhuma posição e se a palavra pode sobrepor outra palavra
    posicao = random.choice(posicoes_permitidas) # escolhendo posição aleatória para a palavra
    return posicao, sobreposicao # retornando a posição escolhida e se a palavra pode sobrepor outra palavra

# função para colocar as palavras na matriz
def inserir_palavra_na_matriz(matriz, palavras, palavra, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    sobreposicao = random.choice([True, False]) # escolhendo aleatoriamente se a palavra vai sobrepor outra palavra
    posicao, sobreposicao = escolher_posicao_aleatoria(matriz, palavras, palavra, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao) # escolhendo posição aleatória para a palavra
    if(posicao == ""): # caso a palavra não possa ser colocada em nenhuma posição
        return False, palavras # recolocar as palavras na matriz
    palavra_foi_colocada, palavras = posicionar_palavra_na_matriz(matriz, palavras, palavra, posicao, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao) # colocando a palavra na matriz na posição escolhida
    if not (palavra_foi_colocada): # caso a palavra não tenha sido colocada na matriz
        return False, palavras # recolocar as palavras na matriz
    return True, palavras # não recolocar as palavras na matriz

# colocando as palavras na matriz
def inserir_palavras_na_matriz(matriz, palavras, tamanho_linhas_matriz, tamanho_colunas_matriz):
    lista_de_palavras = list(palavras.keys()) # criando lista de palavras
    while(True): # caso precise recolocar as palavras na matriz
        contador = 0 # criando contador
        for palavra in lista_de_palavras: # para cada palavra na lista de palavras
            tamanho_palavra = len(palavra) # tamanho da palavra
            palavra_foi_colocada, palavras = inserir_palavra_na_matriz(matriz, palavras, palavra, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz) # colocando a palavra na matriz
            if not (palavra_foi_colocada): # caso a palavra não possa ser colocada na matriz
                matriz = gerar_matriz_vazia(tamanho_linhas_matriz, tamanho_colunas_matriz) # esvaziando a matriz
                break # recolocar as palavras na matriz
            contador += 1 # incrementando o contador
        if(contador == len(palavras)): # caso todas as palavras tenham sido colocadas na matriz
            break # finalizando a colocação das palavras na matriz
    return matriz, palavras # retornando a matriz e as palavras

# função principal
def main():
    tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz = solicitar_tamanho_matriz() # definindo o tamanho da matriz
    matriz = gerar_matriz_vazia(tamanho_linhas_matriz, tamanho_colunas_matriz) # criando a matriz do tamanho definido e a preenchendo com vazios
    palavras = coletar_palavras(tamanho_matriz) # criando as palavras
    palavras = reordenar_palavras(palavras, "maior para o menor") # reordenando as palavras do maior para o menor
    matriz, palavras = inserir_palavras_na_matriz(matriz, palavras, tamanho_linhas_matriz, tamanho_colunas_matriz) # colocando as palavras na matriz
    matriz = preencher_matriz_com_letras_aleatorias(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz) # preenchendo a matriz com letras aleatorias no lugar dos vazios
    palavras = reordenar_palavras(palavras, "alfabética") # reordenando as palavras em ordem alfabética
    return matriz, palavras # retornando a matriz e as palavras