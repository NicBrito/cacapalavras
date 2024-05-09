import random
from unidecode import unidecode

# lista com as letras do alfabeto
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']

# printando a matriz
def printar_matriz(matriz):
    for linha in matriz: # percorrendo linha por linha da matriz
        print(f'|{"|".join([f"{letra}" for letra in linha]).upper()}|') # printando linha da matriz

# printando as palavras
def printar_palavras(palavras):
    print(f'Palavras: {", ".join(palavras).upper()}') # printando a lista de palavras

# função para verificar se o usuário ainda possui tentativas
def existe_tentativas(tentativas):
    if(tentativas == 0): # caso o usuário não tenha mais tentativas
        print("Você excedeu o número de tentativas!") # informando que o usuário excedeu o número de tentativas
        exit() # finalizando o programa
    return True # retornando que o usuário possui tentativas

# definindo tamanho da matriz
def definir_tamanho_matriz():
    tentativas = 3 # definindo a quantidade de tentativas para digitar o tamanho da matriz
    while(existe_tentativas(tentativas)): # caso precise digitar novo valor para o tamanho da matriz
        tamanho_matriz = input("Defina o tamanho da matriz quadrada: ") # definindo o tamanho da matriz
        if(tamanho_matriz.isdigit() and int(tamanho_matriz) > 0): # caso o tamanho da matriz seja um número inteiro e maior que zero
            tamanho_matriz = int(tamanho_matriz) # convertendo o tamanho da matriz para um número inteiro
            tamanho_linhas_matriz = tamanho_matriz # definindo o tamanho das linhas da matriz
            tamanho_colunas_matriz = tamanho_matriz # definindo o tamanho das colunas da matriz
            break # finalizando a definição do tamanho da matriz
        else: # caso o tamanho da matriz não seja um número inteiro e maior que zero
            print("O tamanho da matriz deve ser um número inteiro e maior que zero!") # informando que o tamanho da matriz deve ser um número inteiro e maior que zero
            tentativas -= 1 # decrementando a quantidade de tentativas
    return tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz # retornando valores da matriz

# verificando se a palavra já existe
def palavra_ja_existe(palavras, palavra_digitada):
    for palavra in palavras: # percorrendo lista de palavras
        if(palavra == palavra_digitada): # caso a palavra da lista seja igual a palavra digitada
            print("A palavra já existe!") # informando que a palavra já existe
            return True # retornando que a palavra já existe
    return False # retornando que a palavra não existe

# verificando se a palavra possui um tamanho permitido
def palavra_possui_tamanho_permitido(palavra_digitada, tamanho_matriz):
    if(len(palavra_digitada) <= tamanho_matriz): # caso o usuário digite uma palavra que possua um tamanho permitido
        return True # retornando que a palavra possui um tamanho permitido
    print("A palavra possui um tamanho não permitido!") # informando que a palavra possui um tamanho não permitido
    return False # retornando que a palavra possui um tamanho não permitido

# verificando se a palavra possui apenas letras
def palavra_possui_apenas_letras(palavra_digitada):
    if(palavra_digitada.isalpha()): # caso a palavra digitada possua apenas letras
        return True # retornando que a palavra possui apenas letras
    print("A palavra deve possuir apenas letras!") # informando que a palavra deve possuir apenas letras
    return False # retornando que a palavra não possui apenas letras

# verificando se a digitação de palavras deve ser finalizada
def finalizar_digitar_palavras(palavra_digitada):
    if(not palavra_digitada # caso o usuário não digite nada
       or palavra_digitada.replace(" ", "") == ""): # caso o usuário digite apenas espaços
        return True # retornando que a digitação de palavras deve ser finalizada
    return False # retornando que a digitação de palavras não deve ser finalizada

