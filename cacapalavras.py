import random

# lista com as letras do alfabeto
letras = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
         ]

# lista com os acentos e suas respectivas letras
acentos = {
            'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
            'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
            'ç': 'c',
            'Á': 'A', 'À': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
            'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
            'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
            'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
            'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
            'Ç': 'C'
          }

# printando a matriz
def exibir_matriz(matriz):
    for linha in matriz: # percorrendo linha por linha da matriz
        print(f'|{"|".join([f"{letra}" for letra in linha]).upper()}|') # printando linha da matriz

# printando as palavras
def exibir_palavras(palavras):
    print(f'Palavras: {", ".join(palavras).upper()}') # printando a lista de palavras

# função para verificar se o usuário ainda possui tentativas
def verificar_tentativas_restantes(tentativas):
    if(tentativas == 0): # caso o usuário não tenha mais tentativas
        print("Você excedeu o número de tentativas!") # informando que o usuário excedeu o número de tentativas
        exit() # finalizando o programa
    return True # retornando que o usuário possui tentativas

# definindo tamanho da matriz
def solicitar_tamanho_matriz():
    tentativas = 3 # definindo a quantidade de tentativas para digitar o tamanho da matriz
    while(verificar_tentativas_restantes(tentativas)): # caso precise digitar novo valor para o tamanho da matriz
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

# função para reordenar as palavras no dicionário
def reordenar_palavras(palavras, ordenacao):
    palavras_ordenadas = {} # criando dicionário vazio
    match ordenacao: # verificando a ordenação das palavras
        case "alfabética": # caso a ordenação seja alfabética
            palavras_ordenadas = dict(sorted(palavras.items())) # ordenando as palavras em ordem alfabética
        case "maior para o menor": # caso a ordenação seja maior para o menor
            palavras_ordenadas = dict(sorted(palavras.items(), key=lambda item: len(item[0]), reverse=True)) # ordenando as palavras do maior para o menor
    return palavras_ordenadas # retornando dicionário de palavras ordenadas

# função para registrar as palavras
def registrar_palavras(palavras, palavra):
    letras = {} # criando dicionário de letras
    for letra in palavra: # percorrendo cada letra da palavra
        if(letra in letras): # caso a letra já exista no dicionário de letras
            letras[letra] += 1 # incrementando a quantidade da letra
        else: # caso a letra não exista no dicionário de letras
            letras[letra] = 1 # adicionando a letra no dicionário de letras
    palavras[palavra] = { # adicionando palavra no dicionário de palavras
        "letras": letras, # adicionando dicionário de letras na palavra
        "posicao": { # criando dicionário de posição
            "inicial": (0,0), # adicionando posição inicial da palavra
            "final": (0,0) # adicionando posição final da palavra
                   }
                        }
    return palavras # retornando dicionário de palavras

# verificando se a palavra possui apenas letras
def verificar_palavra_apenas_letras(palavra_digitada):
    if(palavra_digitada.isalpha()): # caso a palavra digitada possua apenas letras
        return True # retornando que a palavra possui apenas letras
    print("A palavra deve possuir apenas letras!") # informando que a palavra deve possuir apenas letras
    return False # retornando que a palavra não possui apenas letras

# verificando se a palavra já existe
def verificar_palavra_ja_existe(palavras, palavra_digitada):
    for palavra in palavras: # percorrendo lista de palavras
        if(palavra == palavra_digitada): # caso a palavra da lista seja igual a palavra digitada
            print("A palavra já existe!") # informando que a palavra já existe
            return True # retornando que a palavra já existe
    return False # retornando que a palavra não existe

# verificando se a palavra possui um tamanho permitido
def verificar_tamanho_palavra(palavra_digitada, tamanho_matriz):
    if(len(palavra_digitada) <= tamanho_matriz): # caso o usuário digite uma palavra que possua um tamanho permitido
        return True # retornando que a palavra possui um tamanho permitido
    print("A palavra possui um tamanho não permitido!") # informando que a palavra possui um tamanho não permitido
    return False # retornando que a palavra possui um tamanho não permitido

# verificando se a digitação de palavras deve ser finalizada
def finalizar_coletar_palavras(palavra_digitada):
    if(not palavra_digitada # caso o usuário não digite nada
       or palavra_digitada.replace(" ", "") == ""): # caso o usuário digite apenas espaços
        return True # retornando que a digitação de palavras deve ser finalizada
    return False # retornando que a digitação de palavras não deve ser finalizada

