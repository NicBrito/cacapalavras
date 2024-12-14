# função para contar posições permitidas
def contador_posicoes_permitidas_para_sobreposicao(matriz, palavra, indice_letra_na_palavra, linha, coluna):
    if(matriz[linha][coluna] == "" or matriz[linha][coluna] == palavra[indice_letra_na_palavra]): # caso a posição da matriz seja um vazio ou igual a letra da palavra
        return True # retornando que a posição é permitida
    return False # retornando que a posição não é permitida

# função para verificar se o lado direito da palavra em relação a letra escolhida é permitido
def verificar_lado_direito(matriz, palavra, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, posicao, palavra_invertida):
    contador = 0 # criando contador
    for indice in range(0, tamanho_palavra_direita): # percorrendo a quantidade de letras do lado direito da palavra
        match posicao: # verificando a posição da palavra
            case "horizontal": # caso a posição seja horizontal
                if not (coluna+1 < len(matriz[linha])): # caso o próximo valor da coluna passe o limite da matriz
                    return False # retornando que o lado direito da palavra não é permitido
                coluna += 1 # incrementando a coluna
            case "vertical": # caso a posição seja vertical
                if not (linha+1 < len(matriz[linha])): # caso o próximo valor da linha passe o limite da matriz
                    return False # retornando que o lado direito da palavra não é permitido
                linha += 1 # incrementando a linha
            case "diagonal para direita": # caso a posição seja diagonal para a direita
                if not (linha+1 < len(matriz[linha]) and coluna+1 < len(matriz[linha])): # caso o próximo valor da linha ou da coluna passe o limite da matriz
                    return False # retornando que o lado direito da palavra não é permitido
                linha += 1 # incrementando a linha
                coluna += 1 # incrementando a coluna
            case "diagonal para esquerda": # caso a posição seja diagonal para a esquerda
                if not (linha+1 < len(matriz[linha]) and coluna-1 >= 0): # caso o próximo valor da linha ou da coluna passe o limite da matriz
                    return False # retornando que o lado direito da palavra não é permitido
                linha += 1 # incrementando a linha
                coluna -= 1 # decrementando a coluna
        if(palavra_invertida): # caso a palavra seja invertida
            indice_letra_na_palavra -= 1 # decrementando o índice da letra na palavra
        else: # caso a palavra não seja invertida
            indice_letra_na_palavra += 1 # incrementando o índice da letra na palavra
        if(contador_posicoes_permitidas_para_sobreposicao(matriz, palavra, indice_letra_na_palavra, linha, coluna)): # verificar se a posição é permitida
            contador += 1 # incrementando o contador
    if(contador == tamanho_palavra_direita): # caso o contador seja igual ao tamanho do lado direito da palavra
        return True # retornando que o lado direito da palavra é permitido
    return False # retornando que o lado direito da palavra não é permitido

# função para verificar se o lado esquerdo da palavra em relação a letra escolhida é permitido
def verificar_lado_esquerdo(matriz, palavra, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, posicao, palavra_invertida):
    contador = 0 # criando contador
    for indice in range(0, tamanho_palavra_esquerda): # percorrendo a quantidade de letras do lado esquerdo da palavra
        match posicao: # verificando a posição da palavra
            case "horizontal": # caso a posição seja horizontal
                if not (coluna-1 >= 0): # caso o próximo valor da coluna passe o limite da matriz
                    return False # retornando que o lado esquerdo da palavra não é permitido
                coluna -= 1 # decrementando a coluna
            case "vertical": # caso a posição seja vertical
                if not (linha-1 >= 0): # caso o próximo valor da linha passe o limite da matriz
                    return False # retornando que o lado esquerdo da palavra não é permitido
                linha -= 1 # decrementando a linha
            case "diagonal para direita": # caso a posição seja diagonal para a direita
                if not (linha-1 >= 0 and coluna-1 >= 0): # caso o próximo valor da linha ou da coluna passe o limite da matriz
                    return False # retornando que o lado esquerdo da palavra não é permitido
                linha -= 1 # decrementando a linha
                coluna -= 1 # decrementando a coluna
            case "diagonal para esquerda": # caso a posição seja diagonal para a esquerda
                if not (linha-1 >= 0 and coluna+1 < len(matriz[linha])): # caso o próximo valor da linha ou da coluna passe o limite da matriz
                    return False # retornando que o lado esquerdo da palavra não é permitido
                linha -= 1 # decrementando a linha
                coluna += 1 # incrementando a coluna
        if(palavra_invertida): # caso a palavra seja invertida
            indice_letra_na_palavra += 1 # incrementando o índice da letra na palavra
        else: # caso a palavra não seja invertida
            indice_letra_na_palavra -= 1 # decrementando o índice da letra na palavra
        if(contador_posicoes_permitidas_para_sobreposicao(matriz, palavra, indice_letra_na_palavra, linha, coluna)): # verificar se a posição é permitida
            contador += 1 # incrementando o contador
    if(contador == tamanho_palavra_esquerda): # caso o contador seja igual ao tamanho do lado esquerdo da palavra
        return True # retornando que o lado esquerdo da palavra é permitido
    return False # retornando que o lado esquerdo da palavra não é permitido