# criando lista de palavras
def criar_palavras(tamanho_matriz):
    print("Você deve digitar até", tamanho_matriz, "palavras com no máximo", tamanho_matriz, "letras!"
          "\nPara finalizar a digitação, digite ENTER") # informando a quantidade de palavras que o usuário deve digitar
    palavras = [] # criando lista de palavras vazia
    tentativas = 3 # definindo a quantidade de tentativas para digitar as palavras
    for indice in range(0, tamanho_matriz): # percorrendo a quantidade de palavras que o usuário deve digitar
        while(existe_tentativas(tentativas)): # caso deva digitar uma nova palavra
            palavra_digitada = unidecode(str(input(f'Digite a {indice+1}a palavra: ')).upper().replace(" ", "")) # pegando a palavra digitada, convertendo para maiúsculo e removendo espaços e acentos
            if(finalizar_digitar_palavras(palavra_digitada)): # caso o usuário não digite nada ou apenas espaços
                break # finalizando a digitação de palavras
            if(palavra_possui_tamanho_permitido(palavra_digitada, tamanho_matriz) # caso a palavra possua um tamanho permitido
               and not palavra_ja_existe(palavras, palavra_digitada) # caso a palavra não exista
               and palavra_possui_apenas_letras(palavra_digitada)): # caso a palavra possua apenas letras
                palavras.append(palavra_digitada) # adicionando palavra na lista de palavras
                break # finalizando a digitação de palavras
            else: # caso a palavra não possua um tamanho permitido, já exista ou não possua apenas letras
                tentativas -= 1 # decrementando a quantidade de tentativas
        if(finalizar_digitar_palavras(palavra_digitada)): # caso deva finalizar a digitação de palavras antes do máximo possível
            break # finalizando a digitação de palavras
    return palavras # retornando lista de palavras

# criando a matriz do tamanho definido e a preenchendo com vazios
def criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz):
    matriz = [] # criando matriz vazia
    for numero_linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        linha = [] # criando linha vazia
        for numero_coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            linha.append("") # adicionando um espaço vazio na linha
        matriz.append(linha) # adicionando linha na matriz
    return matriz # retornando matriz