# função para remover a acentuação das palavras
def remover_acentos(palavra):
    palavra_sem_acentuacao = "" # criando variável para armazenar a palavra sem acentuação
    for letra in palavra: # percorrendo cada letra da palavra
        if(letra in acentos): # caso a letra possua acento
            palavra_sem_acentuacao += acentos[letra] # adicionando a letra sem acento na variável
        else: # caso a letra não possua acento
            palavra_sem_acentuacao += letra # adicionando a letra na variável
    return palavra_sem_acentuacao # retornando a palavra sem acentuação

# criando lista de palavras
def coletar_palavras(tamanho_matriz):
    print("Você deve digitar até", tamanho_matriz, "palavras com no máximo", tamanho_matriz, "letras!"
          "\nPara finalizar a digitação, digite ENTER") # informando a quantidade de palavras que o usuário deve digitar
    palavras = {} # criando dicionário de palavras
    tentativas = 3 # definindo a quantidade de tentativas para digitar as palavras
    for indice in range(0, tamanho_matriz): # percorrendo a quantidade de palavras que o usuário deve digitar
        while(verificar_tentativas_restantes(tentativas)): # caso deva digitar uma nova palavra
            palavra_digitada = remover_acentos(str(input(f'Digite a {indice+1}a palavra: ')).upper().replace(" ", "")) # pegando a palavra digitada, convertendo para maiúsculo e removendo espaços e acentos
            if(finalizar_coletar_palavras(palavra_digitada)): # caso o usuário não digite nada ou apenas espaços
                break # finalizando a digitação de palavras
            if(verificar_tamanho_palavra(palavra_digitada, tamanho_matriz) # caso a palavra possua um tamanho permitido
               and not verificar_palavra_ja_existe(palavras, palavra_digitada) # caso a palavra não exista
               and verificar_palavra_apenas_letras(palavra_digitada)): # caso a palavra possua apenas letras
                palavras = registrar_palavras(palavras, palavra_digitada) # registrando a palavra
                break # finalizando a digitação de palavras
            else: # caso a palavra não possua um tamanho permitido, já exista ou não possua apenas letras
                tentativas -= 1 # decrementando a quantidade de tentativas
        if(finalizar_coletar_palavras(palavra_digitada)): # caso deva finalizar a digitação de palavras antes do máximo possível
            break # finalizando a digitação de palavras
    return palavras # retornando lista de palavras

# criando a matriz do tamanho definido e a preenchendo com vazios
def gerar_matriz_vazia(tamanho_linhas_matriz, tamanho_colunas_matriz):
    matriz = [] # criando matriz vazia
    for linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        linha_vazia = [] # criando linha vazia
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            linha_vazia.append("") # adicionando um espaço vazio na linha
        matriz.append(linha_vazia) # adicionando linha na matriz
    return matriz # retornando matriz

# preenchendo a matriz com letras aleatorias no lugar dos vazios
def preencher_matriz_com_letras_aleatorias(matriz, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for linha in range(0, tamanho_colunas_matriz): # percorrendo linha por linha da matriz
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo coluna por coluna da matriz
            if(matriz[linha][coluna] == ""): # caso a posição da matriz seja um vazio
                letra_aleatoria = random.choice(letras) # escolhendo letra aleatoria
                matriz[linha][coluna] = letra_aleatoria # adicionando letra aleatoria na linha
    return matriz # retornando matriz

# função para registrar as posições da palavra
def registrar_posicoes_da_palavra(palavras, palavra, posicao_inicial, posicao_final):
    palavras[palavra]["posicao"]["inicial"] = posicao_inicial # registrando a posição inicial da palavra
    palavras[palavra]["posicao"]["final"] = posicao_final # registrando a posição final da palavra
    return palavras # retornando dicionário de palavras e suas posições

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

# função para contar posições permitidas
def contar_posicoes_vazias(matriz, linha, coluna, contador):
    if(matriz[linha][coluna] == ""): # caso a posição da matriz seja um vazio
        contador += 1 # incrementando o contador
    else: # caso a posição da matriz não seja um vazio
        contador = 0 # zerando o contador
    return contador # retornando o contador

# função de verificação das diagonais para esquerda
def verificar_diagonal_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, linha, coluna):
    contador = 0 # criando contador
    while(linha < tamanho_linhas_matriz and coluna >= 0): # enquanto a linha for menor que o tamanho da matriz e a coluna for maior ou igual a zero
        contador = contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
        if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
            return True # retornando que a posição diagonal para a esquerda é permitida
        linha += 1 # incrementando a linha
        coluna -= 1 # incrementando a coluna
    return False # retornando que a posição diagonal para a esquerda não é permitida