# função para verificar se a palavra pode sobrepor outra palavra em relação a letra escolhida
def verificar_sobreposicao(matriz, palavra, tamanho_palavra_esquerda, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, posicao, palavra_invertida):
    if(palavra_invertida): # caso a palavra seja invertida
        tamanho_palavra_esquerda, tamanho_palavra_direita = tamanho_palavra_direita, tamanho_palavra_esquerda # invertendo os valores do tamanho da palavra à esquerda e à direita
    if( # verificando se ambos os lados da palavra se encaixam na matriz
        verificar_lado_esquerdo(matriz, palavra, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, posicao, palavra_invertida) # verificar se o lado esquerdo da palavra é permitido
        and
        verificar_lado_direito(matriz, palavra, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, posicao, palavra_invertida) # verificar se o lado direito da palavra é permitido
      ):
        return True # retornando que a palavra pode sobrepor outra palavra
    return False # retornando que a palavra não pode sobrepor outra palavra

# função para verificar quais posições permitem sobreposição
def obter_posicoes_com_sobreposicao(matriz, palavras, palavra, letra_na_matriz, linha, coluna):
    posicoes = [] # criando lista de posições
    lista_de_posicoes = { # criando dicionário de posições
        "horizontal": False, "horizontal": True, # posições horizontais
        "vertical": False, "vertical": True, # posições verticais
        "diagonal para direita": False, "diagonal para direita": True, # posições diagonais para a direita
        "diagonal para esquerda": False, "diagonal para esquerda": True # posições diagonais para a esquerda
    }
    for indice in range(0, palavras[palavra]["letras"][letra_na_matriz]): # percorrendo a quantidade de vezes que a letra existe na palavra
        if(indice == 0): # caso seja a primeira vez que a letra aparece na palavra
            indice_letra_na_palavra = palavra.index(letra_na_matriz) # índice da letra da matriz na palavra
        else: # caso não seja a primeira vez que a letra aparece na palavra
            indice_letra_na_palavra = palavra.index(letra_na_matriz, indice_letra_na_palavra+1) # índice da letra da matriz na palavra
        palavra_esquerda = palavra[:indice_letra_na_palavra] # palavra formada pelas letras à esquerda da letra escolhida na palavra
        palavra_direita = palavra[indice_letra_na_palavra+1:] # palavra formada pelas letras à direita da letra escolhida na palavra
        tamanho_palavra_esquerda = len(palavra_esquerda) # tamanho da palavra à esquerda
        tamanho_palavra_direita = len(palavra_direita) # tamanho da palavra à direita
        for posicao in lista_de_posicoes: # percorrendo as posições
            if(verificar_sobreposicao(matriz, palavra, tamanho_palavra_esquerda, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, posicao, palavra_invertida = lista_de_posicoes[posicao])): # verificar se a posição permite sobreposição
                posicoes.append(posicao) if not (lista_de_posicoes[posicao]) else posicoes.append(posicao + " invertida") # adicionando a posição na lista de posições
    return posicoes # retornando lista de posições

# função para verificar se a matriz permite sobreposição
def verificar_posicoes_com_sobreposicao(matriz, palavras, palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    posicoes = [] # criando lista de posições
    posicoes_retornadas = [] # criando lista de posições retornadas
    for linha in range(0, tamanho_colunas_matriz): # percorrendo cada linha da matriz
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo cada coluna da linha
            letra_na_matriz = matriz[linha][coluna] # letra contida na posição atual da matriz
            if(letra_na_matriz in palavras[palavra]["letras"]): # caso a letra na matriz esteja contida na palavra
                posicoes_retornadas.extend(obter_posicoes_com_sobreposicao(matriz, palavras, palavra, letra_na_matriz, linha, coluna)) # verificar quais posições permitem sobreposição
    for indice in range(0, len(posicoes_retornadas)): # percorrendo a quantidade de posições retornadas
        if(posicoes_retornadas[indice] not in posicoes): # caso a posição não esteja na lista de posições
            posicoes.append(posicoes_retornadas[indice]) # adicionando a posição na lista de posições
    return posicoes # retornando lista de posições