# preenchendo a matriz com letras aleatorias no lugar dos vazios
def preenchendo_matriz(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for numero_linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        for numero_coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            if(matriz[numero_linha][numero_coluna] == ""): # caso a posição da matriz seja um vazio
                letra_aleatoria = random.choice(letras) # escolhendo letra aleatoria
                matriz[numero_linha][numero_coluna] = letra_aleatoria # adicionando letra aleatoria na linha
    return matriz # retornando matriz

# função para colocar as palavras na matriz
def colocando_palavras_na_matriz(matriz, palavra, direcao, linha_palavra, coluna_palavra):
    for letra in palavra: # percorrendo cada letra da palavra
        if(direcao == "horizontal"): # caso a direção seja horizontal
            matriz[linha_palavra][coluna_palavra] = letra # adicionando letra na posição da matriz
            coluna_palavra += 1 # incrementando a coluna para a próxima letra da palavra
        elif(direcao == "vertical"): # caso a direção seja vertical
            matriz[linha_palavra][coluna_palavra] = letra # adicionando letra na posição da matriz
            linha_palavra += 1 # incrementando a linha para a próxima letra da palavra
        elif(direcao == "diagonal para direita"): # caso a direção seja diagonal para a direita
            matriz[linha_palavra][coluna_palavra] = letra # adicionando letra na posição da matriz
            linha_palavra += 1 # incrementando a linha para a próxima letra da palavra
            coluna_palavra += 1 # incrementando a coluna para a próxima letra da palavra
        elif(direcao == "diagonal para esquerda"): # caso a direção seja diagonal para a esquerda
            matriz[linha_palavra][coluna_palavra] = letra # adicionando letra na posição da matriz
            linha_palavra += 1 # incrementando a linha para a próxima letra da palavra
            coluna_palavra -= 1 # decrementando a coluna para a próxima letra da palavra

# função para checar sobreposição de palavras na matriz
def checar_sobreposicao_palavras(palavra, tamanho_palavra, palavra_existente_na_matriz, sobreposicao):
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
def checar_palavra_existente_na_matriz(matriz, direcao, tamanho_palavra, linha_palavra, coluna_palavra):
    palavra_existente_na_posicao = [] # criando variável para armazenar a palavra que já existe na posição
    for indice in range(0, tamanho_palavra): # percorrendo a quantidade de letras da palavra
        if(matriz[linha_palavra][coluna_palavra] == ""): # caso a posição da matriz seja um vazio
            palavra_existente_na_posicao.append("_") # adicionando um underline na variável
        else: # caso a posição da matriz não seja um vazio
            palavra_existente_na_posicao.append(matriz[linha_palavra][coluna_palavra]) # adicionando a letra existente na variável
        if(direcao == "horizontal"): # caso a direção seja horizontal
            coluna_palavra += 1 # selecionado próxima coluna para pegar a próxima letra da palavra
        elif(direcao == "vertical"): # caso a direção seja vertical
            linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
        elif(direcao == "diagonal para direita"): # caso a direção seja diagonal para a direita
            linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
            coluna_palavra += 1 # selecionado próxima coluna para pegar a próxima letra da palavra
        elif(direcao == "diagonal para esquerda"): # caso a direção seja diagonal para a esquerda
            linha_palavra += 1 # selecionado próxima linha para pegar a próxima letra da palavra
            coluna_palavra -= 1 # selecionado próxima coluna para pegar a próxima letra da palavra
    return palavra_existente_na_posicao # retornando a palavra que já existe na posição

# função para verificar se a posição escolhida para a palavra é permitida
def verificando_posicao_aleatoria(matriz, letras_palavra, linha_palavra, coluna_palavra, sobreposicao):
    if(not sobreposicao and matriz[linha_palavra][coluna_palavra] == ""): # caso não permita sobreposição e a posição da matriz seja um vazio
        return True # retornando que a posição escolhida para a palavra é permitida
    if(sobreposicao and (matriz[linha_palavra][coluna_palavra] == "" or matriz[linha_palavra][coluna_palavra] in letras_palavra)): # caso permita sobreposição e a posição da matriz seja um vazio ou contenha uma letra da palavra
        return True # retornando que a posição escolhida para a palavra é permitida
    return False # retornando que a posição escolhida para a palavra não é permitida

# função para escolher posição aleatória para a palavra
def escolher_posicao_aleatoria_para_palavra(matriz, direcao, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra, sobreposicao):
    linha_palavra = 0 # definindo zero como padrão para a linha da palavra
    coluna_palavra = 0 # definindo zero como padrão para a coluna da palavra
    while(True): # caso a posição escolhida para a palavra não seja permitida
        if(direcao == "horizontal"): # caso a direção seja horizontal
            linha_palavra = random.randint(0, tamanho_colunas_matriz-1) # escolhendo linha aleatória para a palavra
            coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra) # escolhendo coluna aleatória para a palavra
        elif(direcao == "vertical"): # caso a direção seja vertical
            linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra) # escolhendo linha aleatória para a palavra
            coluna_palavra = random.randint(0, tamanho_linhas_matriz-1) # escolhendo coluna aleatória para a palavra
        elif(direcao == "diagonal para direita"): # caso a direção seja diagonal para a direita
            linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra) # escolhendo linha aleatória para a palavra
            coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra) # escolhendo coluna aleatória para a palavra
        elif(direcao == "diagonal para esquerda"): # caso a direção seja diagonal para a esquerda
            linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra) # escolhendo linha aleatória para a palavra
            coluna_palavra = random.randint(tamanho_palavra-1, tamanho_linhas_matriz-1) # escolhendo coluna aleatória para a palavra
        if(verificando_posicao_aleatoria(matriz, letras_palavra, linha_palavra, coluna_palavra, sobreposicao)): # verificar se a posição escolhida é permitida
            break # permitir a escolha da posição para a palavra
    return linha_palavra, coluna_palavra # retornando a linha e a coluna da palavra

