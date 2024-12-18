from constants import ACENTOS

# função para reordenar as palavras no dicionário
def palavras_reordenar(palavras, ordenacao):
    palavras_ordenadas = {} # criando dicionário vazio
    match ordenacao: # verificando a ordenação das palavras
        case "alfabética": # caso a ordenação seja alfabética
            palavras_ordenadas = dict(sorted(palavras.items(), key=lambda item: item[0].lower())) # ordenando as palavras em ordem alfabética
        case "maior para o menor": # caso a ordenação seja maior para o menor
            palavras_ordenadas = dict(sorted(palavras.items(), key=lambda item: len(item[0]), reverse=True)) # ordenando as palavras do maior para o menor
    return palavras_ordenadas # retornando dicionário de palavras ordenadas

# função para registrar as posições da palavra
def palavras_registrar_posicoes(palavras, palavra, posicao_inicial, posicao_final):
    palavras[palavra]["posicao"]["inicial"] = posicao_inicial # registrando a posição inicial da palavra
    palavras[palavra]["posicao"]["final"] = posicao_final # registrando a posição final da palavra
    return palavras # retornando dicionário de palavras e suas posições

# função para registrar as palavras
def palavras_registrar(palavras, palavra):
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

# verificando se a palavra possui um tamanho permitido
def palavras_tamanho(palavra_digitada, tamanho_matriz):
    if(1 < len(palavra_digitada) <= tamanho_matriz): # caso o usuário digite uma palavra que possua um tamanho permitido
        return True # retornando que a palavra possui um tamanho permitido
    print("A palavra possui um tamanho não permitido!") # informando que a palavra possui um tamanho não permitido
    return False # retornando que a palavra possui um tamanho não permitido

# verificando se a palavra já existe
def palavras_existe(palavras, palavra_digitada):
    for palavra in palavras: # percorrendo lista de palavras
        if(palavra == palavra_digitada): # caso a palavra da lista seja igual a palavra digitada
            print("A palavra já existe!") # informando que a palavra já existe
            return True # retornando que a palavra já existe
    return False # retornando que a palavra não existe

# verificando se a palavra possui apenas letras
def palavras_apenas_letras(palavra_digitada):
    if(palavra_digitada.isalpha()): # caso a palavra digitada possua apenas letras
        return True # retornando que a palavra possui apenas letras
    print("A palavra deve possuir apenas letras!") # informando que a palavra deve possuir apenas letras
    return False # retornando que a palavra não possui apenas letras

# verificando se a digitação de palavras deve ser finalizada
def palavras_finalizar_coleta(palavra_digitada):
    if(not palavra_digitada # caso o usuário não digite nada
       or palavra_digitada.replace(" ", "") == ""): # caso o usuário digite apenas espaços
        return True # retornando que a digitação de palavras deve ser finalizada
    return False # retornando que a digitação de palavras não deve ser finalizada

# função para remover a acentuação das palavras
def palavras_remover_acentos(palavra):
    palavra_sem_acentuacao = "" # criando variável para armazenar a palavra sem acentuação
    for letra in palavra: # percorrendo cada letra da palavra
        if(letra in ACENTOS): # caso a letra possua acento
            palavra_sem_acentuacao += ACENTOS[letra] # adicionando a letra sem acento na variável
        else: # caso a letra não possua acento
            palavra_sem_acentuacao += letra # adicionando a letra na variável
    return palavra_sem_acentuacao # retornando a palavra sem acentuação

# função para marcar a palavra no dicionário
def palavras_marcar_no_dicionario(palavras, palavra_na_matriz):
    dados_da_palavra = palavras[palavra_na_matriz] # obtendo os dados da palavra
    palavras[palavra_na_matriz.lower()] = dados_da_palavra # adicionando a palavra marcada no dicionário
    del palavras[palavra_na_matriz] # removendo a palavra não marcada do dicionário
    palavras = palavras_reordenar(palavras, "alfabética") # reordenando as palavras no dicionário para a ordem alfabética
    return palavras # retornando o dicionário com a palavra marcada

# função para descobrir a posição da palavra nas posições ditas pelo usuário
def palavras_descobrir_posicao(posicao_inicial, posicao_final):
    if(posicao_inicial[0] == posicao_final[0]): # verificando se a palavra está na horizontal
        if(posicao_inicial[1] < posicao_final[1]): # verificando se a palavra está da esquerda para a direita
            return 'horizontal' # retornando a posição da palavra
        else: # caso a palavra esteja da direita para a esquerda
            return 'horizontal invertida' # retornando a posição da palavra
    elif(posicao_inicial[1] == posicao_final[1]): # verificando se a palavra está na vertical
        if(posicao_inicial[0] < posicao_final[0]): # verificando se a palavra está de cima para baixo
            return 'vertical' # retornando a posição da palavra
        else: # caso a palavra esteja de baixo para cima
            return 'vertical invertida' # retornando a posição da palavra
    elif(posicao_inicial[0] < posicao_final[0]): # verificando se a palavra está na diagonal
        if(posicao_inicial[1] < posicao_final[1]): # verificando se a palavra está para direita
            return 'diagonal para direita' # retornando a posição da palavra
        else: # caso a palavra esteja para esquerda
            return 'diagonal para esquerda' # retornando a posição da palavra
    elif(posicao_inicial[0] > posicao_final[0]): # verificando se a palavra está na diagonal invertida
        if(posicao_inicial[1] > posicao_final[1]): # verificando se a palavra está para direita
            return 'diagonal para direita invertida' # retornando a posição da palavra
        else: # caso a palavra esteja para esquerda
            return 'diagonal para esquerda invertida' # retornando a posição da palavra
    return '' # caso a palavra não esteja em nenhuma posição válida, retornando que a posição é inválida

# função para descobrir o tamanho entre duas posições na matriz
def palavras_descobrir_tamanho(posicao_inicial, posicao_final):
    tamanho = max(abs(posicao_final[0] - posicao_inicial[0]), abs(posicao_final[1] - posicao_inicial[1])) + 1 # descobrindo o tamanho da palavra
    return tamanho # retornando o tamanho da palavra