# função para verificar se a posição diagonal para a esquerda é permitida
def verificar_posicao_diagonal_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for coluna in range(tamanho_palavra - 1, tamanho_linhas_matriz - 1): # percorrendo cada coluna da matriz
        if(verificar_diagonal_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, 0, coluna)): # verificar se a posição diagonal para a esquerda é permitida
            return True # retornando que a posição diagonal para a esquerda é permitida
    for linha in range(0, tamanho_colunas_matriz - tamanho_palavra + 1): # percorrendo cada linha da matriz
        if(verificar_diagonal_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, linha, tamanho_linhas_matriz - 1)): # verificar se a posição diagonal para a esquerda é permitida
            return True # retornando que a posição diagonal para a esquerda é permitida
    return False # retornando que a posição diagonal para a esquerda não é permitida

# função de verificação das diagonais para direita
def verificar_diagonal_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, linha, coluna):
    contador = 0 # criando contador
    while(linha < tamanho_linhas_matriz and coluna < tamanho_colunas_matriz): # enquanto a linha e a coluna forem menores que o tamanho da matriz
        contador = contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
        if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
            return True # retornando que a posição diagonal para a direita é permitida
        linha += 1 # incrementando a linha
        coluna += 1 # incrementando a coluna
    return False # retornando que a posição diagonal para a direita não é permitida

# função para verificar se a posição diagonal para a direita é permitida
def verificar_posicao_diagonal_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for coluna in range(0, tamanho_linhas_matriz - tamanho_palavra + 1): # percorrendo cada coluna da matriz
        if(verificar_diagonal_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, 0, coluna)): # verificar se a posição diagonal para a direita é permitida
            return True # retornando que a posição diagonal para a direita é permitida
    for linha in range(1, tamanho_colunas_matriz - tamanho_palavra + 1): # percorrendo cada linha da matriz
        if(verificar_diagonal_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz, linha, 0)): # verificar se a posição diagonal para a direita é permitida
            return True # retornando que a posição diagonal para a direita é permitida
    return False # retornando que a posição diagonal para a direita não é permitida

# função para verificar se a posição vertical é permitida
def verificar_posicao_vertical(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for coluna in range(0, tamanho_linhas_matriz): # percorrendo cada coluna da matriz
        contador = 0 # criando contador
        for linha in range(0, tamanho_colunas_matriz): # percorrendo cada linha da coluna
            contador = contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
            if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
                return True # retornando que a posição vertical é permitida
    return False # retornando que a posição vertical não é permitida

# função para verificar se a posição horizontal é permitida
def verificar_posicao_horizontal(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    for linha in range(0, tamanho_colunas_matriz): # percorrendo cada linha da matriz
        contador = 0 # criando contador
        for coluna in range(0, tamanho_linhas_matriz): # percorrendo cada coluna da linha
            contador = contar_posicoes_vazias(matriz, linha, coluna, contador) # chamando função para contar posições permitidas
            if(contador == tamanho_palavra): # caso o contador seja igual ao tamanho da palavra
                return True # retornando que a posição horizontal é permitida
    return False # retornando que a posição horizontal não é permitida

# verificando posições permitidas para a palavra sem sobreposição
def verificar_posicoes_sem_sobreposicao(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz):
    posicoes = [] # criando lista de posições
    if(verificar_posicao_horizontal(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição horizontal é permitida
        posicoes.extend(["horizontal", "horizontal invertida"]) # adicionando posição horizontal na lista de posições
    if(verificar_posicao_vertical(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição vertical é permitida
        posicoes.extend(["vertical", "vertical invertida"]) # adicionando posição vertical na lista de posições
    if(verificar_posicao_diagonal_direita(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição diagonal para a direita é permitida
        posicoes.extend(["diagonal para direita", "diagonal para direita invertida"]) # adicionando posição diagonal para a direita na lista de posições
    if(verificar_posicao_diagonal_esquerda(matriz, tamanho_palavra, tamanho_linhas_matriz, tamanho_colunas_matriz)): # verificar se a posição diagonal para a esquerda é permitida
        posicoes.extend(["diagonal para esquerda", "diagonal para esquerda invertida"]) # adicionando posição diagonal para a esquerda na lista de posições
    return posicoes # retornando lista de posições

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