# função para colocar as palavras na posição escolhida
def colocar_palavras_na_posicao(matriz, palavra, direcao, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao):
    if("invertida" in direcao): # caso a direção seja invertida
        direcao = direcao.replace(" invertida", "") # removendo a palavra invertida da direção
        palavra = palavra[::-1] # invertendo a palavra
    while(True): # caso deva escolher uma nova posição para a palavra
        linha_palavra, coluna_palavra = escolher_posicao_aleatoria_para_palavra(matriz, direcao, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, tamanho_palavra, sobreposicao) # escolhendo posicao aleatoria para a palavra
        palavra_existente_na_matriz = checar_palavra_existente_na_matriz(matriz, direcao, tamanho_palavra, linha_palavra, coluna_palavra) # checar palavra que já existe nessa posição na matriz
        pode_colocar_a_palavra_na_matriz = checar_sobreposicao_palavras(palavra, tamanho_palavra, palavra_existente_na_matriz, sobreposicao) # checar se a palavra pode ser colocada na matriz
        if(pode_colocar_a_palavra_na_matriz): # caso a palavra possa ser colocada na matriz
            colocando_palavras_na_matriz(matriz, palavra, direcao, linha_palavra, coluna_palavra) # colocando a palavra na matriz
            break # não permitir a escolha de uma nova posição para a palavra

# função para contar posições permitidas
def contador_posicoes_permitidas(matriz, linha, coluna, contador):
    if(matriz[linha][coluna] == ""): # caso a posição da matriz seja um vazio
        contador += 1 # incrementando o contador
    else: # caso a posição da matriz não seja um vazio
        contador = 0 # zerando o contador
    return contador # retornando o contador

# função de verificação das diagonais para esquerda
def verificando_diagonal_para_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, linha, coluna):
    contador = 0 # criando contador
    while(linha < tamanho_linhas_matriz and coluna >= 0): # enquanto a linha for menor que o tamanho da matriz e a coluna for maior ou igual a zero
        contador = contador_posicoes_permitidas(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
        if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
            return True # retornando que a posição diagonal para a esquerda é permitida
        linha += 1 # incrementando a linha
        coluna -= 1 # incrementando a coluna
    return False # retornando que a posição diagonal para a esquerda não é permitida

# função para verificar se a posição diagonal para a esquerda é permitida
def pode_diagonal_para_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for coluna in range(tamanho_palavra - 1, tamanho_linhas_matriz - 1): # percorrendo cada coluna da matriz
        if(verificando_diagonal_para_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, 0, coluna)): # verificar se a posição diagonal para a esquerda é permitida
            return True # retornando que a posição diagonal para a esquerda é permitida
    for linha in range(0, tamanho_colunas_matriz - tamanho_palavra + 1): # percorrendo cada linha da matriz
        if(verificando_diagonal_para_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, linha, tamanho_linhas_matriz - 1)): # verificar se a posição diagonal para a esquerda é permitida
            return True # retornando que a posição diagonal para a esquerda é permitida
    return False # retornando que a posição diagonal para a esquerda não é permitida

# função de verificação das diagonais para direita
def verificando_diagonal_para_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, linha, coluna):
    contador = 0 # criando contador
    while(linha < tamanho_linhas_matriz and coluna < tamanho_colunas_matriz): # enquanto a linha e a coluna forem menores que o tamanho da matriz
        contador = contador_posicoes_permitidas(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
        if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
            return True # retornando que a posição diagonal para a direita é permitida
        linha += 1 # incrementando a linha
        coluna += 1 # incrementando a coluna
    return False # retornando que a posição diagonal para a direita não é permitida

# função para verificar se a posição diagonal para a direita é permitida
def pode_diagonal_para_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for coluna in range(0, tamanho_linhas_matriz - tamanho_palavra + 1): # percorrendo cada coluna da matriz
        if(verificando_diagonal_para_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, 0, coluna)): # verificar se a posição diagonal para a direita é permitida
            return True # retornando que a posição diagonal para a direita é permitida
    for linha in range(1, tamanho_colunas_matriz - tamanho_palavra + 1): # percorrendo cada linha da matriz
        if(verificando_diagonal_para_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, linha, 0)): # verificar se a posição diagonal para a direita é permitida
            return True # retornando que a posição diagonal para a direita é permitida
    return False # retornando que a posição diagonal para a direita não é permitida

# função para verificar se a posição vertical é permitida
def pode_vertical(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for coluna in range(0, tamanho_linhas_matriz): # percorrendo cada coluna da matriz
        contador = 0 # criando contador
        for linha in range(0, tamanho_colunas_matriz): # percorrendo cada linha da coluna
            contador = contador_posicoes_permitidas(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
            if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
                return True # retornando que a posição vertical é permitida
    return False # retornando que a posição vertical não é permitida

# função para verificar se a posição horizontal é permitida
def pode_horizontal(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for linha in range(0, tamanho_colunas_matriz): # percorrendo cada linha da matriz
        contador = 0 # criando contador
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo cada coluna da linha
            contador = contador_posicoes_permitidas(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
            if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
                return True # retornando que a posição horizontal é permitida
    return False # retornando que a posição horizontal não é permitida

# verificando posições permitidas para a palavra sem sobreposição
def verificando_matriz_sem_sobreposicao(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    posicoes = [] # criando lista de posições
    if(pode_horizontal(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição horizontal é permitida
        posicoes.extend(["horizontal", "horizontal invertida"]) # adicionando posição horizontal na lista de posições
    if(pode_vertical(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição vertical é permitida
        posicoes.extend(["vertical", "vertical invertida"]) # adicionando posição vertical na lista de posições
    if(pode_diagonal_para_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição diagonal para a direita é permitida
        posicoes.extend(["diagonal para direita", "diagonal para direita invertida"]) # adicionando posição diagonal para a direita na lista de posições
    if(pode_diagonal_para_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição diagonal para a esquerda é permitida
        posicoes.extend(["diagonal para esquerda", "diagonal para esquerda invertida"]) # adicionando posição diagonal para a esquerda na lista de posições
    return posicoes # retornando lista de posições

# função para contar posições permitidas
def contador_posicoes_permitidas_para_sobreposicao(matriz, palavra, indice_letra_na_palavra, linha, coluna):
    if(matriz[linha][coluna] == "" or matriz[linha][coluna] == palavra[indice_letra_na_palavra]): # caso a posição da matriz seja um vazio ou igual a letra da palavra
        return True # retornando que a posição é permitida
    return False # retornando que a posição não é permitida

# função para verificar se o lado direito da palavra em relação a letra escolhida é permitido
def verificando_para_direita(matriz, palavra, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, direcao, palavra_invertida):
    contador = 0 # criando contador
    for indice in range(0, tamanho_palavra_direita): # percorrendo a quantidade de letras do lado direito da palavra
        if(direcao == "horizontal"): # caso a direção seja horizontal
            if not (coluna+1 < len(matriz[linha])): # caso o próximo valor da coluna passe o limite da matriz
                return False # retornando que o lado direito da palavra não é permitido
            coluna += 1 # incrementando a coluna
        elif(direcao == "vertical"): # caso a direção seja vertical
            if not (linha+1 < len(matriz[linha])): # caso o próximo valor da linha passe o limite da matriz
                return False # retornando que o lado direito da palavra não é permitido
            linha += 1 # incrementando a linha
        elif(direcao == "diagonal para direita"): # caso a direção seja diagonal para a direita
            if not (linha+1 < len(matriz[linha]) and coluna+1 < len(matriz[linha])): # caso o próximo valor da linha ou da coluna passe o limite da matriz
                return False # retornando que o lado direito da palavra não é permitido
            linha += 1 # incrementando a linha
            coluna += 1 # incrementando a coluna
        elif(direcao == "diagonal para esquerda"): # caso a direção seja diagonal para a esquerda
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
def verificando_para_esquerda(matriz, palavra, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, direcao, palavra_invertida):
    contador = 0 # criando contador
    for indice in range(0, tamanho_palavra_esquerda): # percorrendo a quantidade de letras do lado esquerdo da palavra
        if(direcao == "horizontal"): # caso a direção seja horizontal
            if not (coluna-1 >= 0): # caso o próximo valor da coluna passe o limite da matriz
                return False # retornando que o lado esquerdo da palavra não é permitido
            coluna -= 1 # decrementando a coluna
        elif(direcao == "vertical"): # caso a direção seja vertical
            if not (linha-1 >= 0): # caso o próximo valor da linha passe o limite da matriz
                return False # retornando que o lado esquerdo da palavra não é permitido
            linha -= 1 # decrementando a linha
        elif(direcao == "diagonal para direita"): # caso a direção seja diagonal para a direita
            if not (linha-1 >= 0 and coluna-1 >= 0): # caso o próximo valor da linha ou da coluna passe o limite da matriz
                return False # retornando que o lado esquerdo da palavra não é permitido
            linha -= 1 # decrementando a linha
            coluna -= 1 # decrementando a coluna
        elif(direcao == "diagonal para esquerda"): # caso a direção seja diagonal para a esquerda
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
def pode_sobrepor(matriz, palavra, tamanho_palavra_esquerda, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, direcao, palavra_invertida):
    if(
        verificando_para_esquerda(matriz, palavra, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, direcao, palavra_invertida) # verificar se o lado esquerdo da palavra é permitido
        and
        verificando_para_direita(matriz, palavra, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, direcao, palavra_invertida) # verificar se o lado direito da palavra é permitido
      ):
        return True # retornando que a palavra pode sobrepor outra palavra
    return False # retornando que a palavra não pode sobrepor outra palavra

# função para verificar quais posições permitem sobreposição
def posicoes_permitidas_para_sobreposicao(matriz, palavra, letras_palavra, letra_na_matriz, linha, coluna):
    posicoes = [] # criando lista de posições
    for indice in range(0, letras_palavra[letra_na_matriz]): # percorrendo a quantidade de vezes que a letra existe na palavra
        if(indice == 0): # caso seja a primeira vez que a letra aparece na palavra
            indice_letra_na_palavra = palavra.index(letra_na_matriz) # índice da letra da matriz na palavra
        else: # caso não seja a primeira vez que a letra aparece na palavra
            indice_letra_na_palavra = palavra.index(letra_na_matriz, indice_letra_na_palavra+1) # índice da letra da matriz na palavra
        palavra_esquerda = palavra[:indice_letra_na_palavra] # palavra formada pelas letras à esquerda da letra escolhida na palavra
        palavra_direita = palavra[indice_letra_na_palavra+1:] # palavra formada pelas letras à direita da letra escolhida na palavra
        tamanho_palavra_esquerda = len(palavra_esquerda) # tamanho da palavra à esquerda
        tamanho_palavra_direita = len(palavra_direita) # tamanho da palavra à direita
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_esquerda, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, direcao = "horizontal", palavra_invertida = False)): # verificar se a posição horizontal permite sobreposição
            posicoes.append("horizontal") # adicionando posição horizontal na lista de posições
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_direita, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, direcao = "horizontal", palavra_invertida = True)): # verificar se a posição horizontal invertida permite sobreposição
            posicoes.append("horizontal invertida") # adicionando posição horizontal invertida na lista de posições
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_esquerda, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, direcao = "vertical", palavra_invertida = False)): # verificar se a posição vertical permite sobreposição
            posicoes.append("vertical") # adicionando posição vertical na lista de posições
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_direita, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, direcao = "vertical", palavra_invertida = True)): # verificar se a posição vertical invertida permite sobreposição
            posicoes.append("vertical invertida") # adicionando posição vertical invertida na lista de posições
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_esquerda, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, direcao = "diagonal para direita", palavra_invertida = False)): # verificar se a posição diagonal para a direita permite sobreposição
            posicoes.append("diagonal para direita") # adicionando posição diagonal para a direita na lista de posições
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_direita, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, direcao = "diagonal para direita", palavra_invertida = True)): # verificar se a posição diagonal para a direita invertida permite sobreposição
            posicoes.append("diagonal para direita invertida") # adicionando posição diagonal para a direita invertida na lista de posições
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_esquerda, tamanho_palavra_direita, indice_letra_na_palavra, linha, coluna, direcao = "diagonal para esquerda", palavra_invertida = False)): # verificar se a posição diagonal para a esquerda permite sobreposição
            posicoes.append("diagonal para esquerda") # adicionando posição diagonal para a esquerda na lista de posições
        if(pode_sobrepor(matriz, palavra, tamanho_palavra_direita, tamanho_palavra_esquerda, indice_letra_na_palavra, linha, coluna, direcao = "diagonal para esquerda", palavra_invertida = True)): # verificar se a posição diagonal para a esquerda invertida permite sobreposição
            posicoes.append("diagonal para esquerda invertida") # adicionando posição diagonal para a esquerda invertida na lista de posições
    return posicoes # retornando lista de posições

# função para verificar se a matriz permite sobreposição
def verificando_matriz_com_sobreposicao(matriz, palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    posicoes = [] # criando lista de posições
    posicoes_retornadas = [] # criando lista de posições retornadas
    for linha in range(0, tamanho_colunas_matriz): # percorrendo cada linha da matriz
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo cada coluna da linha
            letra_na_matriz = matriz[linha][coluna] # letra contida na posição atual da matriz
            if(letra_na_matriz in letras_palavra): # caso a letra na matriz esteja contida na palavra
                posicoes_retornadas.extend(posicoes_permitidas_para_sobreposicao(matriz, palavra, letras_palavra, letra_na_matriz, linha, coluna)) # verificar quais posições permitem sobreposição
    for indice in range(0, len(posicoes_retornadas)): # percorrendo a quantidade de posições retornadas
        if(posicoes_retornadas[indice] not in posicoes): # caso a posição não esteja na lista de posições
            posicoes.append(posicoes_retornadas[indice]) # adicionando a posição na lista de posições
    return posicoes # retornando lista de posições

# verificando posições permitidas para a palavra
def posicoes_permitidas_para_palavra(matriz, palavra, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao):
    posicoes = [] # criando lista de posições
    for indice in range(0, 2): # caso precise mudar o estado da sobreposição
        if(sobreposicao): # caso a palavra possa sobrepor outra palavra
            posicoes.extend(verificando_matriz_com_sobreposicao(matriz, palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)) # verificar quais posições pode ocorrer sobreposição
        if not (sobreposicao): # caso a palavra não possa sobrepor outra palavra
            posicoes.extend(verificando_matriz_sem_sobreposicao(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)) # verificar posições permitidas para a palavra sem sobreposição
        if(posicoes == [] and indice == 0): # caso não haja posições permitidas para a palavra
            sobreposicao = not sobreposicao # inverter estado da sobreposição
        else: # caso haja posições permitidas para a palavra
            return posicoes, sobreposicao # retornando lista de posições e o estado da sobreposição
    return posicoes, sobreposicao # retornando lista de posições e o estado da sobreposição

# função para escolher posição aleatória para a palavra
def aleatorizando_posicoes(matriz, palavra, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao):
    direcoes_permitidas, sobreposicao = posicoes_permitidas_para_palavra(matriz, palavra, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao) # direções permitidas para a palavra
    if(direcoes_permitidas == []): # caso não haja posições permitidas para a palavra
        return "", sobreposicao # retornando que a palavra não pode ser colocada em nenhuma posição e se a palavra pode sobrepor outra palavra
    direcao = random.choice(direcoes_permitidas) # escolhendo direção aleatória para a palavra
    return direcao, sobreposicao # retornando a direção escolhida e se a palavra pode sobrepor outra palavra

# função para colocar as palavras na matriz
def colocando_palavra_na_matriz(matriz, palavra, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    sobreposicao = random.choice([True, False]) # escolhendo aleatoriamente se a palavra vai sobrepor outra palavra
    direcao, sobreposicao = aleatorizando_posicoes(matriz, palavra, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao) # escolhendo posição aleatória para a palavra
    if(direcao == ""): # caso a palavra não possa ser colocada em nenhuma posição
        matriz = criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz) # esvaziando a matriz
        return False # recolocar as palavras na matriz
    colocar_palavras_na_posicao(matriz, palavra, direcao, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, sobreposicao) # chamar a função para colocar a palavra na posição escolhida
    return True # não recolocar as palavras na matriz

# função para registrar as letras contidas em uma palavra e a sua frequência
def registrar_letras_e_frequencia(palavra):
    letras_e_frequencia = {} # criando dicionário para armazenar as letras e a sua frequência
    for letra in palavra: # percorrendo cada letra da palavra
        if(letra in letras_e_frequencia): # caso a letra já esteja no dicionário
            letras_e_frequencia[letra] += 1 # incrementando a frequência da letra
        else: # caso a letra não esteja no dicionário
            letras_e_frequencia[letra] = 1 # adicionando a letra no dicionário e a sua frequência
    return letras_e_frequencia # retornando dicionário com as letras e a sua frequência

# colocando as palavras na matriz
def colocar_palavras_na_matriz(matriz, palavras, tamanho_linhas_matriz, tamanho_colunas_matriz):
    while(True): # caso precise recolocar as palavras na matriz
        contador = 0 # criando contador
        for palavra in palavras: # para cada palavra na lista de palavras
            tamanho_palavra = len(palavra) # tamanho da palavra
            letras_palavra = registrar_letras_e_frequencia(palavra) # letras da palavra e a sua frequência
            if not (colocando_palavra_na_matriz(matriz, palavra, tamanho_palavra, letras_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # chamar a função para colocar a palavra na matriz
                matriz = criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz) # esvaziando a matriz
                break # recolocar as palavras na matriz
            contador += 1 # incrementando o contador
        if(contador == len(palavras)): # caso todas as palavras tenham sido colocadas na matriz
            break # finalizando a colocação das palavras na matriz
    return matriz # retornando a matriz

# função principal
def main():
    tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz = definir_tamanho_matriz() # definindo o tamanho da matriz
    matriz = criar_matriz(tamanho_linhas_matriz, tamanho_colunas_matriz) # criando a matriz do tamanho definido e a preenchendo com vazios
    palavras = criar_palavras(tamanho_matriz) # criando as palavras
    palavras_do_maior_pro_menor = sorted(palavras, key=len, reverse=True) # reordenando as palavras para que as maiores fiquem primeiro
    matriz = colocar_palavras_na_matriz(matriz, palavras_do_maior_pro_menor, tamanho_linhas_matriz, tamanho_colunas_matriz) # colocando as palavras na matriz
    matriz = preenchendo_matriz(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz) # preenchendo a matriz com letras aleatorias no lugar dos vazios
    printar_matriz(matriz) # printando a matriz
    palavras_em_ordem_alfabetica = sorted(palavras) # reordenando as palavras para a ordem alfabética
    printar_palavras(palavras_em_ordem_alfabetica) # printando as palavras

# chamando a função principal
if __name__ == "__main__":
    main()